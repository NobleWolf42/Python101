from turtle import *
from tttlogic import *
from tkinter import *

canvas = getcanvas()
screen = getscreen()

def clearScreen():
    clear()
    initialize_board()
    penup()
    setheading(0)
    setpos(0,0)
    tracer(0)
    speed(10)
    hideturtle()
    pensize(10)
    pendown()
    drawgrid()
    penup()
    update()
    turne()

def popupmsg1(msg,ttl):
    NORM_FONT = ("Helvetica", 10)
    popup = Tk()
    popup.wm_title(ttl)
    popup.minsize(width=300, height=80)
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side=TOP, fill="x", pady=10)
    B1 = Button(popup, text = "Okay", command = popup.destroy)
    B1.pack(side=BOTTOM)
    popup.mainloop()

def popupmsg2(wnr):
    if wnr == "X":
        msg = "Congratulations, X is the winner!!! Do you want to Play Again?"
        ttl = "Game Over - X Wins!!!"
    elif wnr == "O":
        msg = "Congratulations, O is the winner!!! Do you want to Play Again?"
        ttl = "Game Over - O Wins!!!"
    elif wnr == "Draw":
        msg = "It's a Draw, Folks... Do you want to Play Again?"
        ttl = "Game Over - Draw"
    if messagebox.askyesno(ttl, msg, default="no"):
        clearScreen()
    else:
        bye()

def winner():
    if current_player() == "X":
        return "O"
    elif current_player() == "O":
        return "X"

def mouse_clickedx(x, y): #This puts the x and y values from the mouse being clicked through to the drawX function.
    square = point_to_square(x, y)
    drawX(square)

def mouse_clickedo(x, y): #This puts the x and y values from the mouse being clicked through to the drawO function.
    square = point_to_square(x, y)
    drawO(square)

def turne():
    if current_player() == "X":
        turnx()
    elif current_player() == "O":
        turno()
    drawline(check_status()[1])

def turnx(): #Defines X as the active player.
    pensize(10)
    canvas.config(cursor = "X_cursor")
    screen.onscreenclick(mouse_clickedx)
    title("Tic-Tac-Toe - X's Turn")
    penup()
    setpos(-320, 280)
    pensize(18)
    setheading(0)
    pencolor("white")
    pendown()
    forward(600)
    penup()
    setpos(-320, 270)
    pencolor("blue")
    write("It is X's turn.", False, align="left", font=("Times New Roman", 12, "bold"))
    #drawline(check_status())

def turno(): #Defines O as the active player.
    pensize(10)
    canvas.config(cursor = "circle")
    screen.onscreenclick(mouse_clickedo)
    title("Tic-Tac-Toe - O's Turn")
    penup()
    setpos(-320, 280)
    pensize(18)
    setheading(0)
    pencolor("white")
    pendown()
    forward(600)
    penup()
    setpos(-320, 270)
    pencolor("red")
    write("It is O's turn.", False, align="left", font=("Times New Roman", 12, "bold"))
    #drawline(check_status())

def drawgrid(): #This draws the grid
    #Left vertical line
    penup()
    setpos(-83, 250)
    pendown()
    right(90)
    forward (500)

    #Right vertical line
    penup()
    setpos(83, 250)
    pendown()
    forward (500)

    #Top horzontial line
    penup()
    setpos(-250, 83)
    pendown()
    left(90)
    forward (500)

    #Bottem horzontial line
    penup()
    setpos(-250, -83)
    pendown()
    forward (500)

def point_to_square(x, y): #This changes the point to a square
    if x <= -83 and x >= -250 and y >= 83 and y <= 250:
        return "NorthWest"
    elif x >= -82 and x <= 83 and y >= 83 and y <= 250:
        return "North"
    elif x >= 84 and x <= 250 and y >= 83 and y <= 250:
        return "NorthEast"
    elif x <= -83 and x >= -250 and y >= -83 and y <= 82:
        return "West"
    elif x >= -82 and x <= 83 and y >= -83 and y <= 82:
        return "Center"
    elif x >= 84 and x <= 250 and y >= -83 and y <= 82:
        return "East"
    elif x <= -83 and x >= -250 and y >= -250 and y <= -84:
        return "SouthWest"
    elif x >= -82 and x <= 83 and y >= -250 and y <= -84:
        return "South"
    elif x >= 84 and x <= 250 and y >= -250 and y <= -84:
        return "SouthEast"

def square_to_point(s): #This changes the square to a point
    if s == "NorthWest":
        x = 167
        y = 167
        
    elif s == "North":
        x = 0
        y = 167
        
    elif s == "NorthEast":
        x = -167
        y = 167
        
    elif s == "West":
        x = 167
        y = 0
        
    elif s == "Center":
        x = 0
        y = 0
        
    elif s == "East":
        x = -167
        y = 0
        
    elif s == "SouthWest":
        x = 167
        y = -167
        
    elif s == "South":
        x = 0
        y = -167

    elif s == "SouthEast":
        x = -167
        y = -167
    return x, y

