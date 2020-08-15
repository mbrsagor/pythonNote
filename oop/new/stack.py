class Stack(object):

    def __init__(self):
        self.users = []

    def add_user(self, users):
        self.users.append(users)

    def remove_users(self):
        return self.users.pop()

    def all_users(self):
        return self.users

    def users_count(self):
        return len(self.users)

    def is_users_empty(self):
        return self.users == []

    def remove_all(self):
        return self.users.clear()


if __name__ == '__main__':
    s1 = Stack()

    s1.add_user("mbr-sagor")
    s1.add_user("saif-nirob")
    s1.add_user("russel-mahmud")

    print(s1.all_users())

    xx = s1.remove_users()
    print(xx)

    print(s1.all_users())

    print(s1.users_count())

    print(s1.is_users_empty())

    s1.add_user("russel-mahmud")

    print(s1.all_users())

    s1.remove_all()
    print(s1.all_users())
