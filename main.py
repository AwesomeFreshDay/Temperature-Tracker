import psutil
import time
import os

print("Temperature Tracker")
print("-------------------")

while True: 
    os.system("cls")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent


    print(f"CPU Usage: {cpu}%")
    print(f"Ram Usage: {ram}%")
    time.sleep(3)