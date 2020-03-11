from turtle import *

title("Filled Box")
tracer(0)
hideturtle()
color("blue")
begin_fill()
for n in range(4):
    forward(100)
    left(90)
end_fill()

done()
