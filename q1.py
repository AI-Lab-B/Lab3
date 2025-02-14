from collections import deque

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_shortest_path(matrix):
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Initialize starting and ending positions
    start = Node(0, 0)
    end = Node(3, 3)
    # Initialize data structures for BFS
    queue = deque() # Use deque for BFS
    queue.append(start)
    visited = set() # Track visited positions
    # BFS Loop
    while queue:
        n = queue.popleft()
        if (n.x, n.y) not in visited:
            if n.x == end.x and n.y == end.y:
                return "Done"
            visited.add((n.x, n.y))
            for direction in directions:
                new_x, new_y = n.x + direction[0], n.y + direction[1]
                if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                    queue.append(Node(new_x, new_y))
    return "No path found"

if __name__ == "__main__":
    outerList = []
    for i in range(6):
        innerList = []
        for j in range(6):
            n = Node(i, j)
            innerList.append(n)
        outerList.append(innerList)
            
    print(find_shortest_path(outerList))
