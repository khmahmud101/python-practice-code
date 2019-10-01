
t = int(input())
t = int(input())
for i in range(t):
    r1 = int(input())
    n1 = input()
    n2 = input()
    if n1 > n2:
        n1, n2 = n2, n1
    print("case {}:".format(i),n1,n2)

    i += 1


