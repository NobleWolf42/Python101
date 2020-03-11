__author__ = "Benjamin Carpenter", "Landon Stoner", "Josh Wade"


#Imports
from turtle import *
from board import *


#Global Variables
boardwidth = 200
boardheight = 200
squaresize= 5
gameboard = Board(boardwidth, boardheight)

hideturtle()
tracer(0)

#Definitions
def square(x, y, size, col = 'black'):
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

def nextFrame():
    clear()
    # Transformations:
    vertical = (boardheight * squaresize + squaresize)/2
    horizontal = -1 * (boardwidth * squaresize + squaresize)/2

    for x in range(boardwidth):
        for y in range(boardwidth):
            if gameboard.get(x, y):
                square(x*squaresize + horizontal, y*squaresize + vertical, squaresize, (0.9, 0.9, 0.9))
            else:
                square(x*squaresize + horizontal, y*squaresize + vertical, squaresize)
    update()


title("Conway's Game of Life")

#Random Crap
gameboard.set(100, 100, True)
gameboard.set(100, 101, True)
gameboard.set(100, 99, True)
gameboard.set(101, 100, True)
gameboard.set(99, 100, True)

for i in range(100):
    nextFrame()
