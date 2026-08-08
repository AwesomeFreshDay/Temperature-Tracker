import psutil
import time

print("Temperature Tracker")
print("-------------------")

while True: 
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent


    print(f"CPU Usage: {cpu}%")
    print(f"Ram Usage: {ram}%")
    time.sleep(3)