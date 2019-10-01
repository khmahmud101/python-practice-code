li = [2,6,4,2,5,7,4]
unique = []
for i in li:
    if i not in unique:
        unique.append(i)
print(unique)
unique = sorted(unique)
print(unique)
unique = li.count(2)
print(unique)