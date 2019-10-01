import turtle
turtle.shape("turtle")
turtle.speed(1)
for length in range(100,200,20):
    for i in range (4):
        turtle.forward(length)
        turtle.left(90)

turtle.exitonclick()
