class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = ['' for x in range(len(graph))]
        for index, value in enumerate(colors):
            if value != "":
                continue
            queue = [index]
            visited = [index]
            colors[index] = True
            while len(queue) is not 0:
                node = queue.pop(0)
                for i in graph[node]:
                    if i not in visited:
                        colors[i] = not colors[node]
                        queue.append(i)
                        visited.append(i)
                    else:
                        if colors[node] == colors[i]:
                            return False
        return True