import psutil

print("Temperature Tracker")
print("-------------------")

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent


print(f"CPU Usage: {cpu}%")
print(f"Ram Usage: {ram}%")