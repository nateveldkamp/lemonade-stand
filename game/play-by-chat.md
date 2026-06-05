# Lemonade Stand — play by chat

This is the 1979 *Lemonade Stand* (Bob Jamison / Charlie Kellner, MECC) written so **any AI assistant can run it conversationally** — no Python, no install. If you're an AI guiding a learner, you act as the game: show the weather, take their three decisions, compute the day, and report results. The numbers below match `game/lemonade.py`; keep them in sync.

## Setup
- Player starts with **$2.00** in assets.
- The game runs day by day until the player is bankrupt or chooses to stop.

## Each day, in order
1. **Weather report** — roll today's weather (below) and show it. Keep any brewing storm hidden until the results.
2. **Three decisions** — ask the player:
   1. How many **glasses** to make (cost depends on the day, below).
   2. How many **advertising signs** to make (**15¢** each).
   3. **Price** per glass, in cents.
   Re-prompt if they can't afford a choice. (Glasses × cost + signs × 15¢ must not exceed assets.)
3. **Results** — compute sales (below) and show: glasses sold, income, expenses, profit, new assets.
4. If assets fall below the cost of a single glass, they're **bankrupt** — game over.

## Cost to make one glass
- Days 1–2: **2¢** ("your mother is giving you free sugar").
- Days 3–6: **4¢** (day 3: "your mother quit giving you free sugar").
- Day 7 on: **5¢** (day 7: "the price of lemonade mix went up").

## Weather (roll each morning)
- **60% Sunny** — weather factor **1.0**.
- **20% Cloudy** — pick a chance of rain from {30, 40, 50, 60, 70}%; weather factor = **1 − rain%/100**. There's a **25%** chance this cloudy day becomes a **thunderstorm** (reveal only at results: all lemonade ruined, **0 sold**).
- **20% Hot and dry** — weather factor **2.0** (a heat wave; demand doubles). *Hot does not occur on days 1–2 — treat as sunny instead.*
- **Sunny special event (25% of sunny days): the street crew is working** — no normal traffic. Then a coin flip: 50% the crew is **thirsty** and buys **all** the glasses you made; otherwise foot traffic collapses (weather factor **0.1**).

## Sales formula
Let `price` = price in cents, `signs` = number of signs, `made` = glasses made.

```
# demand from price (sweet spot is 10¢)
if price >= 10:  base = 3000 / (price * price)          # 10^2 * 30 / price^2
else:            base = (10 - price) * 2.4 + 30

# advertising helps, with diminishing returns
ad_boost = 1 - exp(-0.5 * signs)

sold = floor(weather_factor * base * (1 + ad_boost))
sold = min(sold, made)          # can't sell more than you made
```

Special overrides: **thunderstorm → sold = 0**; **thirsty street crew → sold = made**.

Then:
```
expenses = made * cost_per_glass + signs * 0.15
income   = sold * price / 100
profit   = income - expenses
assets   = assets + profit
```

## Tone
Keep the cheerful retro flavor of the original ("** LEMONSVILLE WEATHER REPORT **", "$$ DAILY FINANCIAL REPORT $$"), but don't overdo the ALL CAPS. Make it quick and fun — a day should take a few seconds to play.

## After a few days, connect it to the real course
Once the learner has the hang of it, point out that every decision they just made is a real business skill on the [skill map](../docs/skills.md): **price → Pricing**, **signs → Marketing**, **how many glasses → Inventory & Unit economics**, **weather & storms → Decision-making & Risk**, **did you profit → Accounting**. The little game is the whole game in miniature.
