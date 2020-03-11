from turtle import *
from random import randrange
from time import clock

#tracer(0)
start_time = clock()
for i in range(100):
    x = randrange(-200, 201)
    y = randrange(-200, 201)
    setposition(x, y)
    if i % 3 == 0:
        color("red")
    elif i % 3 == 1:
        color("blue")
    elif i % 3 == 2:
        color("green")
stop_time = clock()
print(stop_time - start_time, " sec")

#update()
done()

