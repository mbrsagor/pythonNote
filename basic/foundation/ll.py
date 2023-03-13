class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None


    def add_item_end(self, new_item):
        new_node = Node(new_item)
        if self.head is None:
            self.head = new_node
            return
        last_item = self.head
        while last_item.next:
            last_item = last_item.next
        last_item.next = new_node


linked_list = LinkList()

linked_list.head = Node('2')
second = Node("4")
third = Node("6")

# connect node
linked_list.head.next = second
second.next = third
# add node last
linked_list.add_item_end("10")
linked_list.add_item_end("12")
linked_list.add_item_end("15")

while linked_list.head is not None:
    print(linked_list.head.item, end=' ')
    linked_list.head = linked_list.head.next
