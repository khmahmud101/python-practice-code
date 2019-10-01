class Vehicle:
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving",self.manufacturer,self.name)

    def turn(self,direction):
        print("Turning",self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping!")
class Car(Vehicle):
    """ Car Class"""
    def __init__(self,name,manufacturer,color,year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4
        print("A new car has been created. Name:",self.name)
        print("It has 4 wheels",self.wheels)
        print("the car was built in",self.year)

    def change_gear(self,gear_name):
        """ Method of changing gear"""
        print(self.name,"is changing gear to",gear_name)
if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 FX","walton","Black")
    v2 = Vehicle("Softail Delux","Harley-Davidson","Blue")
    v3 = Vehicle("Mustang 5.0 GT","Ford","Red")
    print("")
    v1.drive()
    v2.drive()
    v3.drive()

    print("")

    v1.turn("left")
    v2.turn("Right")
    print("")
    v1.brake()
    v2.brake()
    v3.brake()

    print("car class object")
    c1 = Car("Mustang 5.0 GT couple", "Ford","Red",2017)