def drawX(s): #This draws an x on a square
    pencolor("blue")
    penup()
    pensize(10)
    if move(s) is True:
        if s == "NorthWest":
            setpos(-240, 240)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(-93, 240)
            pendown()
            setheading(225)
            forward(205)
        elif s == "North":
            setpos(-73, 240)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(73, 240)
            pendown()
            setheading(225)
            forward(205)
        elif s == "NorthEast":
            setpos(93, 240)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(240, 240)
            pendown()
            setheading(225)
            forward(205)
        elif s == "West":
            setpos(-240, 73)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(-93, 73)
            pendown()
            setheading(225)
            forward(205)
        elif s == "Center":
            setpos(-73, 73)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(73, 73)
            pendown()
            setheading(225)
            forward(205)
        elif s == "East":
            setpos(93, 73)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(240, 73)
            pendown()
            setheading(225)
            forward(205)
        elif s == "SouthWest":
            setpos(-240, -93)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(-93, -93)
            pendown()
            setheading(225)
            forward(205)
        elif s == "South":
            setpos(-73, -93)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(73, -93)
            pendown()
            setheading(225)
            forward(205)
        elif s == "SouthEast":
            setpos(93, -93)
            pendown()
            setheading(315)
            forward(205)
            penup()
            setpos(240, -93)
            pendown()
            setheading(225)
            forward(205)
    elif move(s) is not True:
        popupmsg1("That is an incorrect move, please try again.", "ERROR!!!")
    update()
    turne()

def drawO(s): #This draws a O centered on a point (centered in a square)
    pencolor("red")
    penup()
    pensize(10)
    setheading(0)
    if move(s) is True:
        if s == "NorthWest":
            setpos(-167, 93)
            pendown()
            circle(73)
        elif s == "North":
            setpos(0, 93)
            pendown()
            circle(73)
        elif s == "NorthEast":
            setpos(167, 93)
            pendown()
            circle(73)
        elif s == "West":
            setpos(-167, -73)
            pendown()
            circle(73)
        elif s == "Center":
            setpos(0, -73)
            pendown()
            circle(73)
        elif s == "East":
            setpos(167, -73)
            pendown()
            circle(73)
        elif s == "SouthWest":
            setpos(-167, -238)
            pendown()
            circle(73)
        elif s == "South":
            setpos(0, -238)
            pendown()
            circle(73)
        elif s == "SouthEast":
            setpos(167, -238)
            pendown()
            circle(73)
    elif move(s) is not True:
        popupmsg1("That is an incorrect move, please try again.", "ERROR!!!")
    update()
    turne()

def drawline(s):
    pencolor("black")
    pensize(25)
    if s == "Win_NW_SE":
        setpos(-250, 250)
        pendown()
        setheading(315)
        forward(707)
        penup()
        popupmsg2(winner())
    elif s == "Win_NE_SW":
        setpos(250, 250)
        pendown()
        setheading(225)
        forward(707)
        penup()
        popupmsg2(winner())
    elif s == "Win_NW_NE":
        setpos(-250, 157)
        pendown()
        setheading(0)
        forward(500)
        penup()
        popupmsg2(winner())
    elif s == "Win_W_E":
        setpos(-250, 0)
        pendown()
        setheading(0)
        forward(500)
        penup()
        popupmsg2(winner())
    elif s == "Win_SW_SE":
        setpos(-250, -157)
        pendown()
        setheading(0)
        forward(500)
        penup()
        popupmsg2(winner())
    elif s == "Win_NW_SW":
        setpos(-157, 250)
        pendown()
        setheading(270)
        forward(500)
        penup()
        popupmsg2(winner())
    elif s == "Win_N_S":
        setpos(0, 250)
        pendown()
        setheading(270)
        forward(500)
        penup()
        popupmsg2(winner())
    elif s == "Win_NE_SE":
        setpos(157, 250)
        pendown()
        setheading(270)
        forward(500)
        penup()
        popupmsg2(winner())
    elif s == "Draw":
        popupmsg2("Draw")
    else:
        pass


#This defines some basic stuff
title("Tic-Tac-Toe")
tracer(0)
speed(10)
hideturtle()
pensize(10)
screen.screensize(260, 260)

#This draws the main grid
drawgrid()
penup()
'''
#setpos(-320, 270)
#pencolor("black")
#write("Press the 'x' or the 'o' key on your keyboard to select the current game-piece.", False, align="left", font=("Times New Roman", 12, "bold"))
'''
update()

'''
#This allows the user to switch who is playing by pressing the x and o keys
#screen.onkeyrelease(turnx, "x")
#screen.listen()
#screen.onkeyrelease(turno, "o")
#screen.listen()
'''

turne()

mainloop() #This should let it keep going, I think....