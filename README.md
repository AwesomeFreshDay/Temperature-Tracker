# Temperature-Tracker
Are you tired of using hardware monitor apps on Windows that are complicated and and sophisticated to navigate? Welcome to the program Temperature Tracker that tracks and monitors your Windows Computer’s usage and temperatures in an easy to navigate and simple environment.

# Features 
- Provides computer statistics such as CPU Usage, GPU Temp, Ram Usage, Time, and 2 sliders for capping CPU + GPU Temp that notifies with a messagebox whenever the temp has been reached
- Lock your temperature cap before the program notifies you a warning that you reached that temperature keeping your system aware and safe
- Temperature tracker that shows your stats every certain number of minutes
- Dark mode/light mode

# Installation
# READ THIS IF YOU ARE RUNNING THIS PROGRAM FROM THE TERMINAL
1. Run the terminal as admistrator(important or an error will throw when launching the program
2. git clone https://github.com/AwesomeFreshDay/Temperature-Tracker.git
3. cd temperature-tracker
4. py -m pip install -r requirements.txt
5. py main.py

# Exe installation
- Download the setup file and  proceed through installation and an exe launchable file will be added to your computer https://github.com/AwesomeFreshDay/Temperature-Tracker/releases/tag/v1.0
- THIS PROGRAM NEEDS IT NEEDS to be run in ADMISTRATOR to launch because WinTMP requires administrator privileges to read hardware hall sensor temperatures.

# If errors occur 
- This program can be run in a VM(Virtual Machine) or any computer with unreadable temperatures but cpu and gpu temp will show as none. Every other feature besides temp will continue to work.
- Windows defender may mark the program as a false positive for some people if this happens turn it off temporarily
- WINDOWS support only for now. This program natively supports and runs on Windows 10/11. 

# Prerequisite 
- (I think you might need it I’m not sure but it probably works without just a guess but if the program doesn’t work install this .NET 10.0 Framework
https://dotnet.microsoft.com/en-us/download/dotnet/10.0


# Additional Information
- I am aware that the program is a little laggy and sometimes freezes this is due to the WinTmp library gathering hall sensor temperature or something from the computer which takes a while to load and gather so the program lags and freezes a little I put the library to load within threading to reduce the lag to the best of my ability so far if there are any tips I would be happy to take them
- When you install the installer and at the end of it check mark the launch program to run it, it will not runt he program but display an error message because it is not automatically run in administrator mode.

# Credits/Achknowledgements
Python and its built in libraries, threading, time, and tkinter
Customtkinter for GUI
psutul library - gathers cpu and ram usage
WinTmp Library - gathers cpu and gpu temperatures from LibreHardware Monitor DLL file + RAMSPDToolkit-NDD.dll

