yr=2000
if yr % 4!=0:
    print("no")
else:
    if yr % 100==0:
        if yr % 400==0:
            print("yes")
        else:
            print("no")
    else:
        print("no")

if yr%400==0:
    print("yes")

elif yr%100==0:
    print("no")
elif yr%4==0:
    print("yes")
else:
    print("no")

if yr % 100 !=0 and yr % 4 ==0:
    print("yes")
elif yr % 100==0 and yr % 400==0:
    print("yes")
else:
    print("no")









