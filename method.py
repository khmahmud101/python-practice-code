class Vehicle:
    """ Base class for all vehicle"""
    def __init__(self,name,manufacturer,color,):
        self.name = name
        self.manufacturer=manufacturer
        self.color=color
        print("name is:", self.name)

    def drive(self):
        print("Driving: ",self.manufacturer, self.name)
    def turn(self,direction):
        print("Turn: ",self.name,"to", direction)
    def brake(self):
        print(self.name,"is stoping!")

class Car(Vehicle):
    """ Car class"""

    def __init__(self,name,manufacturer,color,year):
        super().__init__(name,manufacturer,color,)
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year=year
        self.wheels=4
        print("A car has been created. Name:",self.name)
        print("It has", self.wheels,"wheels")
        print("The car was built in ",self.year)

    def change_gear(self,gear_name):
        """Method for changing gear"""
        print(self.name,"is changing gear to ", gear_name)



c1 = Car("Mustang 5.0 gt coupe","ford","red",2017)

c1.change_gear("Pass")


