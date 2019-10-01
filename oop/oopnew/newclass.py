class Car:
    name = "premio"
    color = "white"

    def start(self):
        print("starting the engine")
print("Name of the car:", Car.name)
print("color:",Car.color)

Car.start('self')

print("")
#Receive Dynamic name and color
class Car:
    name = ""
    color = ""

    def start(self):
        print("starting the engine")
Car.name = "Axio"
Car.color = "Black"

print("Name of the car:", Car.name)
print("color:",Car.color)

Car.start('self')
print("")

class Car:

    def __init__(self,name,color):
        self.name = name
        self.color = color

    def start(self):
        print("starting the engine")
#creating car object
my_car = Car("Corolla","white")
print(my_car.name)
print(my_car.color)
my_car.start()
print("")


class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("starting the engine")


# creating car object
my_car = Car("Corolla", "white")
print(my_car.name)
print(my_car.color)
my_car.start()

print("")
class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Name:",self.name)
        print("Color:",self.color)
        print("starting the engine")



my_car = Car("Corolla", "white")
my_car.start()
print("")

class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Name:",self.name)
        print("Color:",self.color)
        print("starting the engine")



my_car = Car("Corolla", "white")
Car.start(my_car)
print("")

class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Name:",self.name)
        print("Color:",self.color)
        print("starting the engine")



my_car1 = Car("Corolla", "white")
my_car2 = Car("Alion", "Black")
my_car3 = Car("Premio", "Red")
my_car1.start()
my_car2.start()
my_car3.start()
my_car1.year = 2019
my_car2.year = 2019
print(my_car1.year)
print(my_car2.year)



