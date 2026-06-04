#!/usr/bin/env python3
"""
Lemonade Stand
A faithful Python recreation of the 1979 Apple II classic.
Original by Bob Jamison (MECC). Modified for Apple by Charlie Kellner, 1979.
"""
import math
import random

# ---------------------------------------------------------------------------
# Game constants (from original source)
# ---------------------------------------------------------------------------
STARTING_ASSETS = 2.00
SIGN_COST = 0.15        # dollars per advertising sign
OPTIMAL_PRICE = 10      # cents; sweet spot in demand curve
BASE_DEMAND = 30        # glasses sold per day at optimal conditions
AD_DECAY = 0.5          # advertising diminishing-returns constant (C9)
AD_SCALE = 1.0          # advertising scale factor (C2)


# ---------------------------------------------------------------------------
# Core game logic
# ---------------------------------------------------------------------------

def cost_per_glass_cents(day):
    """Ingredient cost in cents. Increases on days 3 and 7."""
    if day < 3:
        return 2
    if day < 7:
        return 4
    return 5


def make_weather(day):
    """Return (weather, chance_of_rain_pct, weather_factor)."""
    r = random.random()
    if r < 0.6:
        weather = "sunny"
    elif r < 0.8:
        weather = "cloudy"
    else:
        # Hot weather doesn't occur in the first two days
        weather = "sunny" if day < 3 else "hot"

    chance_of_rain = 0
    weather_factor = 1.0

    if weather == "cloudy":
        chance_of_rain = 30 + math.floor(random.random() * 5) * 10
        weather_factor = 1.0 - chance_of_rain / 100
    elif weather == "hot":
        weather_factor = 2.0

    return weather, chance_of_rain, weather_factor


def random_events(weather, weather_factor):
    """Determine special events for the day.

    Returns (special_desc, crew_thirsty, storm_brewing, weather_factor).
    The storm_brewing flag is set but not revealed to the player until results.
    """
    special_desc = ""
    crew_thirsty = False
    storm_brewing = False

    if weather == "cloudy":
        # 25% chance of a thunderstorm that will ruin everything
        storm_brewing = random.random() < 0.25
    elif weather == "sunny":
        # 25% chance the street crew is working
        if random.random() < 0.25:
            special_desc = (
                "THE STREET DEPARTMENT IS WORKING TODAY.\n"
                "THERE WILL BE NO TRAFFIC ON YOUR STREET."
            )
            if random.random() < 0.5:
                # Crew is thirsty — they'll buy all your lemonade
                crew_thirsty = True
            else:
                # No foot traffic at all
                weather_factor = 0.1

    return special_desc, crew_thirsty, storm_brewing, weather_factor


def compute_sales(price_cents, signs, glasses_made, weather_factor, storm, crew_thirsty):
    """Return (glasses_sold, special_result_message)."""
    # Base demand from price elasticity
    if price_cents >= OPTIMAL_PRICE:
        n1 = OPTIMAL_PRICE ** 2 * BASE_DEMAND / price_cents ** 2
    else:
        n1 = (OPTIMAL_PRICE - price_cents) / OPTIMAL_PRICE * 0.8 * BASE_DEMAND + BASE_DEMAND

    # Advertising boost (diminishing returns)
    ad_benefit = 1 - math.exp(-signs * AD_DECAY) * AD_SCALE
    n2 = math.floor(weather_factor * n1 * (1 + ad_benefit))

    special = ""
    if storm:
        n2 = 0
        if glasses_made > 0:
            special = "ALL LEMONADE WAS RUINED."
    elif crew_thirsty:
        n2 = glasses_made
        special = "THE STREET CREWS BOUGHT ALL YOUR LEMONADE AT LUNCHTIME!"

    return min(n2, glasses_made), special


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def fmt_dollars(value):
    """Format a float as a dollar string, e.g. $1.25 or $-0.50."""
    if value < 0:
        return f"$-{abs(value):.2f}"
    return f"${value:.2f}"


def pause():
    input("\nPRESS ENTER TO CONTINUE...")


def show_weather_report(day, weather, chance_of_rain, special_desc):
    print()
    print(f"** LEMONSVILLE WEATHER REPORT FOR DAY {day} **")
    print()
    if weather == "storm":
        print("THUNDERSTORMS!")
        print("A SEVERE THUNDERSTORM HIT LEMONSVILLE EARLIER TODAY,")
        print("JUST AS THE LEMONADE STANDS WERE BEING SET UP.")
        print("UNFORTUNATELY, EVERYTHING WAS RUINED!!")
    elif weather == "sunny":
        print("SUNNY")
    elif weather == "cloudy":
        print("CLOUDY")
        print(f"THERE IS A {chance_of_rain}% CHANCE OF LIGHT RAIN,")
        print("AND THE WEATHER IS COOLER TODAY.")
    elif weather == "hot":
        print("HOT AND DRY")
        print("A HEAT WAVE IS PREDICTED FOR TODAY!")
    if special_desc:
        print()
        print(special_desc)


