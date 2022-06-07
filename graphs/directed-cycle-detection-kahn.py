def detectCycleInDirectedGraph(n, edges):
    # Write your code here
    graph = {x : [] for x in range(n)}
    freq = [0 for x in range(n)]
    for i in range(len(edges)):
        graph[edges[i][0]-1].append(edges[i][1]-1)
        freq[edges[i][1]-1] += 1
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
    for f in freq:
        if f>0:
            return 1
    return 0