a = 6
b=2

try:
    print(a/b)
    k=int(input("enter a input: "))
    print(k)
except ZeroDivisionError as e:
    print(" unknown error accoured")
except  ValueError as e:
    print(" Ivalid input")
except Exception as e:
    print(" unknown error accoured",e)
finally:
    print("bye")
