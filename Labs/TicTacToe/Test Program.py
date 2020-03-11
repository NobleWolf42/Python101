from tkinter import *
import turtle

def popupmsg2(msg,ttl):
    NORM_FONT = ("Helvetica", 10)
    popup = Tk()
    popup.wm_title(ttl)
    popup.minsize(width=300, height=80)
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side=TOP, fill="x", pady=10)
    B1 = Button(popup, text = "Okay", command = popup.destroy)
    B2 = Button(popup, text = "Replay", command = turtle.reset())
    B1.place(x=75, y=50)
    B2.place(x=175, y=50)
    popup.mainloop()

popupmsg2("hello","hello")