command = ""
started = False

while True:
    command = input(">> ")
    if command.lower() == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car is started")
    elif command.lower() == "stop":
        if not started:
            print("Car is already stoped")
        else:
            started = False
            print("Cart is stop")
    elif command == "help":
        print("""
start => Start the car
stop => Stop the car
quit => Quit 
        """)
    elif command == "quit":
        break
    else:
        print("Invalid command")
