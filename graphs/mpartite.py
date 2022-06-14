def graphColoring(mat,m):
    #Your code goes here
    n = len(mat)
    colors = [-1 for x in range(n)]
    c = 0
    for i in range(n):
        if colors[i] is -1:
            if (not dfs(mat, i, -1, colors, c, m)): return "NO"
    return "YES"

def dfs(graph, node, parent, colors, c, m):
    colors[node] = c
    for idx, child in enumerate(graph[node]):
        if child:
            if colors[idx] is -1:
                colors[idx] = True
                ret = dfs(graph, idx, node, colors, (c + 1) %m , m)
                if c == colors[idx] or not ret:
                    return False
            elif idx != parent:
                if colors[idx] == c:
                    colors[idx] = (c + 1) % m
                    return False
    return True