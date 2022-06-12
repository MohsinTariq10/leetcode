class Graph:
  def __init__(self, undirected):
    self.adjlist = {  };
    self.undir = undirected;

  def addEdge(self, u, v):
    if u not in self.adjlist:
      self.adjlist[u] = [];
    if v not in self.adjlist:
      self.adjlist[v] = [];

    self.adjlist[u].append(v);
    if self.undir:
      self.adjlist[v].append(u);

  def getAdjList(self):
    return self.adjlist;

def traverse(adj, source):
    distance = [len(adj) for x in range(len(adj))]
    dur = 0
    visited = []
    visited.append(source)
    dfs(adj, source, visited, distance, dur)
    print(distance)
def dfs(graph, start, visited, distance, dur):
  visited.append(start)
  for child in graph[start]:
    if child not in visited:
        dur = dur + 1
        distance[child] = min(dur, distance[child])    
        dfs(graph, child, visited, distance, dur)

if __name__=='__main__':
    g = Graph(True)
    g.addEdge(0,1)
    g.addEdge(0,3)
    g.addEdge(1,2)
    g.addEdge(2,6)
    g.addEdge(3,4)
    g.addEdge(4,5)
    g.addEdge(5,6)
    g.addEdge(6,7)
    g.addEdge(6,8)
    g.addEdge(7,8)
    traverse(g.getAdjList(), 0)
