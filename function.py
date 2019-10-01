import turtle
def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

count = 0
while count<90:
    draw_square(100)
    turtle.right(4)
    count +=1
turtle.exitonclick()