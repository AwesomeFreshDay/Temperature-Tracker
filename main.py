import psutil
import time
import os
from datetime import datetime
import WinTmp

now = datetime.now()
current_time = now.time()

print("Temperature Tracker")
print("-------------------")

while True: 
    os.system("cls")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent


    print(f"CPU Usage: {cpu}%")
    print(f"Ram Usage: {ram}%")
    print(f"CPU Temp: {WinTmp.CPU_Temp()} °C")
    print(f"GPU Temp: {WinTmp.GPU_Temp()} °C")
    print(now.strftime("%I:%M %p"))
    
    time.sleep(3)