class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cr = self.root
        for c in word:
            cr = cr.add_child(c)
        cr.isEnd = True

    def search(self, word: str) -> bool:
        cr = self.root
        for c in word:
            if c in cr.children:
                cr = cr.children[c]
            else:
                return False
        return cr.isEnd

    def startsWith(self, prefix: str) -> bool:
        cr = self.root
        for c in prefix:
            if c in cr.children:
                cr = cr.children[c]
            else:
                return False
        return True

class Node:
    def __init__(self, val = -1, children = None, isEnd = False):
        self.val = -1
        self.children = children if children!=None else {}
        self.isEnd = isEnd

    def add_child(self, val):
        if val not in self.children:
            self.children[val] = Node(val)
        return self.children[val]