def show_results(day, player, glasses_sold, price_cents, glasses_made, signs,
                 cpg, income, expenses, profit, assets, special):
    print()
    print("$$ LEMONSVILLE DAILY FINANCIAL REPORT $$")
    print()
    print(f"   DAY {day:<5}              STAND {player}")
    print()
    if special:
        print(special)
        print()
    sold_lbl = "GLASS SOLD" if glasses_sold == 1 else "GLASSES SOLD"
    made_lbl = "GLASS MADE" if glasses_made == 1 else "GLASSES MADE"
    sign_lbl = "SIGN MADE" if signs == 1 else "SIGNS MADE"
    print(f" {glasses_sold:>4} {sold_lbl}")
    print(f" {fmt_dollars(price_cents / 100):>6} PER GLASS       INCOME {fmt_dollars(income)}")
    print()
    print(f" {glasses_made:>4} {made_lbl}")
    print(f" {signs:>4} {sign_lbl}     EXPENSES {fmt_dollars(expenses)}")
    print()
    print(f"                  PROFIT {fmt_dollars(profit)}")
    print(f"                  ASSETS {fmt_dollars(assets)}")


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------

def get_decisions(player, day, cpg, assets):
    """Prompt a player for their daily decisions. Returns (glasses, signs, price)."""
    print()
    print(f"--- DECISIONS FOR LEMONADE STAND {player} ---")
    print(f"ON DAY {day}, THE COST OF LEMONADE IS $.0{cpg}")
    if day == 3:
        print("(YOUR MOTHER QUIT GIVING YOU FREE SUGAR)")
    elif day == 7:
        print("(THE PRICE OF LEMONADE MIX JUST WENT UP)")
    print(f"\nLEMONADE STAND {player}      ASSETS {fmt_dollars(assets)}")

    while True:
        try:
            glasses = int(input(
                f"\nHOW MANY GLASSES OF LEMONADE ({cpg} CENTS EACH)\nDO YOU WISH TO MAKE? "
            ))
        except ValueError:
            print("COME ON, LET'S BE REASONABLE NOW!!! TRY AGAIN.")
            continue
        if not 0 <= glasses <= 1000:
            print("COME ON, LET'S BE REASONABLE NOW!!! TRY AGAIN.")
            continue
        if glasses * cpg / 100 > assets:
            need = fmt_dollars(glasses * cpg / 100)
            print(f"THINK AGAIN!!! YOU HAVE ONLY {fmt_dollars(assets)} IN CASH AND TO MAKE")
            print(f"{glasses} GLASSES OF LEMONADE YOU NEED {need} IN CASH.")
            continue
        break

    while True:
        try:
            signs = int(input(
                f"\nHOW MANY ADVERTISING SIGNS ({int(SIGN_COST * 100)} CENTS EACH)\nDO YOU WANT TO MAKE? "
            ))
        except ValueError:
            print("COME ON, BE REASONABLE!!! TRY AGAIN.")
            continue
        if not 0 <= signs <= 50:
            print("COME ON, BE REASONABLE!!! TRY AGAIN.")
            continue
        if glasses * cpg / 100 + signs * SIGN_COST > assets:
            remaining = assets - glasses * cpg / 100
            print(f"THINK AGAIN, YOU HAVE ONLY {fmt_dollars(remaining)}")
            print("IN CASH LEFT AFTER MAKING YOUR LEMONADE.")
            continue
        break

    while True:
        try:
            price = int(input("\nWHAT PRICE (IN CENTS) DO YOU WISH TO\nCHARGE FOR LEMONADE? "))
        except ValueError:
            print("COME ON, BE REASONABLE!!! TRY AGAIN.")
            continue
        if not 0 <= price <= 100:
            print("COME ON, BE REASONABLE!!! TRY AGAIN.")
            continue
        break

    return glasses, signs, price


# ---------------------------------------------------------------------------
# Intro screens
# ---------------------------------------------------------------------------

