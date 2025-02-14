from collections import deque



def find_shortest_path(matrix):

    # Define allowed movement directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    
    start = (0, 0)
    goal = (3,3)
    
    # Initialize BFS data structures
    frontier= deque([start])
    visited = {start}
    parent = {start: None}  # Used to reconstruct the path later
    
    # BFS loop
    while frontier:
        node = frontier.popleft()
        
        
        if node== goal:
            # Reconstruct the path from end to start using parent dictionary
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1] 
        
        # Explore neighbors in allowed directions
        for d in directions:
            x, y = node[0] + d[0], node[1] + d[1]
            neighbor = (x, y)
            
            if (neighbor not in visited):
                
                frontier.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = node 
    
    
    return None

# Example usage:
if __name__ == "__main__":
    
    grid = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    
    result = find_shortest_path(grid)
    if result:
        
        for pos in result:
            
            print(f"({pos[0]+1}, {pos[1]+1})\n")
        
    else:
        print("No path found.")
