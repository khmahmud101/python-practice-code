class computer:
 def __init__(self):
     self.name="navin"
     self.age=28
 def compare(self,others):
     if self.age == others.age:
         return True
     else:
         return False



c1= computer()
c1.age=27

c2 =computer()

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")

v1=Vehicle("fusion 11 gx","walton","black")
v2 = Vehicle("sachema 11 fg","ford","red")
v3 =Vehicle("roar x","Audi","white")

v1.drive()
v2.drive()
v3.drive()

v1.turn("left")
v2.turn("right")

v1.brake()
v2.brake()
v3.brake()