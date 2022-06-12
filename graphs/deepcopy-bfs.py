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
        
def cloneGraph(node):
    # Write your code here.
    visited = [node.data]
    deepcopy = graphNode(node.data)        
    q = [(node, deepcopy)]
    ref = {}
    ref[deepcopy.data] = deepcopy
    while q:
        node, noded = q.pop()
        for child in node.neighbours:
            if child.data not in visited:
                childcopy = graphNode(child.data)
                ref[childcopy.data] =  childcopy
                noded.neighbours.append(childcopy)
                visited.append(child.data)
                q.append((child, childcopy))
            else:
                noded.neighbours.append(ref[child.data])
    return deepcopy
        
    
