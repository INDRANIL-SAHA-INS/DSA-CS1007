from collections import deque
class Graph:
    def __init__(self):
        self.adj_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edge(self,u,v,directed=False):
        self.add_vertex(u)
        self.add_vertex(u)
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].appen(u)


    def bfs_path(self,start):
        visited=set()
        q=deque([start])
        path=[]
        while q:
            current=q.popleft()
            if current not in visited:
                visited.add(current)
                path.append(current)

                for neighbors in self.adj_list[current]:
                    if neighbors not in visited:
                        q.append(neighbors)
        return path

g=Graph()
g.add_edge(2,3)
g.add_edge(6,3)
g.add_edge(9,1)
g.add_edge(2,5)
g.add_edge(3,7)
g.add_edge(7,8)
path=g.bfs(2)
print("BFS Path:",path)
