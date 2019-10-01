class car:

    def __init__(self,name,color,year):
        self.name=name
        self.color=color
        self.year = year


    def start(self):
        print(" name is", self.name)
        print(" color is", self.color)
        print(" color is", self.year)
        print(" cc is", self.cc)
        print(" start the engine")

    def stop(self):
        print(" name is", self.name)
        print(" color is", self.color)
        print(" stop the car")



my_car1=car("premio","white",2007)
my_car2=car("allion","red",2007)
my_car1.cc=2100
my_car1.start()



