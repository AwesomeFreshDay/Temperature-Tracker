import psutil
import time
import os
from datetime import datetime
import WinTmp
import csv
from tkinter import *
from tkinter import messagebox
cputest = psutil.cpu_percent(interval=1)
window = Tk()
window.title('Simple Desktop app')
window.geometry('400x400')

# Initalize a Stringvar using after() to schedule updates without blocking the GUI
stringvar = StringVar()
stringvar.set("Click 'Start Count' to begin")

# Counter variable
count = 0

def update_label():
    global count 
    count += 1
    stringvar.set("Count up to: " + str(count))

def start_counting():
    global count
    count = 0
    update_label()

# Create a label widget
label = Label(window, textvariable=stringvar, font='Arial 17 bold')
label.pack(pady=20)

button = Button(window, text="Start Count", command=start_counting)
button.pack()

def message():
    messagebox.showinfo("Test", "Simple messagebox")

text = Label(window, text=f"Your CPU Usage is {cputest}")
text.pack()

btn = Button(window, text="Simple button", command=message)
btn.pack()

window.mainloop()
"""
now = datetime.now()
current_time = now.time()

print("Temperature Tracker")
print("-------------------")

monitor_list = []


while True: 
    os.system("cls")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    cpu_temp = WinTmp.CPU_Temp()
    gpu_temp = WinTmp.GPU_Temp()
    the_time = now.strftime("%I:%M %p")
    monitor_list.extend([cpu, ram, cpu_temp, gpu_temp, the_time])


    print(f"CPU Usage: {cpu}%")
    print(f"Ram Usage: {ram}%")
    print(f"CPU Temp: {cpu_temp} °C")
    print(f"GPU Temp: {gpu_temp} °C")
    print(the_time)
    print(*monitor_list, sep=", ")
    
    time.sleep(3)
    """