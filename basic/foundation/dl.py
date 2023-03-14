# Double LinkList

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    def __init__(self):
        self.head = None

    # add item the linklist
    def add_item(self, new_item):
        new_node = Node(new_item)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node


# print the double linklist
def linklist(node):
    while node is not None:
        print(node.item)
        last = node
        node = node.next


link_list = DoubleLinkList()

link_list.add_item(5)
link_list.add_item(15)
link_list.add_item(4)
link_list.add_item(14)
link_list.add_item(20)

linklist(link_list.head)
