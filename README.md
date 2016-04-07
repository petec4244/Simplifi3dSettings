# Simplifi3dSettings

I'm tired of manually going through Old gcode and comparing what worked or what didn't. 
The goal of this project is to create a quick and easy to use program to show the difference in settings between 2 Simplify3d Gcode files, without any external comparison software like BeyondCompare.

Basically, I'm making it for me, if you can use it too great! Enjoy!


##Requirments 

Python 3.4 or greater - because I use enum in the GUI
If you dont have 3.4 you may be able to use the CMD version

##Usage

Run gCodeParseGUI.py in python, select the 2 s3d gcode files to compare then press the "Compare the Files" button.
The script will add new tabs named alike the S3d Settings, anything that differs will appear in red. 
