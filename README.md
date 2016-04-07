# Simplifi3dSettings

I'm tired of manually going through Old gcode and comparing what worked or what didn't. 
The goal of this project is to create a quick and easy to use program to show the difference in settings between 2 Simplify3d Gcode files, without any external comparison software like BeyondCompare.

Basically, I'm making it for me, if you can use it too great! Enjoy!


##Requirments 

Python 3.4 or greater - because I use enum in the GUI
If you dont have 3.4 you may be able to use the CMD version

##Usage

Using python Run gCodeParseGUI.py select the 2 s3d gcode files to compare then press the "Compare the Files" button.
The script will add new tabs named alike the S3d Settings, anything that differs will appear in red. 

##example commands
if python 3.5 is installed @ C:\python35 
and the script is at C:\Simplifi3dSettings

To use the GUI at the command prompt type:
C:\python35\python.exe C:\Simplifi3dSettings\gCodeParseGUI.py

To use the Command prompt only version type:
C:\python35\python.exe C:\Simplifi3dSettings\gCodeParse_CMD.py [Full path+File to compare1] [Full path+File to compare2]

Note: It may help to enclose the paths and files with ""'s





