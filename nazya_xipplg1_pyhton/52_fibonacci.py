import turtle

def fibonacci_tree(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        t.forward(size)
        t.left(45)
        fibonacci_tree(t, order - 1, size / 2)
        t.right(90)
        fibonacci_tree(t, order - 1, size / 2)
        t.left(45)
        t.backward(size)

t = turtle.Turtle()
t.speed(0) 
t.penup()
t.goto(0, -250)
t.pendown()

fibonacci_tree(t, 5, 200)

turtle.exitonclick()