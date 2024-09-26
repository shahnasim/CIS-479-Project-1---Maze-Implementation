import numpy as np
import random

# Function to generate a random maze of size 10x10 with a specified density of obstacles


def generate_random_maze(size=10, density=0.2):
    # Initialize the maze with all open cells
    maze = np.full((size, size), '.')

    # Calculate the number of obstacles based on density
    num_obstacles = int(size * size * density)

    # Randomly place obstacles in the maze
    obstacles = set()
    while len(obstacles) < num_obstacles:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) not in obstacles:
            maze[x, y] = 'X'
            obstacles.add((x, y))

    # Randomly place the start and goal points in the maze
    while True:
        start_x, start_y = random.randint(
            0, size - 1), random.randint(0, size - 1)
        if maze[start_x, start_y] == '.':
            maze[start_x, start_y] = 'S'
            break

    while True:
        goal_x, goal_y = random.randint(
            0, size - 1), random.randint(0, size - 1)
        if maze[goal_x, goal_y] == '.' and (goal_x, goal_y) != (start_x, start_y):
            maze[goal_x, goal_y] = 'G'
            break

    return maze


# Generate a random maze and print it out
maze = generate_random_maze()
for row in maze:
    print(' '.join(row))
