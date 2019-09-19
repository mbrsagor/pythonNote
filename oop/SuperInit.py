class Super(object):

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_all(self):
        _get_instance = f"Full Name:{self.first_name + ' ' + self.last_name}\nFirst Name: {self.first_name}\nLast Name:" \
                        f" {self.last_name}\nEmail:{self.email}\nPassword:{self.password}"
        return _get_instance


class Client(Super):
    def __init__(self, first_name, last_name, email, password, address, phn_number, amount):
        super().__init__(first_name, last_name, email, password)
        self.address = address
        self.phn_num = phn_number
        self.amount = amount


if __name__ == '__main__' :
    instance = Client('mbr', 'sagor', 'mbrsagor@gmail.com', 's12345', 'uttara sector-11', 1773474709, 35000)
    print(instance.get_all())
