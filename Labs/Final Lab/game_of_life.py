__author__ = "Benjamin Carpenter", "Landon Stoner", "Josh Wade"


#Imports
from turtle import *
from board import *
from time import sleep
import math

screen = getscreen()

#Global Variables
boardwidth = 100
boardheight = 100
squaresize= 5
gameboard = Board(boardwidth, boardheight)
running = False

penup()
hideturtle()
tracer(0)

#Definitions
def square(x, y, size, col = 'red'):
    '''
    Draws a square with the given coordinates (for the top left of the square), size, and optional color.
    '''
    width(1)
    fillcolor(col)
    color(col)
    penup()
    setheading(0)
    goto(x, y)
    pendown()
    begin_fill()
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()

def nextFrame(doNext = True):
    if doNext:
        print("hello")
        clear()
        gameboard.next()
    # clear()
    # Transformations:
    vertical = (boardheight * squaresize)/2
    horizontal = (boardwidth * squaresize)/2
    for x in range(boardwidth):
        for y in range(boardwidth):
            if gameboard.get(x, y):
                # square(x*squaresize + horizontal, y*squaresize + vertical, squaresize)
                square(x*squaresize - horizontal, y*squaresize - vertical, squaresize)
                # pass
            # else:
                # square(x*squaresize - horizontal, y*squaresize - vertical, squaresize)
            # print("hi")
    update()


#Random Crap
'''
gameboard.set(0, 0, True)
gameboard.set(99, 99, True)
gameboard.set(0, 99, True)
gameboard.set(99, 0, True)
gameboard.set(24, 25, True)

gameboard.set(29, 29, True)
gameboard.set(30, 29, True)
gameboard.set(31, 29, True)
gameboard.set(29, 30, True)
gameboard.set(30, 30, True)
gameboard.set(31, 30, True)
gameboard.set(29, 31, True)
gameboard.set(30, 31, True)
gameboard.set(31, 31, True)
'''

def gloop():
    while True:
        #clear()
        nextFrame(running)

def addSquare(x, y):
    vertical = (boardheight * squaresize)/2
    horizontal = (boardwidth * squaresize)/2

    sqX = math.floor(x + (boardwidth/2 * squaresize)/squaresize)
    sqY = math.floor(y + (boardheight/2 * squaresize)/squaresize)
    if abs(sqX) > boardwidth or abs(sqY) > boardheight:
        print(abs(sqX))
        print(abs(sqY))
        print(abs(boardwidth))
        print(abs(boardheight))
        return
    gameboard.switch(sqX, sqY)
    nextFrame(False)

def drawgrid():
    pencolor("blue")
    h = -((squaresize*boardheight)/2)
    w = -((squaresize*boardwidth)/2)-squaresize
    for i in range(-1, boardheight):
        penup()
        goto(h, w)
        h += squaresize
        setheading(90)
        pendown()
        forward(squaresize*boardheight)
        penup()
    h = -((squaresize*boardheight)/2)
    w = -((squaresize*boardwidth)/2)-squaresize
    for j in range(-1, boardwidth):
        penup()
        goto(h, w)
        w += squaresize
        setheading(0)
        pendown()
        forward(squaresize*boardwidth)
        penup()


def run():
    global running
    running = not running
    if not running:
        drawgrid()
        update()

def hello(a, b):
    i = int(a)
    j = int(b)
    if i % 5 != 0:
        if i % 2 == 0:
            i -= 2
            if i % 5 != 0:
                i -= 2
        else:
            i -= 1
            if i % 5 != 0:
                i -= 2
    if j % 5 != 0:
        if j % 2 == 0:
            j -= 2
            if j % 5 != 0:
                j -= 2
        else:
            j -= 1
            if j % 5 != 0:
                j -= 2
    vertical = (boardheight * squaresize)/2
    horizontal = (boardwidth * squaresize)/2
    x = int((i+horizontal)/squaresize)
    y = int((j+vertical)/squaresize)
    gameboard.switch(x, y)

#square((-boardwidth * squaresize)/2, (boardwidth * squaresize)/2, boardwidth*squaresize)
drawgrid()
onscreenclick(hello)
screen.listen()
screen.onkeyrelease(run, "p")
goto(0,0)
gloop()
mainloop()
