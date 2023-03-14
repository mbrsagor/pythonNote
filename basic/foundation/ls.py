def linear_search(items, key):
    # Going through the list
    for item in range(len(items)):
        if items[item] == key:
            return item
    return -1


prime_list = [2, 3, 5, 7, 11, 13]
target = 2
result = linear_search(prime_list, target)

if result == -1:
    print(f"{target} Not found list")
else:
    print(f"Found the list:{target} index:{result}")
