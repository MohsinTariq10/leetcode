#https://leetcode.com/problems/critical-connections-in-a-network/
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = {x: [] for x in range(n) }
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)
        tin = [0] * n
        tlower = [0] * n
        return self.dfs(graph, 0, 0, tin, tlower, 0, [])
        
    
    def dfs(self,graph, node, parent, tin, tlower, counter, bridges):
        tin[node] = counter
        tlower[node] = counter
        for child in graph[node]:
            if child != parent:
                if tin[child] == 0:
                    bridges = self.dfs(graph, child, node, tin, tlower, counter+1, bridges)
                    tlower[node] = min(tlower[child], tlower[node])
                    if(tlower[child] > tin[node]):
                        bridges.append([node, child])
                else:
                    tlower[node] = min(tin[child], tlower[node])
        return bridges