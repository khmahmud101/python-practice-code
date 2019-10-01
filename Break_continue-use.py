terminate = False
while not terminate:
    number1 = int(input(" Please enter a number: "))
    number2 = int(input(" Please enter another number: "))
    while True:
        operation  = input( "Plearse enter (add or sub or quit): ")
        if operation == "quit":
            terminate = True
            break
        if operation not in ["add","sub"]:
            print("unknown program!")
            continue
        if operation == "add":
            print("number add is", number1+number2)
            break
        if operation == "sub":
            print("number sub is", number1 - number2)
            break



















