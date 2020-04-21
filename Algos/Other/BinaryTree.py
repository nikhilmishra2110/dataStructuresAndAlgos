class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal):
        if traversal == "preorder":
            return self.preoreder_print(self.root, "")
        elif traversal == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal =="postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type ", traversal, "is not supported")

    def preoreder_print(self, root, traversal):
        """Root -> Left -> Right"""
        if root:
            traversal += str(root.value) + " -> "
            traversal = self.preoreder_print(root.left, traversal)
            traversal = self.preoreder_print(root.right, traversal)
        return traversal

    def inorder_print(self, root, traversal):
        """Left -> Root -> Right"""
        if root:
            traversal = self.inorder_print(root.left, traversal)
            traversal += str(root.value)+ " -> "
            traversal = self.inorder_print(root.right, traversal)
        return traversal

    def postorder_print(self, root, traversal):
        if root:
            traversal = self.postorder_print(root.right, traversal)
            traversal += str(root.value) + " -> "
            traversal = self.postorder_print(root.left, traversal)
        return traversal

tree = Binary_tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)
print (tree.print_tree("preorder")) # 1-2-4-8-9-5-3-6-7-
print (tree.print_tree("inorder")) # 8 - 4 - 9 - 2 - 5 - 1 - 6 - 3 - 7 -
print (tree.print_tree("postorder")) # 8 - 4 - 9 - 2 - 5 - 1 - 6 - 3 - 7 -


