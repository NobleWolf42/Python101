__author__ = 'Landon Stoner'

#Import Statements
from turtle import *
from random import randrange

#This section sets the basics for the turtle
speed(10000)
colorno = 0
hideturtle()
pencolor("#79a2c6")
penthick = randrange(1, 4)
pensize(penthick)

#This sets the random angle and the initial distance
angle = randrange(50, 180)
distance = 1
distance_max = randrange(300, 601)

#This starts the loop and implements the cap
while distance < distance_max:

#This series of ifs and elifs changes the color as the drawing as it expands
    if colorno == 1000:
        pencolor("#0d2840")
    elif colorno == 900:
        pencolor("#103250")
    elif colorno == 800:
        pencolor("#133c60")
    elif colorno == 700:
        pencolor("#174670")
    elif colorno == 600:
        pencolor("#1a5080")
    elif colorno == 500:
        pencolor("#1d5a90")
    elif colorno == 400:
        pencolor("#2164a1")
    elif colorno == 300:
        pencolor("#3773aa")
    elif colorno == 200:
        pencolor("#4d83b3")
    elif colorno == 100:
        pencolor("#6392bd")
    else: pass

#This section draws the lines for the object and increases the distance
    forward(distance)
    right(angle)
    distance = distance + 0.5
    colorno = colorno + 1

#This wraps things up
update()
done()