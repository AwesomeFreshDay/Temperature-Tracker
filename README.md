# Temperature-Tracker
# *CURRENTLY WORK IN PROGRESS NOT FINSIHED*
Are you tired of using hardware monitor apps on Windows that are complicated and and sophisticated to navigate? Welcome to the program Temperature Tracker that tracks and monitors your Windows Computer’s usage and temperatures in an easy to navigate and simple environment.

# Features 
-
-
- Lock your temperature cap before the program notifies you a warning that you reached that temperature keeping your system aware and safe
- Temperature tracker that shows your stats every certain number of minutes

# Installation
- This program needs to be run in administrator to work properly because of WinTMP requiring privileges to read hardware temperatures. You can run without administrator but you wouldn’t be able to see temps
- WINDOWS support only for now. This program natively supports and runs on Windows 10/11. 

# Prerequisite 
- (I think you might need it I’m not sure but it probably works without just a guess but if the program doesn’t work install this .NET 10.0 Framework
https://dotnet.microsoft.com/en-us/download/dotnet/10.0
- I think you might need to go to the folder installation right click both DLL files and click unblock I’m not sure again because I did that on my side but just double checking 

# Additional Information
- I am aware that the program is a little laggy and sometimes freezes this is due to the WinTmp library gathering hall sensor temperature or something from the computer which takes a while to load and gather so the program lags and freezes a little I put the library to load within threading to reduce the lag to the best of my ability so far if there are any tips I would be happy to take them 




# Credits/Achknowledgements
Python
psutul library - gathers cpu and ram usage
WinTmp Library - gathers cpu and gpu temperatures 
LibreHardware Monitor DLL file

