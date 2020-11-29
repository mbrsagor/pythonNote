first_name = "sagor"
last_name = "sagor"
result = "Yes!! correct name" if first_name == last_name else "incorrect name"
print(result)

person1 = "sagor"
person2 = "ohi"
output = "They are equal" if person1 == person2 else "They are not equal"
print(output)

tarnary_operator = [(x,y) for x in range(5) for y in range(5) if x * y<10]
print(tarnary_operator)

def checkBigNumber(num, num2): "Num is gettr then num2" if num > num2 else "Invalid request"
big_num = checkBigNumber(10, 15)
print(big_num)