def intro():
    """Show welcome and instructions. Returns number of players."""
    print()
    print("HI!  WELCOME TO LEMONSVILLE, CALIFORNIA!")
    print()
    print("IN THIS SMALL TOWN, YOU ARE IN CHARGE OF")
    print("RUNNING YOUR OWN LEMONADE STAND. YOU CAN")
    print("COMPETE WITH AS MANY OTHER PEOPLE AS YOU")
    print("WISH, BUT HOW MUCH PROFIT YOU MAKE IS UP")
    print("TO YOU (THE OTHER STANDS' SALES WILL NOT")
    print("AFFECT YOUR BUSINESS IN ANY WAY). IF YOU")
    print("MAKE THE MOST MONEY, YOU'RE THE WINNER!!")
    print()

    while True:
        ans = input("ARE YOU STARTING A NEW GAME? (YES OR NO)\n==> ").strip().upper()
        if ans.startswith(("Y", "N")):
            break

    while True:
        try:
            n = int(input("HOW MANY PEOPLE WILL BE PLAYING? (1-30) ==> "))
            if 1 <= n <= 30:
                break
        except ValueError:
            pass

    print()
    print("TO MANAGE YOUR LEMONADE STAND, YOU WILL")
    print("NEED TO MAKE THESE DECISIONS EVERY DAY:")
    print()
    print("1. HOW MANY GLASSES OF LEMONADE TO MAKE")
    print("   (ONLY ONE BATCH IS MADE EACH MORNING)")
    print("2. HOW MANY ADVERTISING SIGNS TO MAKE")
    print("   (THE SIGNS COST FIFTEEN CENTS EACH)")
    print("3. WHAT PRICE TO CHARGE FOR EACH GLASS")
    print()
    print("YOU WILL BEGIN WITH $2.00 CASH (ASSETS).")
    print("BECAUSE YOUR MOTHER GAVE YOU SOME SUGAR,")
    print("YOUR COST TO MAKE LEMONADE IS TWO CENTS")
    print("A GLASS (THIS MAY CHANGE IN THE FUTURE).")
    pause()

    print()
    print("YOUR EXPENSES ARE THE SUM OF THE COST OF")
    print("THE LEMONADE AND THE COST OF THE SIGNS.")
    print()
    print("YOUR PROFITS ARE THE DIFFERENCE BETWEEN")
    print("THE INCOME FROM SALES AND YOUR EXPENSES.")
    print()
    print("THE NUMBER OF GLASSES YOU SELL EACH DAY")
    print("DEPENDS ON THE PRICE YOU CHARGE, AND ON")
    print("THE NUMBER OF ADVERTISING SIGNS YOU USE.")
    print()
    print("KEEP TRACK OF YOUR ASSETS, BECAUSE YOU")
    print("CAN'T SPEND MORE MONEY THAN YOU HAVE!")
    pause()

    return n


# ---------------------------------------------------------------------------
# Main game loop
# ---------------------------------------------------------------------------

def play():
    num_players = intro()
    assets = [STARTING_ASSETS] * num_players
    bankrupt = [False] * num_players
    day = 0

    while True:
        day += 1
        cpg = cost_per_glass_cents(day)
        weather, chance_of_rain, weather_factor = make_weather(day)
        special_desc, crew_thirsty, storm_brewing, weather_factor = \
            random_events(weather, weather_factor)

        # Show today's weather (storm is hidden until results)
        show_weather_report(day, weather, chance_of_rain, special_desc)
        pause()

        # Collect decisions from all active players
        decisions = []
        for i in range(num_players):
            if bankrupt[i]:
                print(f"\nSTAND {i + 1}: YOU ARE BANKRUPT.")
                print("NO DECISIONS FOR YOU TO MAKE.")
                decisions.append((0, 0, 0))
            else:
                decisions.append(get_decisions(i + 1, day, cpg, assets[i]))

        # Reveal the storm now (if it happened) before showing results
        if storm_brewing:
            show_weather_report(day, "storm", 0, "")
            pause()

        # Calculate and display results for each active player
        for i in range(num_players):
            if bankrupt[i]:
                continue

            glasses, signs, price = decisions[i]
            sold, special = compute_sales(
                price, signs, glasses, weather_factor, storm_brewing, crew_thirsty
            )
            expenses = glasses * cpg / 100 + signs * SIGN_COST
            income = sold * price / 100
            profit = income - expenses
            assets[i] += profit

            show_results(day, i + 1, sold, price, glasses, signs,
                         cpg, income, expenses, profit, assets[i], special)

            if assets[i] < cpg / 100:
                print(f"\nSTAND {i + 1}")
                print("...YOU DON'T HAVE ENOUGH MONEY LEFT")
                print("TO STAY IN BUSINESS. YOU'RE BANKRUPT!")
                bankrupt[i] = True

            pause()

        if all(bankrupt):
            break

    # Final standings for multi-player games
    if num_players > 1:
        print()
        print("--- FINAL STANDINGS ---")
        for i, a in enumerate(assets):
            print(f"  STAND {i + 1}: {fmt_dollars(max(a, 0.0))}")
        winner = max(range(num_players), key=lambda i: assets[i])
        print(f"\nSTAND {winner + 1} WINS!")

    print()
    ans = input("WOULD YOU LIKE TO PLAY AGAIN? (Y/N) ==> ").strip().upper()
    if ans.startswith("Y"):
        play()


if __name__ == "__main__":
    play()
