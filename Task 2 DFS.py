import time
maze = [
    ". . . . . . . . . .",
    ". . . . . . . . X .",
    ". X . . . . . . . .",
    "X . . . . X . . . .",
    ". . . . . . S . . .",
    ". . X . . . X . . X",
    "X . X . . . X . . .",
    ". X . . X . X . . .",
    ". . . X G . . . . .",
    ". X . X X X X X . .",
]

maze = [
    ". X . . . . . . . .",
    ". . . X . . . . . .",
    ". . . . X . X . X .",
    ". . . . . . . . . .",
    "X . . . . X . . . .",
    ". . . X . . S . . X",
    ". . X X . . . . . .",
    ". . X X . X X X . .",
    ". . . . X . . X . .",
    "X . . . . X . . . G",
]

maze = [
    ". . . . . X . . X .",
    ". . . . . . . . . .",
    ". . . . . . . . . .",
    "G X . . X . . . . .",
    ". . X . . . . X X .",
    ". . . . . . . . X .",
    ". X X . . . X . . .",
    "X X . . X X . . . .",
    ". X . . . . . . . .",
    "S X X . . . X . . X",

]

maze = [
    ". . . . . X . . . .",
    "X . . . . . . . . .",
    ". . X . G . . . . .",
    ". . . . X X . . X X",
    ". X . . . . . . . .",
    ". X . . . . . . . .",
    ". X . . X . . X . .",
    ". . . . . X . . X .",
    ". . X . . X X . X S",
    ". X . . . . . . X .",
]

maze = [
    ". . . X . . X . . .",
    ". . . . . . X . . .",
    ". . X S . X . . . .",
    ". . . . X . . . . .",
    "X . X . . X . X . .",
    "X . . . X . . X X .",
    "X . . . . . . . X .",
    ". . X . . . . . X .",
    ". . . G . . . X . .",
    ". . . . . . . . X .",
]

maze = [
    ". . . . . . . . . .",
    "X . . . X X . X . .",
    ". S . . . . . . . X",
    ". X . . . . . . X .",
    ". . . . G X . . . .",
    ". X . . . . . . X .",
    ". . . X . X . . . .",
    ". . . . . . . X X X",
    ". . X . . . . . X .",
    ". X . . . . . . X X",
]

maze = [
    ". . X X . X . . X .",
    ". . . . . . X . . .",
    "S . X X . . X . . X",
    ". . . . . . . . X .",
    ". . X X . . . X . .",
    "X . . . . . . . . .",
    "X . . . . . . . . .",
    "X X . X . . . . . .",
    ". . . . . . . . . .",
    "X . . X . . . . . G",
]

maze = [
    ". . . . . X . X . .",
    ". . X . X . . . . .",
    ". . X . . . . . . .",
    ". . X . . X . . X .",
    ". . . X . X . . . .",
    ". . . . . . . X . .",
    ". . . . . . . . . .",
    ". . . X X . . X X .",
    ". X . X . . . . . .",
    "X X S . . X . G . .",

]

maze = [
    ". . . X . . X X . .",
    ". X X . . X . . . .",
    ". . . . . . X . . .",
    ". S . X . X . X X .",
    "X . . X . X . . . .",
    ". . . . X . . . . .",
    ". . . . X . . . . G",
    ". . . . . X . X . .",
    ". . . . . . . . . .",
    ". . . . X . . . X .",
]

maze = [
    "X X . . . . . . G .",
    ". . X . . X . . X X",
    ". . X S . . X . . .",
    ". . . . . . X . . .",
    ". . . X X . . . . .",
    ". . . X . . . . . .",
    ". . . . X . . . . .",
    "X . X . . . . . X .",
    ". X . . . . . . . .",
    ". . . . . . X X X .",
]


def dfs(maze, start, goal):
    # Stack for DFS; holds tuples of (position, path)
    stack = [(start, [start])]
    visited = set()  # Set of visited positions

    while stack:
        (x, y), path = stack.pop()  # Current position and path
        if (x, y) not in visited:
            visited.add((x, y))  # Mark the current cell as visited

            # Goal check
            if maze[x][y] == 'G':
                return path

            # Add neighbors to the stack
            # Possible movements: up, down, left, right
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] != 'X':
                    if (next_x, next_y) not in visited:
                        stack.append(
                            ((next_x, next_y), path + [(next_x, next_y)]))

    return None  # No path found

# Function to visualize the path in the maze


def visualize_path(maze, path):
    maze_copy = [list(row) for row in maze]  # Create a copy of the maze
    for x, y in path:
        if maze_copy[x][y] == '.':  # Only change the '.' cells to avoid overwriting S and G
            maze_copy[x][y] = '*'
    return maze_copy


# Get the starting and goal positions from the maze
start = None
goal = None
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

# Run DFS to find the path
path = dfs(maze, start, goal)

# Record the start time using perf_counter
start_time = time.perf_counter()

# Record the end time using perf_counter
end_time = time.perf_counter()

# Visualize the path in the maze, if a path is found
if path:
    maze_with_path = visualize_path(maze, path)
    for row in maze_with_path:
        print(' '.join(row))
else:
    print("No path found using DFS.")

# Calculate and print the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
