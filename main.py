from tkinter import *

window = Tk()

window.title('timer')

label1 = Label(window, width= 5, font = ('Verdana', 80), text = "00:00")
label1.grid(row = 0, columnspan = 2)

start_btn = Button(window, text = "Start", font = ('Verdana', 20))
start_btn.grid(row = 1, column = 0, sticky = 'ew')

stop_btn = Button(window, text = "Stop", font = ('Verdana', 20))
stop_btn.grid(row = 1, column = 1, sticky = 'ew')

window.mainloop()