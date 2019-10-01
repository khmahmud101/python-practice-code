year = input("Enter year: ")
year = int(year)

if year % 4 != 0:
    print("no")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("yes")
        else:
            print("no")
    else:
        print("yes")

if  year % 400 == 0:
    print("yes")
elif year % 100 == 0:
    print("no")
elif year % 4 == 0:
    print("yes")
else:
    print("no")








