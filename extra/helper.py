class Helper(object):

    def __init__(self):
        self.items = []

    def add(self, val):
        item = self.items.append(val)
        return item

    def add_first(self, val):
        return self.items.insert(0, val)

    def remove_fist(self, val):
        return self.items.remove(val)

    def remove_last(self, val):
        return self.items.pop(val)

    def display(self):
        return self.items

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.size() == 0:
            return f"Sorry! No item found"


if __name__ == '__main__':
    helper = Helper()
    helper.add(1)
    helper.add(2)
    helper.add(5)
    helper.add(3)
    helper.add(2)
    helper.add(50)
    helper.add(30)
    print(helper.display())
    print(helper.size())
    helper.remove_last(2)
    print(helper.display())
    print(helper.size())
    print(helper.is_empty())
    helper.remove_fist(30)
    print(helper.display())
    helper.add_first(20)
    print(helper.display())
