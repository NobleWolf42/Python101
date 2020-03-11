import turtle
import math
import webbrowser

lake_x, lake_y = -200, 200
beach_x, beach_y = -200, 150
browser_x, browser_y = -200, 100

current_background = "beach"

def option(x, y, label):
    turtle.penup()
    turtle.setposition(x, y - 5)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.setposition(x + 20, y)
    turtle.pendown()
    turtle.write(label)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def draw():
    if current_background == "beach":
        turtle.bgpic("beach.gif")
    else:
        turtle.bgpic("lake.gif")
    option(lake_x, lake_y, "Lake")
    option(beach_x, beach_y, "Beach")
    option(browser_x, browser_y, "Browser")
    turtle.update()
    

def mouseclick(x, y):
    global current_background
    print("**** x =", x, "y =", y)
    if distance(x, y, lake_x, lake_y) < 10:
        current_background = "lake"
    elif distance(x, y, beach_x, beach_y) < 10:
        current_background = "beach"
    elif distance(x, y, browser_x, browser_y) < 10:
        if current_background == "lake":
            webbrowser.open_new("https://en.wikipedia.org/wiki/Lake")
        else:
            webbrowser.open_new("https://en.wikipedia.org/wiki/Beach")
    draw()

turtle.tracer(0)
turtle.hideturtle()
turtle.onscreenclick(mouseclick)
draw()
turtle.mainloop()
