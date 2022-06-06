import numpy as np
from scipy import sparse
def BFS(vertex, edges):
    # Write your solution here
    # 'vertex' is the number of vertices present in the graph
    # 'edges' is a matrix of the set of edges between two given vertices in the graph
    graph = {x : [] for x in range(vertex)}
    temp = edges[0]
    edges[0] += edges[1]
    edges[1] += temp
    
    sum = []
    for i in range(len(edges[0])):
        sum.append(edges[0][i] + edges[1][i])
    sum = np.array(sum)
    indices = np.argsort(sum)
    for i in indices:
        graph[edges[0][i]].append(edges[1][i])
    q = []
    visited = []
    endresult = []
    for i in range(vertex):
        if i in visited: continue
        q.append(i)
        visited.append(i)
        while len(q) >0:
            node = q.pop(0)
            endresult.append(node)
            for child in graph[node]:
                if child not in visited:
                    q.append(child)
                    visited.append(child)
    return endresult
            