import turtle
class Ajobturtle(turtle.Turtle):
    """ This is ajob turtle """
    def forward(self, pixel):
        super().backward(pixel)
    def backward(self, pixel):
        super().forward(pixel)
    def left(self, angel):
        super().right(angel)

    def right(self, angel):
        print("I won't turn right bcz I am ajob")

if __name__ =="__main__":
    montu = Ajobturtle()
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)



    turtle.done()