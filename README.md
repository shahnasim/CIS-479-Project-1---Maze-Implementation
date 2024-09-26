# Maze Maker

## What It Does
This script makes a maze. It uses `numpy` for creating a grid and `random` to put walls and paths. The maze has a start (S), end (G), open paths (.), and walls (X).

## You Need
- Python 3
- Numpy

Get Numpy like this:
```
pip install numpy
```

## How to Use
1. Open the script.
2. Run this part:

```python
maze = generate_random_maze(size=10, density=0.2)
for row in maze:
    print(' '.join(row))
```

You can change `size` to make the maze bigger or smaller and `density` to have more or fewer walls.

## About the Maze Function
- **generate_random_maze(size=10, density=0.2):**
  - `size`: How big the maze is. Default is 10x10.
  - `density`: How many walls you want. Default is 20% walls.

First, it makes a big empty space. Then, it randomly puts walls until it's as full as you want. It makes sure there's a start and an end that are not blocked or the same spot.

## What You Get
A maze printed out as a grid. Paths, walls, a start, and an end are shown with different symbols.
