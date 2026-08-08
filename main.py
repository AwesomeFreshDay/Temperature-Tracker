import psutil
import time
import os
from datetime import datetime
import WinTmp
import csv

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
    # monitor_list.extend([cpu, ram, ])


    print(f"CPU Usage: {cpu}%")
    print(f"Ram Usage: {ram}%")
    print(f"CPU Temp: {cpu_temp} °C")
    print(f"GPU Temp: {gpu_temp} °C")
    print(now.strftime("%I:%M %p"))
    #print(*monitor_list, sep=", ")
    
    time.sleep(3)