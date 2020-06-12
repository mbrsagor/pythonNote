def map_function(n):
    return n + n


num = (1, 2, 3, 4, 5)
result = map(map_function, num)
print(list(result))