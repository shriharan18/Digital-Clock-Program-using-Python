#this code was written by Shreeharan for the YouTube channel Stark Intelligence. Check out the video : https://youtu.be/eh3O7A8smdY
import time             #importing time
from tkinter import *   #importing tkinter

canvas = Tk()           #creating a window for clock
canvas.title("Digital Clock by Stark Intelligence")     #giving the title for the window
canvas.geometry("250x100")      #determine the size of the window
canvas.resizable(1,1)

label = Label(canvas, font = ("Courier", 30, 'bold'), bg = "black", fg = "yellow", bd = 30)     #we have used the font 'Courier'. You can use any one you want. You can use any colors as you want
label.grid(row = 0, column = 1)

#creating a function for digitalclock
def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text = text_input)
    label.after(200, digitalclock)

digitalclock()          #calling the function digitalclock()
canvas.mainloop()
