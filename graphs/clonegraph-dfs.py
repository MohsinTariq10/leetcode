# Class for graph node is as follows:
class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()

def dfs(node, visited, ref):
    deepcopy = graphNode(node.data)
    ref[node.data] = deepcopy
    l = []
    for child in node.neighbours:
        if child.data not in visited:
            visited.append(child.data)
            l.append(dfs(child, visited, ref))
        else:
            l.append(ref[child.data])
    deepcopy.neighbours = l
    return deepcopy
            

def cloneGraph(node):
    # Write your code here.
    visited = [node.data]
    ref = {}
    return dfs(node, visited, ref)