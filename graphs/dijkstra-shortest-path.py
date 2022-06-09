import numpy as np
def dijkstra(vec, vertices, edges, source):
    # Write your code here.
    dist = [2147483647] * vertices
    dist[source] = 0
    adj = {x : [] for x in range(vertices)}
    weights = {x: [] for x in range(vertices)}
    for v in vec:
        adj[v[0]].append(v[1])
        adj[v[1]].append(v[0])
        weights[v[0]].append(v[2])
        weights[v[1]].append(v[2])        
    q = [source]
    while q:
        node = q.pop(0)
        for idx, child in enumerate(adj[node]):
            if dist[child] > dist[node] + weights[node][idx]:
                dist[child] = dist[node] + weights[node][idx]
                q.append(child)
    return dist