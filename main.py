import psutil
import time
import os
from datetime import datetime
import WinTmp
import csv
from tkinter import *
from tkinter import messagebox

now = datetime.now()
current_time = now.time()

window = Tk()
window.title('Temperature Tracker')
window.geometry('400x400')

# Update CPU Usage after 1 second

def update_cpu_usage():
    cputest = psutil.cpu_percent(interval=None)
    cpu_label['text'] = f"CPU Usage: {cputest}%"

cpu_label = Label(window)
cpu_label.pack()


# Update CPU Temp after 1 second
def update_cpu_temp():
    cpu_temp = WinTmp.CPU_Temp()
    cpu_temp_label['text'] = f"CPU Temp: {cpu_temp}° C"

cpu_temp_label = Label(window)
cpu_temp_label.pack()


# Update GPU temp after 1 second

def update_gpu_temp():
    gpu_temp = WinTmp.GPU_Temp()
    gpu_temp_label['text'] = f"GPU Temp: {gpu_temp}° C"

gpu_temp_label = Label(window)
gpu_temp_label.pack()


# Update ram usage after 1 second

def update_ram_usage():
    ram_usage = psutil.virtual_memory().percent
    ram_usage_label['text'] = f"Ram Usage: {ram_usage}%"

ram_usage_label = Label(window)
ram_usage_label.pack()


# Update disk usage after 1 second

def update_time_clock():
    time_clock = now.strftime("%I:%M:%S %p")
    time_clock_label['text'] = time_clock

time_clock_label = Label(window)
time_clock_label.pack()


def update_hardware_monitor():
    window.after(1000, update_hardware_monitor)
    update_cpu_usage()
    update_cpu_temp()
    update_gpu_temp()
    update_ram_usage()
    update_time_clock()

# Update all hardware monitor after 1 second passed
update_hardware_monitor()


def message():
    messagebox.showinfo("Test", "Simple messagebox")

btn = Button(window, text="Simple button", command=message)
btn.pack()
# Function to validate integer input
# This was made possible with this guide to block letters and special characters input
# https://www.tutorialkart.com/python/tkinter/how-to-allow-only-integer-in-entry-widget-in-tkinter-python/
# Limit characters counted for to 3 or less
def validate_input(P):
    if P == "" or (P.isdigit and len(P) <= 3):
        return True
    return False

# Register validation function
vcmd = window.register(validate_input)

# String variable to store temperature cap
temp_cap = StringVar()

# Function to get temperature input and store on screen

def submit():
    temp = temp_cap.get()
    print(f"The temperature is {temp}")
    if int(temp) > 120:
        print("ok")
        messagebox.showinfo("Tempearture", "Temperature cannot be higher than 120, choose a different value")
        

# Create a label for the user to type in
temp_label = Label(window, text = 'Temp Cap ° C')
temp_label.pack()

# Create entry for the label input to send its data to the terminal
temp_entry = Entry(window, textvariable = temp_cap, validate="key", validatecommand=(vcmd, "%P"))
temp_entry.pack()

# Create submit button to submit function
set_btn = Button(window, text = 'Set Temperature', command = submit)
set_btn.pack()






window.mainloop()
"""


print("Temperature Tracker")
print("-------------------")

monitor_list = []


while True: 
    os.system("cls")
    cpu = psutil.cpu_percent(interval=1)
    
    
    
    
    monitor_list.extend([cpu, ram, cpu_temp, gpu_temp, the_time])


    print(f"CPU Usage: {cpu}%")
    print(f"Ram Usage: {ram}%")
    print(f"CPU Temp: {cpu_temp} °C")
    print(f"GPU Temp: {gpu_temp} °C")
    print(the_time)
    print(*monitor_list, sep=", ")
    
    time.sleep(3)
    """