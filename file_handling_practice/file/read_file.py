lines = ["This is lin one","This is lin two","This is lin three",]

with open("file_write.txt","w") as fp:
    for line in lines:
        fp.write(line+"\n")


with open("file_write.txt","r") as fp:
    content = fp.read()
    print(content)


with open("file_write.txt","r") as fp:
    lines = fp.readlines()
    print(lines)
    for line in lines:
        print(line)

with open("file_write.txt","r") as fp:
    for line in fp:
        print(line)




