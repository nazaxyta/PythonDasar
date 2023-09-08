import turtle

def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_trapezium(base1, base2, height):
    turtle.forward(base1)
    turtle.left(135)
    turtle.forward(height)
    turtle.left(45)
    turtle.forward(base2)
    turtle.left(45)  
    turtle.forward(height)
    turtle.left(135) 
    turtle.forward(base1)
    turtle.forward(base2)

def belahket(base, height):
    turtle.forward(base)
    turtle.left(60)
    turtle.forward(height)
    turtle.left(120)
    turtle.forward(base)
    turtle.left(60)
    turtle.forward(height)

def jajargen(side_length):
    for _ in range(2):
        turtle.forward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        turtle.left(120)

turtle.speed(5)

turtle.color
turtle.begin_fill()
draw_rectangle(100, 50)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

turtle.color
draw_triangle(100)

turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()

turtle.color
draw_trapezium(100, 200, 80)

turtle.penup()
turtle.goto(150, -100)
turtle.pendown()

turtle.color
belahket(100, 50)

turtle.penup()
turtle.goto(-100, -200)
turtle.pendown()

turtle.color
jajargen(70)

turtle.exitonclick()