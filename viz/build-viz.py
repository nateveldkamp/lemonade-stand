#!/usr/bin/env python3
"""Generate viz/index.html from viz/skills.json.

Embeds the JSON inline so the file opens as a plain file:// URL — no server
needed. Run after build-skills-json.py whenever frontmatter changes.

The visualization is a "Google Maps for skills." The lemonade stand sits at
the center. The wheel is divided into 4 quadrants (Craft / Build / Run / Lead),
each holding several slices. A skill's distance from the center is its
*complexity level* (Rule of 3 and 10) — the business scale where it first
matters. Skills are connected by a road network = the authored "builds on"
edges (prereq -> dependent), plus on-ramps from the stand to every root skill.
The learner marks the skills they already have ("you are here"), clicks a skill
they want ("destination"), and the map charts a route: the sequence of skills
to learn to get there.

Radius (business complexity), roads (builds-on prerequisites), and tiers
(skill mastery, inside a node) are three separate channels — see
docs/skills.md.

Usage:
    python3 viz/build-viz.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_JSON = REPO_ROOT / "viz" / "skills.json"
OUTPUT = REPO_ROOT / "viz" / "index.html"


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lemonade Stand — Skill Map</title>
<style>
html, body { height: 100%; margin: 0; overflow: hidden; background: #0b1120;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
svg { width: 100vw; height: 100vh; display: block; cursor: grab; }
svg.pan { cursor: grabbing; }

.ring { fill: none; stroke: #15203a; stroke-width: 1; }
.stage-label { fill: #2f3e5c; font-size: 10px; letter-spacing: .05em; text-anchor: middle; }
.blabel { font-size: 13px; letter-spacing: .08em; font-weight: 700; text-transform: uppercase; }
.qlabel { font-size: 30px; letter-spacing: .22em; font-weight: 800;
  text-transform: uppercase; opacity: .16; }

.road { fill: none; stroke: #1c2942; stroke-width: 1.5; }
.road.route { stroke: #60a5fa; stroke-width: 3; }
.road.dim { opacity: .3; }

.node { cursor: pointer; }
.node rect { stroke-width: 1.5; }
.node text { pointer-events: none; text-anchor: middle; font-size: 10px; }
.node.dim { opacity: .22; }
.node.owned rect { stroke: #22c55e !important; stroke-width: 3 !important; }
.node.route rect { stroke: #60a5fa !important; stroke-width: 3 !important; }
.node.dest rect { stroke: #f8fafc !important; stroke-width: 3.5 !important; }

.center-g circle { fill: #d1fae5; stroke: #059669; stroke-width: 3; }
.center-g text { fill: #064e3b; font-weight: 700; pointer-events: none; text-anchor: middle; }

#tip {
  position: fixed; background: #1e293b; border: 1px solid #334155;
  border-radius: 8px; padding: 10px 14px; font-size: 12px; line-height: 1.5;
  max-width: 240px; pointer-events: none; opacity: 0; transition: opacity .12s;
  color: #e2e8f0; z-index: 9;
}
#tip b { color: #f8fafc; font-size: 13px; display: block; margin-bottom: 2px; }
#tip em { color: #94a3b8; font-style: normal; display: block; font-size: 11px; }
#tip small { color: #64748b; font-size: 10px; display: block; margin-top: 4px;
  text-transform: uppercase; letter-spacing: .06em; }

#nav {
  position: fixed; top: 16px; left: 16px; background: #1e293b;
  border: 1px solid #334155; border-radius: 10px; padding: 13px 16px;
  color: #cbd5e1; font-size: 12px; max-width: 270px; z-index: 9;
}
#nav h3 { margin: 0 0 6px; font-size: 13px; color: #f8fafc; }
#nav .muted { color: #64748b; font-size: 11px; line-height: 1.5; }
#nav .route-line { margin: 8px 0 4px; color: #93c5fd; font-weight: 600; }
#nav ol { margin: 4px 0 0; padding-left: 18px; }
#nav li { margin: 2px 0; }
#nav li.have { color: #22c55e; }
#nav button { margin-top: 10px; background: #334155; color: #e2e8f0; border: none;
  border-radius: 6px; padding: 5px 11px; font-size: 11px; cursor: pointer; }
#nav button:hover { background: #475569; }

#legend {
  position: fixed; bottom: 16px; left: 16px; background: #1e293b;
  border: 1px solid #334155; border-radius: 8px; padding: 10px 14px;
  color: #94a3b8; font-size: 11px;
}
.lr { display: flex; align-items: center; gap: 7px; margin-bottom: 5px; }
.lr:last-child { margin-bottom: 0; }
.ld { width: 13px; height: 13px; border-radius: 3px; border: 2px solid; flex-shrink: 0; }

#hint { position: fixed; bottom: 16px; right: 16px; color: #475569; font-size: 11px;
  user-select: none; text-align: right; line-height: 1.6; }
#hint b { color: #64748b; }
</style>
</head>
<body>
<svg id="viz"></svg>
<div id="tip"></div>
<div id="nav">
  <h3>Plan a route</h3>
  <div class="muted" id="nav-body">
    <b>Click</b> a skill to chart a route to it.<br>
    <b>Shift-click</b> skills you already have to set where you're starting from.
  </div>
  <button id="reset">Reset</button>
</div>
<div id="legend">
  <div class="lr"><div class="ld" style="border-color:#22c55e"></div>you have this</div>
  <div class="lr"><div class="ld" style="border-color:#60a5fa"></div>on your route</div>
  <div class="lr"><div class="ld" style="border-color:#f8fafc"></div>destination</div>
</div>
<div id="hint">scroll to zoom &nbsp;·&nbsp; drag to pan</div>
<script>const DATA = __SKILLS_DATA__;</script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
(function () {
  const { prelude, branches, skills, edges } = DATA;
  const W = innerWidth, H = innerHeight;
  // Complexity rings (Rule of 3 and 10): radius = the business scale where a
  // skill first matters. Each level is roughly a 3x step in people/scale.
  const LEVEL_DESC = ['just you', '~3 people', '~10 · locations', '~30 · first hires',
    '~100 · regional', '~300 · manufacturing', '~1,000 · national', 'global'];

  // ----- quadrants & slice ordering ----------------------------------
  const QUADRANTS = [
    { slug: 'craft', name: 'Craft', color: '#38bdf8' },
    { slug: 'build', name: 'Build', color: '#34d399' },
    { slug: 'run',   name: 'Run',   color: '#fb923c' },
    { slug: 'lead',  name: 'Lead',  color: '#a78bfa' },
  ];
  const orderedBranches = [];
  const branchColor = {};
  QUADRANTS.forEach(q => {
    const inQ = branches.filter(b => b.quadrant === q.slug);
    inQ.forEach((b, i) => {
      orderedBranches.push(b);
      const t = inQ.length > 1 ? (i - (inQ.length - 1) / 2) / inQ.length : 0;
      branchColor[b.slug] = d3.rgb(q.color).brighter(t * 1.1).formatHex();
    });
  });
  branches.forEach(b => { if (!branchColor[b.slug]) { branchColor[b.slug] = '#64748b'; orderedBranches.push(b); } });
  const N = orderedBranches.length;
  const quadrantIdxs = {};
  orderedBranches.forEach((b, i) => { (quadrantIdxs[b.quadrant] || (quadrantIdxs[b.quadrant] = [])).push(i); });

  // ----- radial layout -----------------------------------------------
  const HUB_R = 58, R0 = 150, RSTEP = 122;
  const WEDGE = 2 * Math.PI / N, FAN = WEDGE * 0.34, NW = 116, NH = 38;
  const branchAngle = {};
  orderedBranches.forEach((b, i) => { branchAngle[b.slug] = -Math.PI / 2 + WEDGE * i; });
  function stageOf(s) { return s.complexity_level == null ? 1 : s.complexity_level; }
  const maxStage = d3.max(skills, stageOf);
  const outerR = R0 + maxStage * RSTEP;

  // ----- appearance --------------------------------------------------
  function inProgress(s) { return /^tier|multi/.test(s); }
  function fillFor(s) {
    if (s === 'stub') return '#fef3c7';
    if (s === 'complete' || s === 'authored') return '#d1fae5';
    if (inProgress(s)) return '#dbeafe';
    return '#1e293b';
  }
  function strokeFor(s) {
    if (s === 'stub') return '#d97706';
    if (s === 'complete' || s === 'authored') return '#059669';
    if (inProgress(s)) return '#3b82f6';
    return '#475569';
  }
  function textFor(s) {
    if (s === 'stub') return '#92400e';
    if (s === 'complete' || s === 'authored') return '#064e3b';
    if (inProgress(s)) return '#1e40af';
    return '#cbd5e1';
  }
  function splitName(name, max) {
    if (name.length <= max) return [name];
    const mid = Math.floor(name.length / 2);
    let sp = name.lastIndexOf(' ', mid);
    if (sp < 2) sp = name.indexOf(' ', mid);
    if (sp < 0) return [name.slice(0, max - 1) + '…'];
    return [name.slice(0, sp), name.slice(sp + 1)];
  }

  // ----- place skills by (slice, stage) ------------------------------
  const groups = {};
  skills.forEach(s => { const k = s.branch + '|' + stageOf(s); (groups[k] || (groups[k] = [])).push(s); });
  const nodes = skills.map(s => {
    const st = stageOf(s), g = groups[s.branch + '|' + st], m = g.length, k = g.indexOf(s);
    const off = m > 1 ? FAN * ((k - (m - 1) / 2) / ((m - 1) / 2)) : 0;
    const a = branchAngle[s.branch] + off, r = R0 + st * RSTEP;
    const tx = Math.cos(a) * r, ty = Math.sin(a) * r;
    return { id: s.slug, slug: s.slug, branch: s.branch, name: s.name, tagline: s.tagline,
             build_state: s.build_state, stage: st, tx, ty, x: tx, y: ty };
  });
  const nodeById = Object.fromEntries(nodes.map(n => [n.id, n]));
  const nameById = Object.fromEntries(nodes.map(n => [n.id, n.name]));

  // ----- road network = authored "builds on" edges -------------------
  // Roads are the real prerequisite edges (prereq -> dependent). Plus
  // on-ramps from the stand to every root skill (one with no prereqs), so
  // a journey can always start downtown.
  const CENTER = { id: '__center__', tx: 0, ty: 0, x: 0, y: 0 };
  const roads = [], roadSet = new Set();
  function addRoad(a, b) {
    if (!a || !b) return;
    const key = a.id < b.id ? a.id + '|' + b.id : b.id + '|' + a.id;
    if (roadSet.has(key)) return;
    roadSet.add(key);
    roads.push({ a, b });
  }
  const hasPrereq = new Set(edges.map(e => e.to));
  edges.forEach(e => addRoad(nodeById[e.from], nodeById[e.to]));
  nodes.forEach(n => { if (!hasPrereq.has(n.id)) addRoad(CENTER, n); });
  // adjacency for routing
  const adj = {};
  function link(a, b) { (adj[a] || (adj[a] = [])).push(b); }
  roads.forEach(r => { link(r.a.id, r.b.id); link(r.b.id, r.a.id); });

  // ----- routing state -----------------------------------------------
  const owned = new Set();
  let dest = null;

  // multi-source BFS from owned (plus the stand) to dest; fewest new skills
  function computeRoute() {
    if (!dest) return null;
    const sources = new Set(['__center__', ...owned]);
    const prev = {}, seen = new Set(sources);
    let frontier = [...sources];
    while (frontier.length) {
      const next = [];
      for (const v of frontier) for (const w of adj[v] || []) {
        if (!seen.has(w)) { seen.add(w); prev[w] = v; next.push(w); }
      }
      frontier = next;
    }
    if (!seen.has(dest)) return null;
    const path = [];
    let cur = dest;
    while (cur != null) { path.unshift(cur); if (sources.has(cur)) break; cur = prev[cur]; }
    return path;
  }

  // ----- SVG scaffold -------------------------------------------------
  const svg = d3.select('#viz');
  const root = svg.append('g');

  for (let st = 0; st <= maxStage; st++) {
    const r = R0 + st * RSTEP;
    root.append('circle').attr('class', 'ring').attr('r', r);
  }
  const labelAngle = branchAngle[orderedBranches[0].slug] + WEDGE / 2;
  for (let st = 0; st <= maxStage; st++) {
    const r = R0 + st * RSTEP;
    root.append('text').attr('class', 'stage-label')
      .attr('x', Math.cos(labelAngle) * r).attr('y', Math.sin(labelAngle) * r)
      .attr('dy', '.35em').text('L' + st + ' · ' + (LEVEL_DESC[st] || ''));
  }
  QUADRANTS.forEach(q => {
    const idxs = quadrantIdxs[q.slug]; if (!idxs || !idxs.length) return;
    const midA = -Math.PI / 2 + WEDGE * (idxs.reduce((a, b) => a + b, 0) / idxs.length);
    const r = outerR + 150;
    root.append('text').attr('class', 'qlabel')
      .attr('x', Math.cos(midA) * r).attr('y', Math.sin(midA) * r).attr('fill', q.color)
      .attr('text-anchor', 'middle').attr('dominant-baseline', 'central').text(q.name);
  });
  orderedBranches.forEach(b => {
    const a = branchAngle[b.slug], r = outerR + 46;
    root.append('text').attr('class', 'blabel')
      .attr('x', Math.cos(a) * r).attr('y', Math.sin(a) * r).attr('fill', branchColor[b.slug])
      .attr('text-anchor', 'middle').attr('dominant-baseline', 'central').text(b.name);
  });

  // roads
  const roadSel = root.append('g').selectAll('path').data(roads).join('path').attr('class', 'road');

  // center hub
  const cg = root.append('g').attr('class', 'center-g');
  cg.append('circle').attr('r', HUB_R);
  cg.append('text').attr('y', -4).attr('dy', '.35em').attr('font-size', 12).text('The stand');
  cg.append('text').attr('y', 13).attr('font-size', 9).attr('fill', '#047857').text('you start here');

  // skill nodes
  const tip = document.getElementById('tip');
  const nodeSel = root.append('g').selectAll('g').data(nodes).join('g').attr('class', 'node')
    .call(d3.drag()
      .on('start', (ev, d) => { d._moved = false; if (!ev.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
      .on('drag', (ev, d) => { d._moved = true; d.fx = ev.x; d.fy = ev.y; })
      .on('end', (ev, d) => { if (!ev.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }))
    .on('click', onClick).on('mouseover', onOver).on('mousemove', onMove).on('mouseout', onOut);
  nodeSel.append('rect')
    .attr('x', -NW / 2).attr('y', -NH / 2).attr('width', NW).attr('height', NH).attr('rx', 6)
    .attr('fill', d => fillFor(d.build_state)).attr('stroke', d => strokeFor(d.build_state));
  nodeSel.each(function (d) {
    const g = d3.select(this), lines = splitName(d.name, 15);
    if (lines.length === 1) g.append('text').attr('y', 0).attr('dy', '.35em').attr('fill', textFor(d.build_state)).text(lines[0]);
    else {
      g.append('text').attr('y', -7).attr('fill', textFor(d.build_state)).text(lines[0]);
      g.append('text').attr('y', 8).attr('fill', textFor(d.build_state)).text(lines[1]);
    }
  });

  // ----- interaction --------------------------------------------------
  function onClick(ev, d) {
    if (d._moved) return;
    ev.stopPropagation();
    if (ev.shiftKey) {
      if (owned.has(d.id)) owned.delete(d.id); else owned.add(d.id);
      if (d.id === dest) dest = null;
    } else {
      dest = (dest === d.id) ? null : d.id;
    }
    render();
  }
  function onOver(ev, d) {
    const b = branches.find(x => x.slug === d.branch);
    tip.innerHTML = `<b>${d.name}</b><em>${d.tagline}</em>`
      + `<small>${b ? b.name : d.branch} · L${d.stage} ${LEVEL_DESC[d.stage] || ''} · ${d.build_state.replace(/-/g, ' ')}</small>`;
    tip.style.opacity = '1';
  }
  function onMove(ev) { tip.style.left = (ev.clientX + 16) + 'px'; tip.style.top = (ev.clientY - 10) + 'px'; }
  function onOut() { tip.style.opacity = '0'; }

  document.getElementById('reset').onclick = () => { owned.clear(); dest = null; render(); };

  // ----- render routing state ----------------------------------------
  const navBody = document.getElementById('nav-body');
  function ekey(a, b) { return a + '>' + b; }
  function render() {
    const route = computeRoute();
    const routeSet = new Set(route || []);
    const routeEdges = new Set();
    if (route) for (let i = 1; i < route.length; i++) { routeEdges.add(ekey(route[i - 1], route[i])); routeEdges.add(ekey(route[i], route[i - 1])); }
    const active = !!dest;

    nodeSel.classed('owned', d => owned.has(d.id))
      .classed('route', d => active && routeSet.has(d.id) && !owned.has(d.id) && d.id !== dest)
      .classed('dest', d => d.id === dest)
      .classed('dim', d => active && !routeSet.has(d.id) && !owned.has(d.id));
    roadSel.classed('route', r => routeEdges.has(ekey(r.a.id, r.b.id)))
      .classed('dim', r => active && !routeEdges.has(ekey(r.a.id, r.b.id)));

    if (!dest) {
      navBody.innerHTML = '<b>Click</b> a skill to chart a route to it.<br>'
        + '<b>Shift-click</b> skills you already have to set where you\'re starting from.'
        + (owned.size ? `<div class="route-line">${owned.size} skill${owned.size > 1 ? 's' : ''} marked as known.</div>` : '');
      return;
    }
    const steps = (route || []).filter(id => id !== '__center__');
    const toLearn = steps.filter(id => !owned.has(id));
    let html = `<div class="route-line">Route to ${nameById[dest]}</div>`;
    if (!route) html += `<div class="muted">No path found from where you are.</div>`;
    else if (toLearn.length === 0) html += `<div class="muted">You already have this skill.</div>`;
    else {
      html += `<div class="muted">${toLearn.length} skill${toLearn.length > 1 ? 's' : ''} to learn:</div><ol>`;
      steps.forEach(id => { html += `<li class="${owned.has(id) ? 'have' : ''}">${nameById[id]}${owned.has(id) ? ' ✓' : ''}</li>`; });
      html += `</ol>`;
    }
    navBody.innerHTML = html;
  }

  // ----- force settle + tick -----------------------------------------
  const sim = d3.forceSimulation(nodes)
    .force('x', d3.forceX(d => d.tx).strength(0.55))
    .force('y', d3.forceY(d => d.ty).strength(0.55))
    .force('collide', d3.forceCollide(NW / 2 + 6))
    .force('charge', d3.forceManyBody().strength(-90))
    .alphaDecay(0.04).on('tick', tick);
  function roadPath(r) {
    const sx = r.a.x, sy = r.a.y, tx = r.b.x, ty = r.b.y;
    const dx = tx - sx, dy = ty - sy, len = Math.hypot(dx, dy) || 1, c = Math.min(30, len * 0.1);
    const mx = (sx + tx) / 2 - (dy / len) * c, my = (sy + ty) / 2 + (dx / len) * c;
    return `M${sx},${sy} Q${mx},${my} ${tx},${ty}`;
  }
  function tick() {
    nodeSel.attr('transform', d => `translate(${d.x},${d.y})`);
    roadSel.attr('d', roadPath);
  }

  // ----- zoom / pan ---------------------------------------------------
  const zoom = d3.zoom().scaleExtent([0.2, 5]).on('zoom', e => {
    root.attr('transform', e.transform);
    svg.classed('pan', e.sourceEvent && e.sourceEvent.type === 'mousemove');
  });
  svg.call(zoom).on('dblclick.zoom', null);
  const fit = Math.min(W, H) * 0.5 / (outerR + 110);
  svg.call(zoom.transform, d3.zoomIdentity.translate(W / 2, H / 2).scale(fit));
  render();
}());
</script>
</body>
</html>
"""


def main() -> int:
    if not SKILLS_JSON.exists():
        print(
            f"error: {SKILLS_JSON} not found — run viz/build-skills-json.py first",
            file=sys.stderr,
        )
        return 1

    data = json.loads(SKILLS_JSON.read_text(encoding="utf-8"))
    json_str = json.dumps(data, separators=(",", ":"))
    html = HTML_TEMPLATE.replace("__SKILLS_DATA__", json_str)
    OUTPUT.write_text(html, encoding="utf-8")

    n_skills = len(data.get("skills", []))
    n_edges = len(data.get("edges", []))
    print(
        f"wrote {OUTPUT.relative_to(REPO_ROOT)}: "
        f"{n_skills} skills, {n_edges} roads (complexity-ring map + routing)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
