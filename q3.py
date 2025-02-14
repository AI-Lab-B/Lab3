from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        """Initializes the graph with an adjacency list."""
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        """Returns the neighbors of a given node."""
        return self.adjacency_list[v]

    def h(self, n):
        """Heuristic function: estimates the cost from node n to the goal."""
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 0
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        """Implements the A* search algorithm to find the optimal path."""
        open_list = set([start_node])
        closed_list = set([])

        g = {}  # Cost from start node to all other nodes
        g[start_node] = 0

        parents = {}  # Keeps track of paths
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None  # Current node

            # Find the node with the lowest f(n) = g(n) + h(n)
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print("Path does not exist!")
                return None

            # If goal node is found, reconstruct and return the path
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print("Path found: {}".format(reconst_path))
                return reconst_path

            # Explore all neighbors of the current node
            for (m, weight) in self.get_neighbors(n):
                # If the current node isn't in both open and closed list, add it to the open list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # Otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed list, move it to open list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # Remove n from the open list, and add it to the closed list because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None

# Define the graph given in adjacency list
adjacency_list = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 3), ('E', 1)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 3)],
    'E': [('B', 1), ('F', 3)],
    'F': [('C', 5), ('E', 3), ('G', 2)],
    'G': [('F', 2)]
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'G')  # Define start and goal words
