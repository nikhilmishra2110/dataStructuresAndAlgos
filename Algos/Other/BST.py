class Node:
    def __init__(self, data =None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, data, curr):
        if data < curr.data:
            if curr.left is None:
                curr.left = Node(data)
            else:
                self._insert(data, curr.left)
        elif data > curr.data:
            if curr.right is None:
                curr.right = Node(data)
            else:
                self._insert(data, curr.right)
        else:
            print(" Given data is already present in the tree ")

    def insert(self, data):
        # Case 1: there is no root
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _find(self, data, curr):
        if curr.data == data:
            return True
        elif data < curr.data and curr.left:
            return self._find(data, curr.left)
        elif data > curr.data and curr.right:
            return self._find(data, curr.right)

    def find(self, data):
        if self.root:
            found = self._find(data, self.root)
            if found:
                return True
            else:
                return False
        else: return None

b = BST()

b.insert(4)
b.insert(3)
b.insert(6)
b.insert(9)
b.insert(1)
b.insert(7)
print(b.find(7))
print(b.find(79))





