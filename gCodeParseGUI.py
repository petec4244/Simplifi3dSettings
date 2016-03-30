import sys
import string
import time
import csv
import os
import os.path
from tkinter import *
import tkinter.constants as Tkconstants
import tkinter.filedialog as tkFileDialog
from tkinter import ttk
import simpenums as Enu
import GUInotebook as NB

def ReadGcode(File1, File2, outfile):
	File1 = File1.get()
	File2 = File2.get()
	LastLine = 185 #where the actual Gcode begins. 
	startTime = time.time()
	writeToLog("F1 = " + str(File1) + "\nF2 = "+ str(File2)+"\nOutput File = " + outfile+"\n");
	with open(File1) as myFile1:
		with open(File2) as myFile2:
			readLines1 = myFile1.readlines()[0:LastLine]
			readLines2 = myFile2.readlines()[0:LastLine]
			for i in range(len(readLines1)):
				if(readLines1[i] != readLines2[i]):
					writeToLog("F1-LINE["+str(i)+"] " + readLines1[i] +"F2-LINE["+str(i)+"] " + readLines2[i])
	elapsedTime = time.time() - startTime
	m, s = divmod(elapsedTime, 60)
	h, m = divmod(m, 60)
	writeToLog("The operations took: %02d:%02d:%02d (H:M:S)" % (h, m, s))
	writeToLog("Finished!")
	

def mainRead(File1, File2, outFile):
	ReadGcode(File1, File2, outFile)
	
def askopenfilename(fileNum, *args):
	filename = tkFileDialog.askopenfilename(**NB.file_opt)
	if filename:
		if(fileNum == 0):
			File1.set(filename)
		if(fileNum == 1):
			File2.set(filename)
		

def asksaveasfilename():
	filename = tkFileDialog.asksaveasfilename(**NB.file_opt)
	if filename:
		return open(filename, 'w')

def writeToLog(msg):
	numlines= log.index('end - 1 line').split('.')[0]
	log['state']='normal'
	if numlines == 200:
		log.delete(1.0, 2.0)
	if log.index('end-1c')!='1.0':
		log.insert('end', '\n')
	log.insert('end', msg)
	log['state'] = 'disabled'
	log.yview(END)
	
def LookupEnum(type, refNum):
	refNum = int(refNum)
	if(type == 1): #tab
		if refNum < len(Enu.TabEnum):
			write(str(Enu.TabEnum(refNum)))
		else:
			write('Not found Max:' + str(len(Enu.TabEnum)-1))
	else: #label
		write(Enu.LineNames.get(refNum, 'Number not defined'))
	
if __name__ == "__main__":
	def write(x): writeToLog(x)
	root = Tk()
	root.title("Simplify3d gCode")
	note = NB.Notebook(root, width= 800, height =700, activefg = 'Gray', inactivefg = 'black')
	note.grid()
	
	#StringVars - This is going to be brutally ugly until I figure out a better way of doing things.
	# so much copy past I know I am doing something wrong. 
	File1 = StringVar()
	File2 = StringVar()
	outFile = ""
	
	#tab12 
	tab12 = note.add_tab(text = "Settings")
	pt12 = NB.add_Pane(tab12)
	fr12 = NB.add_LblFrame(pt12, "File Selections")
	fr12_1 = NB.add_LblFrame(pt12, "Other Options")
	fr12_2 = NB.add_LblFrame(pt12, "Console")
	
	NB.LblTV(fr12, File1, 2, 2, W)
	NB.LblTV(fr12, File2, 2, 3, W)
	
	Button(fr12, text="Open File 2", command=(lambda:askopenfilename(1))).grid(column=1, row=3, sticky=(W))
	Button(fr12, text="Open File 1", command=(lambda:askopenfilename(0))).grid(column=1, row=2, sticky=(W))
	
	
	Label(fr12_1, text="Lookup what Line/Enum#?", bg="white", fg = "blue").grid(column=1, row=5, sticky=(W))
	txt = Text(fr12_1, width=50, height=2)
	txt.focus()
	txt.grid(column=2, row=5, sticky=(W))

	Button(fr12_1, text="Get Tab", command=(lambda: LookupEnum(1, txt.get('1.0', END)))).grid(column=1, row=6, sticky=(W))
	Button(fr12_1, text="Get Field", command=(lambda: LookupEnum(2, txt.get('1.0', END)))).grid(column=2, row=6, sticky=(W))
	
	Button(fr12, text="Run Files", command=(lambda: mainRead(File1, File2, outFile))).grid(column=1, row=4, sticky=(W))
	Button(fr12, text="EXIT", command=(lambda: sys.exit())).grid(column=1, row=8, sticky=(W, E))
	
	log = Text(fr12_2, state='disabled')#.grid(column=2, row=3, sticky=(W))
	log.grid(column=1, row=1, sticky=(N,W))
	
	lastNum=0
	lastLabel = 185
	for i in Enu.TabEnum:
		numLabels = 0
		switchNum = 0 	#the number where we switch to the next Tab
		addedLabels = 0 # how we know what row to add the field to.
		columnCount = 1 #Keep track of how many entries per column we want. 
		
		strTabname = i
		TabAdded = note.add_tab(text= strTabname)
# m1 = NB.add_Pane(tab1, VERTICAL) #add the pane
# f1 = NB.add_LblFrame(m1, "Overview") # add the frame		
		
		Name = str(i)
		for j in Enu.tabSwitchName:
			tabname_L = str(j)
			if(Name == tabname_L):
				switchNum = Enu.tabSwitchName.get(j)
				break
		numLabels = switchNum - lastNum
		for jk in Enu.LineNames:
			LineTitle_S = str(Enu.LineNames.get(jk))
			if(addedLabels % 30 == 0):
				columnCount = columnCount + 2
				addedLabels = 0
			if jk <= switchNum:
				if jk > lastNum:		
					NB.Lbl(TabAdded, LineTitle_S, columnCount, addedLabels, (W))
					addedLabels = addedLabels + 1
					if jk == switchNum:
						lastNum = switchNum
	note.focus_on(tab12)
	root.mainloop()
