pat = [5,2,5,2,4]
for item in pat:
    print(item*"x")
  #simple way
print("")
#wih nested loop
for i in pat:
    result = ''
    for j in range(i):
        result +="x"
    print(result)