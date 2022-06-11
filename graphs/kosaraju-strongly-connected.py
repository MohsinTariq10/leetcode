def stronglyConnectedComponents(n, edges):
    # Write your code here
    graph = {x : [] for x in range(n)}
    trans = {x: [] for x in range(n)}
    for src, dst in edges:
        graph[src].append(dst)
        trans[dst].append(src)
    stack = []
    visited = []
    for i in range(n):
        if i not in visited:
            visited.append(i)
            topo(graph, i, visited, stack)
    strongly = []
    index = 0
    visited = []
#     print("topo --- ", stack)
    while stack:
        start = stack.pop()
        if start not in visited:
            visited.append(start)
            strongly.append([])
            dfs(trans, start, visited, strongly[index])
            index +=1
    return strongly

def topo(graph, node, visited, stack):
#     print("traversal", node)
    for child in graph[node]:
        if child not in visited:
            visited.append(child)
            topo(graph, child, visited, stack)
    stack.append(node)

def dfs(graph, node, visited, strongly):
    strongly.append(node)
    for child in graph[node]:
        if child not in visited:
            visited.append(child)
            dfs(graph, child, visited, strongly)