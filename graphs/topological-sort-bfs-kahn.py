def topologicalSort(adj, v, e):
    # Write your code here
    graph = {x : [] for x in range(v)}
    freq = [0 for x in range(v)]
    for i in range(e):
        graph[adj[i][0]].append(adj[i][1])
        freq[adj[i][1]] += 1
    q = []
    for idx, f in enumerate(freq):
        if f == 0: 
            q.append(idx)
    sort = []
    while len(q) > 0:
        node = q.pop(0)
        children = graph[node]
        for child in children:
            freq[child] -= 1
            if freq[child] == 0:
                q.append(child)
        sort.append(node)
    return sort