from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        """Initializes the graph with an adjacency list."""
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
       
        return self.adjacency_list[v]
    
    def h(self, n):
      
        H = {
            'The': 4,
            'cat': 3,
            'dog': 3,
            'runs': 2,
            'fast': 1,  
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node): 
        """Implements the A* search algorithm to find the optimal path.""" 
        open_list = set([start_node])
        closed_list = set([])

        g = {} # Cost from start node to all other nodes 
        g[start_node] = 0 
        parents = {} # Keeps track of paths parents[start_node] = start_node 
        while len(open_list)>0:
            n = None # Current node 
            # Find the node with the lowest f(n) = g(n) + h(n) 
            for node in open_list:
                    if n is None:
                        n = node
                    else:
                        if (g[node] + self.h(node)) < (g[n] + self.h(n)):
                            n = node
            
            if n == None: 
                print("Path does not exist!") 
                return None
            # If the goal is reached, reconstruct the path.
            if n == stop_node:
                    reconst_path = []
                    while n!=start_node:
                        reconst_path.append(n)
                        n = parents[n]
                    reconst_path.append(start_node)
                    reconst_path.reverse()
                    return reconst_path, g[stop_node]
            for neighbour,weight in self.get_neighbors(n):
                if neighbour not in closed_list and neighbour not in open_list:
                    open_list.add(neighbour)
                    g[neighbour]=g[n]+weight  #cost=cost+weight
                    parents[neighbour]=n
                else:
                    if g[n] +weight< g[neighbour]:  #better path with less cost is found, we reopen the case
                        g[neighbour]=g[n]+weight
                        parents[neighbour] = n
                        if neighbour in closed_list:
                                closed_list.remove(neighbour)
                                open_list.add(neighbour)
                    
            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None
                

if __name__ == "__main__":
   
    adjacency_list = {
        'The': [('cat', 2), ('dog', 3)],
        'cat': [('runs', 1)],
        'dog': [('runs', 2)],
        'runs': [('fast', 2)],
        'fast': []  
    }

    
    graph = Graph(adjacency_list)

   
    start_node = 'The'
    stop_node = 'fast'
    path, total_path_cost = graph.a_star_algorithm(start_node, stop_node)
    
    if path:
        print("Path found:\n", path)
        print("THe total path cost is: ", total_path_cost)
    else:
        print("No path found!")
