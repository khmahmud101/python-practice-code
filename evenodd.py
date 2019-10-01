a = input("Enter your number: ")
a = int(a)
even = [False]* (a+1)
for i in range(0,a+1,2):
    even[i] = True
print(even[a])




