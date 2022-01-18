class About(object):

    @classmethod
    def get_full_name(cls, first, last):
       print(f"Full Name is: {first} {last}")

    @staticmethod
    def get_name(name):
        print(f"Hello {name}")


if __name__ == '__main__':
    About.get_full_name('mbr', 'sagor')
    About.get_name('sagor')
