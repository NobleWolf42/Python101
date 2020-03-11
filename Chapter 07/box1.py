from turtle import *

def box(x, y):
    penup()
    setposition(x, y)
    pendown()
    setheading(0)
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    update()

if __name__ == "__main__":
    tracer(0)
    hideturtle()
    box(0, 0)
    box(200, 100)
    done()
