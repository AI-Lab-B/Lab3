task 1

from collections import deque

def Finding_Shortest_Path(Matrix):

    Direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    Start = (1, 1)
    End = (4, 4)
    
    row, col = len(Matrix), len(Matrix[0])
    
    queue = deque([(Start, [Start])])
    visit = set()
    visit.add(Start)
    

    while queue:
        (x, y), path = queue.popleft()
    
        if (x, y) == End:
            return path
        
    
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and Matrix[nx][ny] != 1 and (nx, ny) not in visit:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visit.add((nx, ny))
    

    return none

Matrix = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

path = Finding_Shortest_Path(Matrix)
if path:
    print("Shortest Path:", path)
else:
    print("No path found")


task 2


import time
from collections import deque

def state_to_tuple(state):
    return tuple(state)

def tuple_to_state(matrix):
    return ''.join(matrix)

def get_moves(state):
    
    moves = []
    state = list(state)
    zero_index = state.index('0')
    row, col = divmod(zero_index, 3)
    directions = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    
    for move, (dr, dc) in directions.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            moves.append((''.join(new_state), move))
    
    return moves

def dfs(start_state, goal_state):

    stack = [(start_state, [])]
    visited = set()
    
    while stack:
        state, path = stack.pop()
        
        if state in visited:
            continue
        
        visited.add(state)
        
        if state == goal_state:
            return path
        
        for new_state, move in get_moves(state):
            stack.append((new_state, path + [move]))
    
    return None

def main():

    start_state = input("Enter start State: ")
    goal_state = input("Enter goal State: ")
    
    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)
    
    print("----------------")
    print("DFS Algorithm")
    print("----------------")
    
    start_time = time.time()
    solution_path = dfs(start_tuple, goal_tuple)
    end_time = time.time()
    
    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path))
        print("No of Nodes Visited:", len(solution_path) + 1)
        
        state = list(start_state)
        for move in solution_path:
            print('------')
            for row in range(3):
                print(' '.join(state[row * 3:(row + 1) * 3]))
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()


task 3


from queue import PriorityQueue

class Graph:
    def __init__(self, adjacency_list, heuristics):
    
        self.adjacency_list = adjacency_list
        self.heuristics = heuristics

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def h(self, node):

        return self.heuristics.get(node, float('inf'))

    def a_star_algorithm(self, start_node, stop_node):

        open_list = PriorityQueue()
        open_list.put((self.h(start_node), start_node))
        g = {start_node: 0} # Cost from start node to all other nodes
        parents = {start_node: None}

        while not open_list.empty():
            _, current_node = open_list.get()
            
            if current_node == stop_node:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = parents[current_node]
                path.reverse()
                return path, g[stop_node]
            
            for neighbor, cost in self.get_neighbors(current_node):
                temp_g = g[current_node] + cost
                
                if neighbor not in g or temp_g < g[neighbor]:
                    g[neighbor] = temp_g
                    f = temp_g + self.h(neighbor)
                    open_list.put((f, neighbor))
                    parents[neighbor] = current_node
        
        return None, float('inf')

# Define the adjacency list (edges and costs)
adjacency_list = {
    "The": [("Cat", 2), ("Dog", 3)],
    "Cat": [("runs", 1)],
    "Dog": [("runs", 2)],
    "runs": [("fast", 2)],
    "fast": []
}

# Define the heuristic values (h(n))
heuristics = {
    "The": 4,
    "Cat": 3,
    "Dog": 3,
    "runs": 2,
    "fast": 1
}

# Create the graph
graph = Graph(adjacency_list, heuristics)

# Run A* algorithm from "The" to "fast"
path, total_cost = graph.a_star_algorithm("The", "fast")

# Print results
if path:
    print("Sentence:", " ".join(path))
    print("Total cost:", total_cost)
else:
    print("No path found!")
if __name__ == "__main__":
    main()