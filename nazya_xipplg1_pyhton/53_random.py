import turtle

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
t.color("red") 

t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)

t.end_fill()

t.penup()
t.goto(0, 0)
t.color("black")
t.pendown()
t.hideturtle()
t.write("Mang Eyak??", align="center", font=("Arial", 20, "bold"))

turtle.exitonclick()