with open("country.txt","r") as f:
    lines = f.readlines()
    for line in lines:

        if line.startswith("A"):
            with open("a.txt", "a") as f:
                f.write(line)
        if line.startswith("B"):
            with open("b.txt", "a") as f:
                f.write(line)









