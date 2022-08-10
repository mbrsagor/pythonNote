class Node(object):

    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class SLinkList(object):

    def __init__(self):
        self.head_val = None

    def display(self):
        show_val = self.head_val
        while show_val is not None:
            print(show_val.data_val)
            show_val = show_val.next_val


sll = SLinkList()
sll.head_val = Node("Fri")
e2 = Node("Sun")
e3 = Node("Mon")
e4 = Node("Tue")

sll.head_val.next_val = e2
e2.next_val = e3
e3.next_val = e4
sll.display()
