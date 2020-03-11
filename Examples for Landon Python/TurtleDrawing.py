__author__ = 'Landon Stoner'
from turtle import *
from random import randrange
speed(10000)
colorno = 0
hideturtle()
pencolor("#061420")


penup()
setpos(-250, -250)
pendown()

angle = randrange(1, 180)
distance = randrange(200, 501)
while distance > 0.5:
    if colorno == 100:
        pencolor("#0d2840")
    elif colorno == 200:
        pencolor("#103250")
    elif colorno == 300:
        pencolor("#133c60")
    elif colorno == 400:
        pencolor("#174670")
    elif colorno == 500:
        pencolor("#1a5080")
    elif colorno == 600:
        pencolor("#1d5a90")
    elif colorno == 700:
        pencolor("#2164a1")
    elif colorno == 800:
        pencolor("#3773aa")
    elif colorno == 900:
        pencolor("#4d83b3")
    elif colorno == 1000:
        pencolor("#6392bd")
    else: pass
    forward(distance)
    left(angle)
    distance = distance - 0.5
    colorno = colorno + 1
update()
done()