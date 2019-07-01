first_str = input("Enter first text:")
second_str = input("Enter second text:")

if len(first_str) == len(second_str):
    if sorted(first_str) == sorted(second_str):
        print("They are anagrams")
    else:
        print("They are not anagrams")
else:
    print("Sorry!! Length are not same")
