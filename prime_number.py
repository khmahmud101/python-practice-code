def isprime(num):
    if num<2:
        return False
    prime=True
    for i in range(2,num):
        if num % i==0:
            print(num,"is devided by",i)
            prime=False
    return prime
while True:
    number=input("please enter a number()enter 0 to exit: ")
    number = int (number)
    if number == 0:
        break
    prime=isprime(number)
    if prime is True:
        print(number,"is a prime number.")
    else:
        print(number,"is not a prime number")