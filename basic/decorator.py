def say_hello(func):
    def welcome():
        print("Hello everyone, how are you?")
        func()
        print("Welcome, to your website")

    return welcome()


@say_hello
def say_something():
    print("I'm calling to say something decorator method")


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


items = [1, 2, 3, 10, 3, 12]
result = contains_duplicate(items)
print(result)
