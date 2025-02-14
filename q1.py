from collections import deque

def find_shortest_path(matrix):
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    start=(1,1)
    end=(4,4)

    rows,cols = len(matrix), len(matrix[0])
    if not(0<=start[0]< rows and 0<= start[1]< cols and 0 <=end[0]< rows and 0 <=end[1] < cols):
        return "invalid start or end position"
    queue = deque([(start , [start])])
    visited = set()
    while queue:
        (rows,cols) , path = deque.popleft()
        if (rows,cols) == end:
            return path
        visited.add((rows,cols))
        for dr,dc in directions:
            new_row, new_col= rows+dr,cols+dc
            if (0<=new_row< rows and 0<= new_col< cols and (new_row,new_col) not in visited and matrix[new_row][new_col]!=1):
                queue.append(((new_row,new_col), path + [(new_row,new_col)]))

    return "No path found"
matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

shortest_path = find_shortest_path(matrix)
print(shortest_path)

matrix_with_obstacle = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
shortest_path = find_shortest_path(matrix_with_obstacle)
print(shortest_path)