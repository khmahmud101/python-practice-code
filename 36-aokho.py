import turtle
turtle.speed(5)
turtle.color("red")
count = 0
while count <= 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    count+=1
turtle.exitonclick()