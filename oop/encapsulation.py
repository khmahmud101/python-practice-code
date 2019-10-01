class car():
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color= color


    def set_speed(self,speed):
        self.__speed=speed
    def get_speed(self):
        return self.__speed

c1= car(300,"red")
c2 =car(400,"blue")
c1.set_speed(600)
print(c1.get_speed())

