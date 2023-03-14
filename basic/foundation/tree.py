class Node(object):
    """
    The tree name is general tree.
    """

    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
k = Node("K")
l = Node("L")

# adding child node
a.add_child(b)
a.add_child(c)
a.add_child(d)

b.add_child(e)
b.add_child(f)
b.add_child(g)

g.add_child(h)

d.add_child(k)
d.add_child(l)

# Print child of A
print("Child of A Are:")
for child in a.children:
    print(child.val)

# Print child of D
print("Child of D Are:")
for child in d.children:
    print(child.val)
