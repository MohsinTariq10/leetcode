import numpy as np
class DisjointSet:
    def __init__(self, n):
        self.value = [i for i in range(n+1)]
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    
    def find_parent(self, c):
        inp = c
        while(self.parent[c] != self.value[c]):
            c = self.parent[c]
        ultimatep = c
        c = inp
        while(self.parent[c] != self.value[c]):
            old_parent = self.parent[c]
            self.parent[c] = ultimatep
            c = old_parent
        return ultimatep
    
    def union(self, a, b):
        pa = self.find_parent(a)
        pb = self.find_parent(b)
        rpa = self.rank[pa]
        rpb = self.rank[pb]
        if rpa > rpb:
            self.parent[pb] = pa
        elif rpa < rpb:
            self.parent[pa] = pb
        else:
            self.parent[pa] = pb
            self.rank[pb] += 1

def kruskalMST(n, m, graph):
    # Write your code here.
    if len(graph) == 0:
        return 0
    graph = np.array(graph)
    sorted_graph = graph[graph[:,2].argsort()]
    graph = sorted_graph.tolist()
    mst = 0
    d = DisjointSet(n)
    for src, dst, wt in graph:
        if d.find_parent(src) != d.find_parent(dst):
            d.union(src, dst)
            mst+=wt
    return mst
    