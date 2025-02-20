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



window = Tk()

window.title('timer')

label1 = Label(window, width= 5, font = ('Verdana', 80), text = "00:00")
label1.grid(row = 0, columnspan = 2)

start_btn = Button(window, text = "Start", font = ('Verdana', 20), command = start_timer)
start_btn.grid(row = 1, column = 0, sticky = 'ew')

stop_btn = Button(window, text = "Stop", font = ('Verdana', 20))
stop_btn.grid(row = 1, column = 1, sticky = 'ew')

window.mainloop()