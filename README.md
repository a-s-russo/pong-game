# Pong
A recreation of the classic Pong game in Python using the [Turtle package](https://docs.python.org/3/library/turtle.html).

Inspired by the project for day 22 of the course: [100 Days of Python](https://100daysofpython.dev/).

## Playing

The left player uses:
- `W` to move the paddle up
- `S` to move the paddle down

The right player uses:
- `🠉` to move the paddle up
- `🠋` to move the paddle down

The first player to reach 5 points wins.

The ball increases in speed each time it is hit by a paddle. The speed resets to the starting speed after each point is scored.

## Installing

1. Ensure [Python](https://www.python.org/) is installed on your computer.
2. Download the Python scripts from this repository (that is, the five `*.py` files) into the same folder.
3. Run `main.py`.

The game is based on the `turtle` package that is a pre-installed Python library. For possible issues with `turtle`, consult the [tutorial](https://docs.python.org/3/library/turtle.html).

## Modifying

Various parameters can be changed in the `parameters.py` script. Note however that some parameter values or combinations of values may make the game not function correctly or as intended. 

![alt text](game-screen-shot.png)