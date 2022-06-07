def topologicalSort(adj, v, e):
    # Write your code here
    graph = {x : [] for x in range(v)}
    for i in range(e):
        graph[adj[i][0]].append(adj[i][1])
    visited = []
    stack = []
    for i in range(v):
        if i in visited: continue
        visited.append(i)
        dfs(graph, i, visited, stack)
    stack.reverse()
    return stack

def dfs(graph, start, visited, stack):
    children = graph[start]
    for child in children:
        if child not in visited:
            visited.append(child)
            dfs(graph, child, visited, stack)
    stack.append(start)