class MyFile(object):
    text1 = "Hey there I am sagor, come form Gaibandha.\nI am start up python developer(software developer).\nRight now I live uttara sector #14"

    # Here create file method and get data text1 global(class) variable

    def create_file(self):
        _file = open("myself.txt", "w")
        _file.write(self.text1)
        _file.close()

    # This method use created file read

    def read_file(self):
        _file = open("myself.txt", "r")
        content = _file.read()
        print(content)


if __name__ == '__main__':
    """
        Here, after instantiating `MyFile` class, the file prepared `create` and `read` method 
    """
    my_file = MyFile()
    my_file.create_file()
    my_file.read_file()
