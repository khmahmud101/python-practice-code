def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
       print("not devided with zero")
    except TypeError:
        print("Unsupported type.Did you use string?")

print(div(10,2))
print(div(10,0))
print(div("12",3))