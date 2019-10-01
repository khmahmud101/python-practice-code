class Vehicle():
    """ Base class for all vehicle """
    def __init__(self,name,manufaturer,color):
        print("creating a vehicle")
        self.name= name
        self.manufacturer= manufaturer
        self.color= color

class Car(Vehicle):
    """ Car class """
    def __init__(self,name,manufaturer,color,year):
        print("Creating a CAR")
        super().__init__(name,manufaturer,color)
        self.year= year
        self.wheels= 4
if __name__ == "__main__":
    c = Car("Mustang 5.0 GT ","Ford","Red",2017)
    print(c.name, c.year, c.wheels)

