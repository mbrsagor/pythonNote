class OOP(object):
    table_name = "User Table"

    def __init__(self):
        pass

    @classmethod
    def get_table(cls):
        return cls.table_name

    @staticmethod
    def get_something():
        return OOP.table_name


user = OOP()
print(user.get_table())
print(user.get_something())
