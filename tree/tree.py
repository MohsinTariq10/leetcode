from urllib import robotparser


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left = Node(4)
root.left.right.left = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def bfs(root):
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def levelorder(root):
    q = []
    q.append(root)
    while q:
        size = len(q)
        for s in range(size):
            node = q.pop(0)
            print(node.val, end=", ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print("\n")

def interative_preorder(root):
    s = []
    s.append(root)
    while s:
        node = s.pop()
        print(node.val)
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)

def interative_inroder(root):
    s = [root]
    left = root.left
    while True:
        if left:
            s.append(left)
            left = left.left
        else:
            node = s.pop()
            print(node.val)
            left = node.right
            if not s and not left:
                break

def iterative_postorder(root):
    s1 = [root]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    
    while s2:
        print(s2.pop().val)


inorder(root)
print("\n")
preorder(root)
print("\n")
postorder(root)
print("\n")
bfs(root)
print("\n")
levelorder(root)
print("\n")
interative_preorder(root)
print("\n")
interative_inroder(root)
print("\n")
iterative_postorder(root)