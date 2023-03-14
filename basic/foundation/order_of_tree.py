class Node(object):
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    # Traverse preorder
    def preorder_traverse(self):
        print(self.val, end=' ')
        if self.left:
            self.left.preorder_traverse()
        if self.right:
            self.right.preorder_traverse()

    # Traverse inorder
    def inorder_traverse(self):
        if self.left:
            self.left.inorder_traverse()
        print(self.val, end=' ')
        if self.right:
            self.right.inorder_traverse()

    # Traverse postorder
    def postorder_traverse(self):
        if self.left:
            self.left.postorder_traverse()
        if self.right:
            self.right.postorder_traverse()
        print(self.val, end=' ')


root = Node("A")
root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

print("Preorder traversal:")
root.preorder_traverse()
print("\n")
print("On order traversal:")
root.inorder_traverse()
print("\n")
print("postorder traversal:")
root.postorder_traverse()
