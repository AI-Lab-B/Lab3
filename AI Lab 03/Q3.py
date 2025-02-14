from collections import deque

class Graph:
    def _init_(self, adjacency_list):
        """Initializes the graph with an adjacency list."""
        self.adjacency_list = adjacency_list
    
    def get_neighbors(self, v):
        """Returns the neighbors of a given node."""
        return self.adjacency_list.get(v, [])
    
    def h(self, n):
        """Heuristic function: estimates the cost from node n to the goal."""
        H = {
            "The": 4,
            "Cat": 3,
            "Dog": 3,
            "runs": 2,
            "fast": 1
        }
        return H[n]
    
    def a_star_algorithm(self, start_node, stop_node):
        """Implements the A* search algorithm to find the optimal path."""
        open_list = set([start_node])
        closed_list = set([])
        
        g = {start_node: 0}  # Cost from start node to all other nodes
        parents = {start_node: start_node}  # Keeps track of paths

        while len(open_list) > 0:
            n = None
            # Find a node with the lowest cost
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            
            if n == None:
                print("Path does not exist!")
                return None, float('inf')
            
            # Check if the goal has been reached
            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                path.reverse()
                return path, g[stop_node]
            
            # Check neighbors of the current node
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            
            open_list.remove(n)
            closed_list.add(n)
        
        
        
        return None, float('inf')

# Define the graph given in adjacency list
adjacency_list = {
    "The": [("Cat", 2), ("Dog", 3)],
    "Cat": [("runs", 1)],
    "Dog": [("runs", 2)],
    "runs": [("fast", 2)],
    "fast": []
}

graph1 = Graph(adjacency_list)
path, cost = graph1.a_star_algorithm("The", "fast")
if path:
    print("Sentence:", " ".join(path))
    print("Total cost:", cost)
else:
    print("Path does not exist!")