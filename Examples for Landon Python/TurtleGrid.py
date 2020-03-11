__author__ = 'Landon Stoner'
from turtle import *
hideturtle()
speed(100)
tracer(0)

#This section sets variables to be used in grid drawing
x = -50
y = 50

penup()
setpos(x,y)
pendown()
#This section is a loop for drawing squares
for i in range(1, 11):
    for i in range(1, 11):
        forward(10)
        right(90)
        forward(10)
        right(90)
        forward(10)
        right(90)
        forward(10)
        right(90)
        penup()
        forward(10)
        pendown()
    penup()
    right(90)
    forward(10)
    right(90)
    forward(100)
    right(180)
    pendown()
update()
done()