from turtle import *
from random import randrange


def mouse_clicked(x, y):
    print("x =", x, " y =", y)
    if x < 0 and y < 0:
        name = textinput("You selected two negative values",
                         "Please enter your name")
        print("Hello", name)
    polygon(4, x, y)
    update()


def polygon(n, x, y):
    """
    Draws a regular polygon with n sides.
    The pen begins at point(x, y).
    """
    penup()
    setposition(x, y)
    pendown()
    for i in range(n):
        forward(50)
        left(360//n)


#polygon(8, 100, 30, -100, -100, "blue", False)

#mouse_clicked(45, 2)

# Speed up the rendering
tracer(0)
# Do not show the pen
hideturtle()
# Bind the mouse click event to our function
onscreenclick(mouse_clicked)

## Draw some random polygons
#for i in range(20):
#    polygon(randrange(3, 11), randrange(-250, 251), randrange(-250, 251))
update()
mainloop()

