"""
position = -1


def linear_search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['position'] = i
            return True
        i += 1

    return False


list = [2, 5, 3, 10, 9]
n = 9

if linear_search(list, n):
    print(f"Found list position: {position+1}")
else:
    print("Not found")


"""


def linearSearch(list, data):
    for _data in range(0, len(list)):
        if list[_data] == data:
            return data, "was found at position ", str(_data)
        else:
            return data, "was not found in this list"


list = [30, 10, 50, "sagor", True, "ritu"]
search_item = linearSearch(list, 50)
print(search_item)
