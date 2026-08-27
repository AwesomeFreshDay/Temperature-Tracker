import psutil
import time
import os
from datetime import datetime
import WinTmp
import csv
from tkinter import *
from tkinter import messagebox
import customtkinter
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
window = customtkinter.CTk()
window.title('Temperature Tracker')
window.geometry('400x400')
window.resizable(False, False)

# Create threading for temps to run in background of program to optimize/stop the lag
def get_temps():
 while True:
    cputest = psutil.cpu_percent(interval=None) 
    cpu_temp = WinTmp.CPU_Temp()
    gpu_temp = WinTmp.GPU_Temp()
    ram_usage = psutil.virtual_memory().percent
    now = datetime.now()
    time_clock = now.strftime("%I:%M:%S %p")
    # Immediately Give temps back to gui
    window.after(0, update_temps, cputest, cpu_temp, gpu_temp, ram_usage, time_clock) 
    time.sleep(1)

# We passed our temp values to the function and print them out
def update_temps(cputest, cpu_temp, gpu_temp, ram_usage, time_clock):
    # For the cpu usage for the program
    cpu_label.configure(text=f"CPU Usage: {cputest}%")

    # For the cpu temp for the program
    cpu_temp_label.configure(text=f"CPU Temp: {cpu_temp}° C")
    
    # Now for the gpu temp for the program
    gpu_temp_label.configure(text=f"GPU Temp: {gpu_temp}° C")

    # now for the ram
    ram_usage_label.configure(text=f"Ram Usage: {ram_usage}%")

    # For the clock
    time_clock_label.configure(text=time_clock)
    
# Update CPU Usage after 1 second
cpu_label = customtkinter.CTkLabel(master=window, text="Editable text")
cpu_label.pack()

cpu_temp_label = customtkinter.CTkLabel(master=window, text="")
cpu_temp_label.pack()

gpu_temp_label = customtkinter.CTkLabel(master=window, text="")
gpu_temp_label.pack()

# Update ram usage after 1 second
ram_usage_label = customtkinter.CTkLabel(master=window, text="")
ram_usage_label.pack()

# Update the clock every second
time_clock_label = customtkinter.CTkLabel(master=window, text="")
time_clock_label.pack()

# Start only one background thread
    # Run temps in background
threading.Thread(target=get_temps, daemon=True).start()

def message():
    messagebox.showinfo("Test", "Simple messagebox")

btn = Button(window, text="Simple button", command=message)
btn.pack()

cpu_temp_slider_label = customtkinter.CTkLabel(window, text="CPU Temperature Cap:")
cpu_temp_slider_label.pack()
# Function to input value the user puts & Function to reset while_running back to false
def sliding(value):
    temp_slider_label.configure(text=f"{int(value)} ° C")
    global while_cpu_running
    while_cpu_running = False

# Define starting point for obtaining cpu temp

slider = customtkinter.CTkSlider(master=window, from_=30, to=120, progress_color="#2f5694", command=sliding)
slider.set(80)
temp_slider_label = customtkinter.CTkLabel(window, text=f"{slider.get()} ° C")
slider.pack()
temp_slider_label.pack()

# Label gpu
gpu_temp_slider_label = customtkinter.CTkLabel(window, text="GPU Temperature Cap:")
gpu_temp_slider_label.pack()

# Store value for the gpu this time
def sliding_gpu(value):
    gpu_slider_label.configure(text=f"{int(value)} ° C")
    global while_gpu_running
    while_gpu_running = False

# slider for the gpu this time

gpu_slider = customtkinter.CTkSlider(master=window, from_=30, to=120, progress_color="#f05d5d", command=sliding_gpu)
gpu_slider.set(80)
gpu_slider_label = customtkinter.CTkLabel(window, text=f"{gpu_slider.get()} ° C")
gpu_slider.pack()
gpu_slider_label.pack()

# Boolean to send the messagebox only 1 time when they close the box until they change the value
while_cpu_running = False
while_gpu_running = False

# Function to get temperature input and store on screen for the cpu
def show_temp_data():
   global while_cpu_running
   cpu_temp = WinTmp.CPU_Temp()
   temp = int(slider.get())
   if cpu_temp > temp and while_cpu_running == False:
           while_cpu_running = True
           print("Hello")
           print(f"CPU: {cpu_temp}°C | Cap: {temp}°C")
           messagebox.showwarning("WARNING", "CPU temperature cap exceeded!")
   window.after(1000, show_temp_data)

show_temp_data()

# FUnction for gpu temp output

def show_gpu_data():
    global while_gpu_running
    gpu_temp = WinTmp.GPU_Temp()
    temp = int(gpu_slider.get())
    if gpu_temp > temp and while_gpu_running == False:
     while_gpu_running = True
     print(f"CPU: {gpu_temp}°C | Cap: {temp}°C")
     messagebox.showwarning("WARNING", "GPU temperature cap exceeded!")
window.after(1000, show_temp_data)
     
show_gpu_data()

# If switch is on set dark if its off put light
def switch_click():
    if switch_widget.get() == "on":
        customtkinter.set_appearance_mode("dark")
    if switch_widget.get() == "off":
        customtkinter.set_appearance_mode("light")
# 2 values given onvalue on and offvalue off and switch activates function
switch_widget = customtkinter.CTkSwitch(window, text="Dark Mode", onvalue="on", offvalue="off", command=switch_click)
# Switch position to bottom
switch_widget.place(x=10, y=365)
# Start with the switch already toggled on
switch_widget.select()



# MAKE SURE TO Create a seperate tab for temperature tracker next session 


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