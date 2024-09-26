import heapq
import time
import matplotlib.pyplot as plt

# Define maze, start, and goal
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
# Function to calculate the Manhattan distance between two points


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Function to perform A* search with interactive visualization


def astar(maze, start, goal):
    # Priority queue for A*; holds tuples of (f-score, g-score, position, path)
    priority_queue = [(0, 0, start, [start])]
    visited = set()  # Set of visited positions

    plt.ion()  # Turn on interactive mode for Matplotlib
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    maze_visualization = [
        [0 for _ in range(len(maze[0]))] for _ in range(len(maze))]

    while priority_queue:
        _, g, (x, y), path = heapq.heappop(
            priority_queue)  # Current position and path

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

            # Add neighbors to the priority queue
            # Possible movements: up, down, left, right
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] != 'X':
                    if (next_x, next_y) not in visited:
                        # Calculate f-score (f = g + h)
                        h = manhattan_distance((next_x, next_y), goal)
                        g_next = g + 1
                        f = g_next + h
                        heapq.heappush(
                            priority_queue, (f, g_next, (next_x, next_y), path + [(next_x, next_y)]))

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

# Run A* search to find the path with visualization
astar(maze, start, goal)
