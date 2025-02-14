from collections import deque

def find_shortest_path(matrix):
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize starting and ending positions (adjusted for 0-based index)
    start = (1, 1)
    end = (4, 4)
    rows, cols = len(matrix), len(matrix[0])
    
    # Check if start or end is an obstacle
    if matrix[start[0]][start[1]] == 1 or matrix[end[0]][end[1]] == 1:
        return "No path available"
    
    # Initialize data structures for BFS
    queue = deque([(start, [start])])  # (current_position, path)
    visited = set()
    visited.add(start)
    
    # BFS Loop
    while queue:
        (x, y), path = queue.popleft()
        
        # Check if HOME is reached
        if (x, y) == end:
            return path
        
        # Explore neighboring cells
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited and matrix[new_x][new_y] == 0:
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))
                visited.add((new_x, new_y))
    
    return "No path available"

matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

path = find_shortest_path(matrix)
print(path)