import psutil
import time
import os
from datetime import datetime
import WinTmp
import csv
from tkinter import *
from tkinter import messagebox


window = Tk()
window.title('Simple Desktop app')
window.geometry('400x400')

def update_cpu_usage():
    cputest = psutil.cpu_percent(interval=None)
    cpu_label['text'] = f"CPU Usage: {cputest}"
    window.after(1000, update_cpu_usage)


def message():
    messagebox.showinfo("Test", "Simple messagebox")

cpu_label = Label(window)
cpu_label.pack()
update_cpu_usage()

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