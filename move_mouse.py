import pyautogui as pyg
import time
import random
import os
import tkinter as tk
from threading import Thread
import configparser


def scan():
    width, height = pyg.size()    
    while True:
        if running == False:
            print("Stopped")
            break
        else:
            x = random.randint(0, width)
            y = random.randint(0, height)
            pyg.moveTo(x, y, duration=2)
            print("sleep for: %d min" %(timer))
            time.sleep(timer * 60)
            pyg.press('win')
        
def mouse_start():
    global running 
    running = True
    t = Thread(target=scan)
    t.start()

def mouse_stop():
    global running 
    running = False
    h = Thread(target=scan)
    h.start()
    
    ## write settings to file when click on stop
    settings['auto_start'] = auto_start
    settings['show_start_btn'] = show_start_btn
    settings['timer'] = str(timer)

    with open('config.ini', 'w') as f:
        config.write(f)
    f.close()



def set_timer():
    global timer
    timer = timer_entry.get()
    timer = float(timer)
    timer_entry.delete(0,"end")

def disable_enable_start_btn():
    global show_start_btn
    start_btn.config(state=tk.DISABLED if val_check.get() else tk.NORMAL)
    if val_check.get():
        show_start_btn = "False"
    else:
        show_start_btn = "True"

def check_settings_at_startup(auto_start, show_start_btn):
    if show_start_btn == "True":
        start_btn.config(state=tk.NORMAL)
        val_check.set(0)
    else:
        start_btn.config(state=tk.DISABLED)
        val_check.set(1)
        auto_start = "True"
        mouse_start()

## Settings
running = False


config = configparser.ConfigParser()
config.read('config.ini')
settings = config['settings']

auto_start = settings['auto_start']
show_start_btn = settings['show_start_btn']
timer = float(settings['timer'])

## GUI box
root = tk.Tk()
val_check = tk.IntVar(root)

root.geometry("600x200")
root.title("Click Start to move mouse")

frame = tk.Frame(root, width=300, height=400)
frame.grid(row=0, column=0)
# frame.pack()

start_btn = tk.Button(frame, text="Start",width=10, height=2, command=mouse_start) #.place(x=-10, y=60)
start_btn.grid(row=1, column=0, padx=15, pady=15)

timer_label = tk.Label(frame, text='Set timer in minutes') #.place(x=90,y=40)
timer_label.grid(row = 0, column=1)
timer_entry = tk.Entry(frame, width=10) #.place(x=105, y=80)
timer_entry.grid(row = 1, column = 1)
set_btn = tk.Button(frame, text='Set', width=10, command=set_timer) #.place(x=105, y=120)
set_btn.grid(row = 2, column = 1)
stop_btn = tk.Button(frame, text="Stop", width=10, height=2, fg="red", command=mouse_stop) #.place(x=220, y=60)
stop_btn.grid(row = 1, column = 2, padx=15, pady=15)

checkbox = tk.Checkbutton(frame, text='disable start button', variable=val_check, command=disable_enable_start_btn)
checkbox.grid(row=3, column=0)

info = tk.Label(frame, text='* Settings are saved when stopped')
info.grid(row=4, column=2)
info.config(font=("Courier", 6))

check_settings_at_startup(auto_start, show_start_btn)
root.mainloop()
