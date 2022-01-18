def select(num):
    def child():
        return "Hello, I'm Mbr Sagor"
    
    def child2():
        return "Hi, This is a Bozlur here."
    
    if num == 1:
        return child()
    else:
        return child2()



print(select(1))
print(select(2))
