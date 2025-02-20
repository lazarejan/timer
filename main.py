from tkinter import *
from datetime import datetime

temp = 0
after_id = None

def tick():
    global temp, after_id

    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text = str(f_temp))
    temp += 1
    after_id = window.after(1000, tick)

def start_timer():
    if after_id:
        return None
    tick()

def stop_timer():
    stop_btn.grid_forget()
    start_btn.grid_forget()

    cont_btn.grid(row = 1, column = 0, sticky = 'ew')
    reset_btn.grid(row = 1, column = 1, sticky = 'ew')

    window.after_cancel(after_id)

window = Tk()

window.title('timer')

label1 = Label(window, width= 5, font = ('Verdana', 80), text = "00:00")
label1.grid(row = 0, columnspan = 2)

start_btn = Button(window, text = "Start", font = ('Verdana', 20), command = start_timer)
start_btn.grid(row = 1, column = 0, sticky = 'ew')

stop_btn = Button(window, text = "Stop", font = ('Verdana', 20), command = stop_timer)
stop_btn.grid(row = 1, column = 1, sticky = 'ew')

cont_btn = Button(window, text = "Continue", font = ('Verdana', 20), width= 6)

reset_btn = Button(window, text = "Reset", font = ('Verdana', 20))

window.mainloop()