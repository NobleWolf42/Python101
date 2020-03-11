from turtle import *

count = 0

title("Grid")
tracer(0)
speed(10)
hideturtle()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
while count < 5:
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
    forward(100)
    left(90)
    count = count + 1

right(180)
forward(100)
right(90)

count = 0

while count < 5:
    forward(10)
    right(90)
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    count = count + 1

update()

done()
