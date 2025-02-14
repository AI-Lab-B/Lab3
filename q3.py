from collections import deque

class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list
    def get_neighbours(self,v):
        return self.adj_list[v]
    def h(self,n):
        H={
             'The': 4,
            'cat': 3,
            'dog': 3,
            'runs': 2,
            'fast': 1 
        }
        return H(n,0)
    def a_star_search(self, start, goal):
        open_list = set([start])
        closed_list = set([])
        g = {}
        g[start]=0
        parent ={}
        parent[start]=start
        while len(open_list)>0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v)<g[n]+self.h(n):
                    n=v
            if n== None:
                print("Goal is Not reachable")
                break
            if n == goal:
                retrace = []
                while parent[n] != n:
                    retrace.append(n)
                    n = parent[n]
                retrace.append(start)
                retrace.reverse()
                print("Sentence:", " ".join(retrace))
                print("Total cost:", g[goal])  
                return retrace
            for (m, weight) in self.get_neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parent[m] = n
                    g[m] = g[n] + weight
                elif g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parent[m] = n
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None
    



adjacency_list = {
    'The': [('cat', 2), ('dog', 3)],
    'cat': [('runs', 3)],
    'dog': [('runs', 4)],
    'runs': [('fast', 1)],
    'fast': []
}
graph = Graph(adjacency_list)
graph.a_star_search('The', 'fast')