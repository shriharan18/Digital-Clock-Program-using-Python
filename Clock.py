import time
from tkinter import *

canvas = Tk()
canvas.title("Digital Clock by Stark Intelligence")
canvas.geometry("250x100")
canvas.resizable(1,1)

label = Label(canvas, font = ("Courier", 30, 'bold'), bg = "black", fg = "yellow", bd = 30)
label.grid(row = 0, column = 1)

#creating a function for digitalclock
def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text = text_input)
    label.after(200, digitalclock)

digitalclock()
canvas.mainloop()