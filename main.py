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

# Create tabview
my_tab = customtkinter.CTkTabview(window,corner_radius=20, width=600,height=250)
my_tab.pack()

# Create tabs

tab_1 = my_tab.add("Main")
tab_2 = my_tab.add("Temperature Tracker")

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
cpu_label = customtkinter.CTkLabel(master=tab_1, text="Editable text")
cpu_label.pack()

cpu_temp_label = customtkinter.CTkLabel(master=tab_1, text="")
cpu_temp_label.pack()

gpu_temp_label = customtkinter.CTkLabel(master=tab_1, text="")
gpu_temp_label.pack()

# Update ram usage after 1 second
ram_usage_label = customtkinter.CTkLabel(master=tab_1, text="")
ram_usage_label.pack()

# Update the clock every second
time_clock_label = customtkinter.CTkLabel(master=tab_1, text="")
time_clock_label.pack()

# Start only one background thread
    # Run temps in background
threading.Thread(target=get_temps, daemon=True).start()

def message():
    messagebox.showinfo("Test", "Simple messagebox")

btn = Button(tab_1, text="Simple button", command=message)
btn.pack()

cpu_temp_slider_label = customtkinter.CTkLabel(tab_1, text="CPU Temperature Cap:")
cpu_temp_slider_label.pack()
# Function to input value the user puts & Function to reset while_running back to false
def sliding(value):
    temp_slider_label.configure(text=f"{int(value)} ° C")
    global while_cpu_running
    while_cpu_running = False

# Define starting point for obtaining cpu temp

slider = customtkinter.CTkSlider(master=tab_1, from_=30, to=120, progress_color="#2f5694", command=sliding)
slider.set(80)
temp_slider_label = customtkinter.CTkLabel(tab_1, text=f"{slider.get()} ° C")
slider.pack()
temp_slider_label.pack()

# Label gpu
gpu_temp_slider_label = customtkinter.CTkLabel(tab_1, text="GPU Temperature Cap:")
gpu_temp_slider_label.pack()

# Store value for the gpu this time
def sliding_gpu(value):
    gpu_slider_label.configure(text=f"{int(value)} ° C")
    global while_gpu_running
    while_gpu_running = False

# slider for the gpu this time

gpu_slider = customtkinter.CTkSlider(master=tab_1, from_=30, to=120, progress_color="#f05d5d", command=sliding_gpu)
gpu_slider.set(80)
gpu_slider_label = customtkinter.CTkLabel(tab_1, text=f"{gpu_slider.get()} ° C")
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
           messagebox.showwarning("WARNING", f"CPU temperature cap exceeded! CPU: {cpu_temp}°C | Cap: {temp}°C")
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
        messagebox.showwarning("WARNING", f"GPU temperature cap exceeded! GPU: {gpu_temp}°C | Cap: {temp}°C")
    window.after(1000, show_gpu_data)
     
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

# Tab 2
# Creating temperature tracker
#def temperature_tracker():
    #while True:
        #minutes = int(dropdown_box.get())

def time_picker():
    unconverted_numbers = dropdown_box.get()
    # Convert string to number
    string_number = int(unconverted_numbers.split()[0])
    if "seconds" in unconverted_numbers:
        milliseconds = string_number * 1000
    else: 
        # If it dont contain seconds, its minute so multiply along with 60
        milliseconds = string_number * 60 * 1000
    print(milliseconds)
    frame.after(milliseconds, add_another_row)
    return milliseconds
    
#print(
    #f"Time: {time_clock} | Cpu_usage: {cpu_usage} | Cpu_temp: {cpu_temp} | gpu_temp: {gpu_temp} | ram_usage: {ram_usage}")



time_selection = ["10 seconds", "5 minutes", "10 minutes", "15 minutes", "20 minutes"]
dropdown_box = customtkinter.CTkComboBox(tab_2, values=time_selection)
dropdown_box.pack()
set_time_button = customtkinter.CTkButton(tab_2, text="Set time", command=time_picker)
set_time_button.pack()

# Make the frame
frame = customtkinter.CTkFrame(tab_2, width=450, height=245, fg_color="#8D6F3A", border_color="#FFCC70")
frame.pack()
frame.grid_propagate(False)

# The stats on the top
time_frame_label = customtkinter.CTkLabel(frame, text="Time")
time_frame_label.grid(row=0, column=1, padx=8)
cpu_usage_frame_label = customtkinter.CTkLabel(frame, text="CPU Usage")
cpu_usage_frame_label.grid(row=0, column=2, padx=8)
cpu_temp_frame_label = customtkinter.CTkLabel(frame, text="CPU °C")
cpu_temp_frame_label.grid(row=0, column=3, padx=8)
gpu_temp_frame_label = customtkinter.CTkLabel(frame, text="GPU °C")
gpu_temp_frame_label.grid(row=0, column=4, padx=8)
ram_usage_frame_label = customtkinter.CTkLabel(frame, text="Ram Usage")
ram_usage_frame_label.grid(row=0, column=5, padx=8)

nextrow = 1
count = 0

def add_another_row():
    global nextrow
    global count
    # Run our function time picker and put what it gives to miliseconds variable
    milliseconds = time_picker()
    if count > 2:
        return
    now = datetime.now()
    time_clock = now.strftime("%I:%M:%S %p")
    cpu_usage = psutil.cpu_percent(interval=None) 
    cpu_temp = WinTmp.CPU_Temp()
    gpu_temp = WinTmp.GPU_Temp()
    ram_usage = psutil.virtual_memory().percent
    # Now need to add the text on the bottom column
    time_frame = customtkinter.CTkLabel(frame, text=time_clock)
    time_frame.grid(row=nextrow, column=1, padx=8)
    cpu_usage_frame = customtkinter.CTkLabel(frame, text=cpu_usage)
    cpu_usage_frame.grid(row=nextrow, column=2, padx=8)
    cpu_temp_frame = customtkinter.CTkLabel(frame, text=cpu_temp)
    cpu_temp_frame.grid(row=nextrow, column=3, padx=8)
    gpu_temp_frame = customtkinter.CTkLabel(frame, text=gpu_temp)
    gpu_temp_frame.grid(row=nextrow, column=4, padx=8)
    ram_usage_frame = customtkinter.CTkLabel(frame, text=ram_usage)
    ram_usage_frame.grid(row=nextrow, column=5, padx=8)
    nextrow += 1
    #count +=1
    
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