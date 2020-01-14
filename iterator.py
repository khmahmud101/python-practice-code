mytuple =  ("apple","banana","cherry")
myit = iter(mytuple)
#print(myit)
print(next(myit))
print(next(myit))
print(next(myit))
print("")
for i in mytuple:
    print(i)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
