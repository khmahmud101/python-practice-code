try:
    fobj = open("test", "r")
    content = fobj.read()
    print(content)

except Exception as e:
    print("file error")
finally:
    fobj.close()

try:
    with open("test","r") as myfile:
        content = myfile.read()
        print(content)
except Exception as e:
    print("file error")

with open("test","w") as myfile:
    for i in range(1,100+1):
        myfile.write(int(i))
