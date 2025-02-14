from collections import deque


# Function Skeleton for BFS:
def find_shortest_path(matrix, startPos, endPos):
    # Directions: Left, Right, Up, Down
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Initialize starting and ending positions
    start = (0, 0)
    end = (len(matrix[0]) - 1, len(matrix) - 1)
    # Initialize data structures for BFS
    queue = deque() # Use deque for BFS
    visited = set() # Track visited positions

    queue.append((startPos, [])) # Append starting position and path
    # BFS Loop
    while queue:
        # Dequeue the next position
        current, path = queue.popleft()

        if current == endPos:
            return path + [current]

        if current in visited:
            continue

        for direction in directions:
            nextPos = (current[0] + direction[0], current[1] + direction[1])
            if nextPos[0] < start[0] or nextPos[0] > end[0] or nextPos[1] < start[1] or nextPos[1] > end[1]:
                continue

            if nextPos in visited:
                continue

            # obstacles
            if matrix[nextPos[0]][nextPos[1]] == 1:
                continue

            queue.append((nextPos, path + [current]))

    return None

matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

startPos = (1, 1)
endPos = (4, 4)

path = find_shortest_path(matrix, startPos, endPos)
print(path)

