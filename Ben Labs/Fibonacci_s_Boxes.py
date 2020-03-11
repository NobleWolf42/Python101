#This allows me to use the drawing function (Turtle)
from turtle import *

#These define the varibles used later on in the program
count = 0
lengthofline = 1
previous = 1

#My title
title("Fibonacci's Pyramid")

#These statements specify no animation and remove the triangle (Turtle)
tracer(0)
hideturtle()

#This creates multipule boxs (A total of 20 to be exact), but it also increases in size and rotates the box
while count < 250:
    forward(lengthofline)
    left(90)
    forward(lengthofline)
    left(90)
    forward(lengthofline)
    left(90)
    forward(lengthofline)

    #This is what counts the number of boxes
    count = count + 1

    #This is what increases the size of the boxes
    lengthofline = lengthofline + previous

#This is to enshure all defined lines are drawn
update()

#This stops the drawing
done()
