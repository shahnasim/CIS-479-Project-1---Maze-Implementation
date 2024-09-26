import time
import matplotlib.pyplot as plt

# Define maze, start, and goal
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

# Function to perform Depth-First Search with interactive visualization


def dfs(maze, start, goal):
    # Initialize the DFS stack with starting position and path
    stack = [(start, [start])]
    visited = set()  # Set of visited positions

    plt.ion()  # Turn on interactive mode for Matplotlib
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    maze_visualization = [
        [0 for _ in range(len(maze[0]))] for _ in range(len(maze))
    ]

    while stack:
        (x, y), path = stack.pop()  # Current position and path

        if (x, y) == goal:
            # Highlight the final path
            for x, y in path:
                maze_visualization[x][y] = 2  # Mark path cells as 2
            plt.imshow(maze_visualization, cmap='viridis')
            plt.pause(1)  # Pause for a moment to see the final state
            break

        if (x, y) not in visited:
            visited.add((x, y))  # Mark the current cell as visited

            # Highlight the explored cell
            maze_visualization[x][y] = 1  # Mark visited cells as 1
            plt.imshow(maze_visualization, cmap='viridis')
            plt.pause(0.1)

            # Add neighbors to the DFS stack in reverse order (right, left, down, up)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + dx, y + dy
                if (
                    0 <= next_x < len(maze)
                    and 0 <= next_y < len(maze[0])
                    and maze[next_x][next_y] != 'X'
                    and (next_x, next_y) not in visited
                ):
                    stack.append(((next_x, next_y), path + [(next_x, next_y)]))

    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show the final visualization


# Get the starting and goal positions from the maze
start = None
goal = None
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

# Run DFS to find the path with visualization
dfs(maze, start, goal)
