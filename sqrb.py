while True:
    n = int(input("Enter a number (without 0): "))
    if n < 0:
       print("We allow only positive number", n, "is not allowed")
       continue
    if n == 0:
        print(n,"is not allow")
        break
    print("squire of ",n,"is",n*n)



