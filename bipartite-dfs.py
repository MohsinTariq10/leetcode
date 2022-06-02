class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = ['' for x in range(len(graph))]
        visited = []
        for index, value in enumerate(colors):
            if value != "":
                continue
            if not self.dfs(graph, index, visited, colors):
                return False
            print(colors)
        return True
    
    def dfs(self, graph, start ,visited, colors):
        children = graph[start]
        colors[start] = not not colors[start]
        if start not in visited: visited.append(start)
        ret = True
        for child in children:
            if child not in visited:
                visited.append(child)
                colors[child] = not colors[start]
                ret = self.dfs(graph, child, visited, colors)
            else:
                if colors[child] == colors[start]:
                    print(start, child)
                    return False
        return ret
        