def bellmonFord(n, m, src, dest, edges):
    # Write your code here.
    dist = [1000000000] * (n+1)
    dist[src] = 0
    for i in range(1, n):
        for u, v, wt in edges:
            if dist[u] == 1000000000 and dist[v] == 1000000000:
                continue
            if dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
    return dist[dest]