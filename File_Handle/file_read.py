lines = ["this is first line","this is second line","this is third line"]
with open("file.txt","w") as f:
    for line in lines:
        f.write(line + "\n")
with open("file.txt","r") as f:
    content= f.read()
    print(content)

with open("file.txt","r") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line)

with open("file.txt","r") as f:


    for line in lines:
        print(line)
with open("number.txt","w") as f:
    for line in range(1,100):
        f.write("%s" %line +"\n")
