# Joshua Wade
# Landon Stoner
# Ben Carpenter

from turtle import *
from math import floor

tracer(0)
hideturtle()

board = []
running = False

for i in range(60):
    row = []
    for j in range(60):
        row.append(False)
    board.append(row)

cellsToCheck = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

def check(row, column):
    livingCells = 0
    for cell in cellsToCheck:
        rowToCheck = row + cell[0]
        columnToCheck = column + cell[1]

        if rowToCheck >= len(board):
            rowToCheck = 0
        if columnToCheck >= len(board):
            columnToCheck = 0

        if board[rowToCheck][columnToCheck] == True:
            livingCells += 1

    if livingCells <= 1 or livingCells >= 4:
        return False

    if livingCells == 3:
        return True

    if livingCells == 2 and board[row][column] == True:
        return True
    else:
        return False

def tick():
    global board
    newBoard = []
    for row in range(len(board)):
        r = []
        for column in range(len(board[0])):
            r.append(check(row, column))
        newBoard.append(r)
    board = newBoard

def draw():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column]:
                penup()
                goto(column*10 - 300, row*-10 + 300)
                pendown()
                seth(0)
                begin_fill()
                for i in range(4):
                    forward(10)
                    right(90)
                end_fill()
    update()

def drawGrid():
    penup()
    goto(-300, 300)
    seth(-90)
    pendown()
    for i in range(2):
        for j in range(61):
            forward(600)
            penup()
            backward(600)
            left(90)
            forward(10)
            right(90)
            pendown()
        penup()
        right(90)
        forward(10)

def pause():
    global running
    running = not running

def click(x, y):
    row = y
    column = x

    row += 300
    column -= 300

    row /= -10
    column /= 10

    row = floor(row)
    column = floor(column)
    board[row][column] = not board[row][column]

onscreenclick(click)
onkeyrelease(pause, "p")
listen()

while True:
    clear()
    if running:
        tick()
    else:
        drawGrid()
    draw()
