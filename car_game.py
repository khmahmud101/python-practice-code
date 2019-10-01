
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("car already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
start -- to start car
stop -- to stop car
quit -- get quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry did't understand")


