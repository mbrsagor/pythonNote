class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = self.Information()

    def display_all(self):
        show = self.name, self.age, self.info
        return show

    class Information(object):

        def __init__(self):
            self.id = 20343
            self.address = "Dhaka"
            self.className = "Six"


if __name__ == '__main__':
    student_instance = Student("mbr-sagor", 24)
    print(student_instance.display_all())
