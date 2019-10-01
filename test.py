
class car:
    name = ""
    color = " "

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("car name:",self.name,"car color:",self.color,"car year:",self.year)
        print("start the engine")
        print()

car.year=2017
co1 = car("corola","white")
co1.start()
co2 = car("premio","black")
co2.start()
co3 = car("allion","red")
co3.start()




