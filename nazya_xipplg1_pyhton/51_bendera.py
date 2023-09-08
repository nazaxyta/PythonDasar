import turtle

flag = turtle.Turtle()

def draw_rectangle(color, width, height):
    flag.begin_fill()
    flag.fillcolor(color)
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()

screen = turtle.Screen()
screen.setup(width=600, height=400)

flag.penup()
flag.goto(-300, 200)
flag.pendown()
draw_rectangle("red", 600, 200)

flag.penup()
flag.goto(-300, 0)
flag.pendown()
draw_rectangle("white", 600, 200)

flag.hideturtle()

turtle.done()