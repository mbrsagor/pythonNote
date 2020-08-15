numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def square(number):
    return number * number


my_list = list(map(square, numbers))
print(my_list)


def revarse(string):
    revarse_text = ''
    for _text in string:
        revarse_text = _text + revarse_text
    print(f"Revarse string is: {revarse_text}")


string = input("Enter write something: ")
print(string)
revarse(string)
