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
    for y in range(-100, 101, 20):
        for x in range(-100, 101, 20):
            box(x, y)
    done()
