from tkinter import *
from datetime import datetime


def replace_btns(frgt1, frgt2, grid1, grid2):
    def outter(func):
        def wrapper():
            # if func() == "False":
            #     return
            frgt1.grid_forget()
            frgt2.grid_forget()

            grid1.grid(row = 1, column = 0, sticky = 'ew')
            grid2.grid(row = 1, column = 1, sticky = 'ew')

            return func()
        return wrapper
    return outter


window = Tk()

window.title('timer')

label1 = Label(window, width= 5, font = ('Verdana', 80), text = "00:00")
label1.grid(row = 0, columnspan = 2)

start_btn = Button(window, text = "Start", font = ('Verdana', 20))
start_btn.grid(row = 1, column = 0, sticky = 'ew')

stop_btn = Button(window, text = "Stop", font = ('Verdana', 20))
stop_btn.grid(row = 1, column = 1, sticky = 'ew')

cont_btn = Button(window, text = "Continue", font = ('Verdana', 20), width= 6)

reset_btn = Button(window, text = "Reset", font = ('Verdana', 20))

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

@replace_btns(stop_btn, start_btn, cont_btn, reset_btn)
def stop_timer():
    if after_id:
        window.after_cancel(after_id)
    #     return
    # return "False"

@replace_btns(cont_btn, reset_btn, start_btn, stop_btn)
def cont_timer():
    tick()

@replace_btns(cont_btn, reset_btn, start_btn, stop_btn)
def reset_timer():
    global temp, after_id
    temp = 0
    label1.config(text = "00:00")
    window.after_cancel(after_id)
    after_id = None


start_btn.config(command = start_timer)
stop_btn.config(command = stop_timer)
cont_btn.config(command = cont_timer)
reset_btn.config(command = reset_timer)

window.mainloop()