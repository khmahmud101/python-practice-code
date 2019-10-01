lines = ["this is first line","this is second line","this is third line"]

with open("file.txt","w") as f:
    for line in lines:
        f.write(line+"\n")

with open("file.txt","r") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line)
with open("file.txt","r") as f:
    for line in f:
        print(line)
