# Lemonade Stand

A faithful Python recreation of the 1979 Apple II classic *Lemonade Stand*.

Original by Bob Jamison (MECC). Modified for Apple II by Charlie Kellner, 1979.
The original source code is available at [codenautics.com/lemonade](http://codenautics.com/lemonade/).

## How to play

```
python lemonade.py
```

Requires Python 3.8+. No third-party dependencies.

## Game mechanics

Each day you run your lemonade stand by deciding:

1. **How many glasses to make** — each glass costs 2¢ (rising to 4¢ on day 3, then 5¢ on day 7)
2. **How many advertising signs to make** — 15¢ each; more signs boost sales with diminishing returns
3. **What price to charge** — the sweet spot is around 10¢; too high or too low hurts demand

Weather affects sales:
- **Sunny** — normal demand
- **Hot & dry** — 2× demand
- **Cloudy** — reduced demand; chance of a thunderstorm that ruins everything
- **Thunderstorm** — all lemonade ruined (revealed after you've committed your resources)

Random events: the street department occasionally works on your street, either blocking all traffic or sending a thirsty crew that buys every glass you have.

The game ends when you go bankrupt. Supports up to 30 players taking turns at the same terminal.

## Authors

* **Nate Veldkamp**

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
