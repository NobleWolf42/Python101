from turtle import *
from random import randrange, choice

def polygon(n, s, h, x, y, c, f):
    """
    Draws a regular polygon with n sides.
    The length of each side is s.
    The pen's initial heading is h.
    The pen begins at point(x, y).
    The polygon's color is c.
    The polygon is filled if f is True; otherwise, the 
    polygon is an outline.
    """
    penup()
    setposition(x, y)
    setheading(h)
    color(c)
    pendown()
    if f:
        begin_fill()
    for i in range(n):
        forward(s)
        left(360//n)
    if f:
        end_fill()


#polygon(8, 100, 30, -100, -100, "blue", False)

for i in range(20):
    polygon(randrange(3, 11), randrange(10, 201),
            randrange(361), randrange(-250, 251),
            randrange(-250, 251),
            choice(("red", "blue", "green", "yellow", "black")),
            randrange(2))
done()

