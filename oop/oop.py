class Car:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def start(self):
        print("name: ", self.name)
        print("color: ", self.color)
        print("year: ", self.year)
        print("start the car")

my_car=Car("corolla","white")
my_car.year=2014
my_car2=Car("alion","red")
my_car2.year=2014
my_car.start()
my_car2.start()