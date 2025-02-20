from tkinter import *

window = Tk()

window.title('timer')

label1 = Label(window, width= 5, font = ('Verdana', 80), text = "00:00")
label1.grid(row = 0, columnspan = 2)

window.mainloop()