import os
from tkinter import *
import tkinter.constants as Tkconstants
import tkinter.filedialog as tkFileDialog
from tkinter import ttk

BASE = RAISED
SELECTED = FLAT

#Starting path for opening or saving files
rootPathFileOpts = os.environ["USERPROFILE"] +'\\Documents\\Python\\'

# define options for opening or saving a file type 1
file_opt = options = {}
options['defaultextension'] = '.gcode'
options['filetypes'] = [('all files', '.*'), ('Gcode files', '.gcode')]
options['initialdir'] = rootPathFileOpts
options['initialfile'] = 'myfile.gcode'
#options['parent'] = root
options['title'] = 'Open Gcode File'

# define options for opening or saving a file
save_opt = options = {}
options['defaultextension'] = '.txt'
options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
options['initialdir'] = rootPathFileOpts
options['initialfile'] = 'myfile.txt'
#options['parent'] = root
options['title'] = 'This is a title'

def add_Pane(tab):
	retPane = PanedWindow(tab, orient=VERTICAL, width=100, height=100)
	#retPane = PanedWindow(tab, orient=VERTICAL).grid(column=1, row=1, sticky = (W))
	retPane.pack(fill=BOTH, expand=0)
	return retPane
	
def add_Pane(tab):
	retPane = PanedWindow(tab, orient=VERTICAL, width=100, height=100)
	#retPane = PanedWindow(tab, orient=VERTICAL).grid(column=1, row=1, sticky = (W))
	retPane.pack(fill=BOTH, expand=0)
	return retPane

def add_PaneO(tab, orient):
	retPane = PanedWindow(tab, orient=orient)
	retPane.pack(fill=BOTH, expand=1)
	return retPane

def add_LblFrame(place, txt):
	retFrame = ttk.LabelFrame(place, text=txt, width=100, height=100)
	#retFrame = ttk.LabelFrame(place, text=txt).grid(column=1, row=1, sticky = (W))
	retFrame.pack(fill=BOTH, expand=0)
	return retFrame
	
# def addtoPlace(place, additem):
	# place.add(additem)
	
# def getGrid(col, rw, stcky):
	# grid = grid(column=col, row=row, sticky=(stcky))
	# return grid
	
#use default colors
def Lbl(place, txt, col, rw, stcky):
	#default colors
	newLabel = Label(place, text=txt, bg="LightGray", fg="black").grid(column=col, row=rw, sticky = (stcky))
	return newLabel
	
#provide Colors
def Lblc(place, txt, bgnd, fgrnd, col, rw, stcky):
	# if str(bgnd) == " ":
		# bgnd == "LightGray"
	# if str(fgrnd) == " ":
		# fgrnd = "black"
	newLabel = Label(place, text=txt, bg=bgnd, fg=fgrnd).grid(column=col, row=rw, sticky = (stcky))
	return newLabel
	
#addLabel with textVariable
def LblTV(place, txtVar, col, rw, stcky):
	newLabel = Label(place, textvariable=txtVar, bg="LightGray", fg="black").grid(column=col, row=rw, sticky = (stcky))
	return newLabel

class Notebook(Frame):
	"""Notebook Widget"""
	def __init__(self, parent, activerelief = RIDGE, inactiverelief = RAISED, xpad = 4, ypad = 6, activefg = 'black', inactivefg = 'black', **kw):
																						  #Make various argument available to the rest of the class
		self.activefg = activefg															
		self.inactivefg = inactivefg
		self.deletedTabs = []		
		self.xpad = xpad
		self.ypad = ypad
		self.activerelief = activerelief
		self.inactiverelief = inactiverelief												
		self.kwargs = kw																	
		self.tabVars = {}																  #This dictionary holds the label and frame instances of each tab
		self.tabs = 0																	  #Keep track of the number of tabs																			 
		self.noteBookFrame = Frame(parent)												 #Create a frame to hold everything together
		self.BFrame = Frame(self.noteBookFrame)											#Create a frame to put the "tabs" in
		self.noteBook = Frame(self.noteBookFrame, relief = RAISED, bd = 2, **kw)			#Create the frame that will parent the frames for each tab
		self.noteBook.grid_propagate(0)													#self.noteBook has a bad habit of resizing itself, this line prevents that
		Frame.__init__(self)
		self.noteBookFrame.grid()
		self.BFrame.grid(row =0, sticky = W)
		self.noteBook.grid(row = 1, column = 0, columnspan = 27)

	def change_tab(self, IDNum):
		for i in (a for a in range(0, len(self.tabVars.keys()))):
			if not i in self.deletedTabs:												  #Make sure tab hasen't been deleted
				if i != IDNum:															
					self.tabVars[i][1].grid_remove()										#Remove the Frame corresponding to each tab that is not selected
					self.tabVars[i][0]['relief'] = self.inactiverelief					 #Change the relief of all tabs that are not selected to "Groove"
					self.tabVars[i][0]['fg'] = self.inactivefg							 #Set the fg of the tab, showing it is selected, default is black
				else:																	  #When on the tab that is currently selected...
					self.tabVars[i][1].grid()											  #Re-grid the frame that corresponds to the tab					  
					self.tabVars[IDNum][0]['relief'] = self.activerelief					#Change the relief to "Raised" to show the tab is selected
					self.tabVars[i][0]['fg'] = self.activefg								#Set the fg of the tab, showing it is not selected, default is black

	def add_tab(self, width = 2, **kw):
	
		#Temp is used so that the value of self.tabs will not throw off the argument sent by the label's event binding
		temp = self.tabs 
		
		#Create the tab
		self.tabVars[self.tabs] = [Label(self.BFrame, relief = RIDGE, **kw)]				
		#Makes the tab "clickable"
		self.tabVars[self.tabs][0].bind("<Button-1>", lambda Event:self.change_tab(temp))  
		
		#Packs the tab as far to the left as possible
		self.tabVars[self.tabs][0].pack(side = LEFT, ipady = self.ypad, ipadx = self.xpad) 
		
		#Create Frame, and append it to the dictionary of tabs
		self.tabVars[self.tabs].append(Frame(self.noteBook, **self.kwargs))
		
		#Grid the frame ontop of any other already existing frames
		self.tabVars[self.tabs][1].grid(row = 0, column = 0)
		
		#Set focus to the first tab
		self.change_tab(0)
		
		#Update the tab count
		self.tabs += 1
		
		#Return a frame to be used as a parent to other widgets
		return self.tabVars[temp][1]

	def destroy_tab(self, tab):
		self.iteratedTabs = 0															  #Keep track of the number of loops made
		for b in self.tabVars.values():													#Iterate through the dictionary of tabs
		
			if b[1] == tab:	#Find the NumID of the given tab
				b[0].destroy()  #Destroy the tab's frame, along with all child widgets
				#Subtract one from the tab count
				self.tabs -= 1 
				self.deletedTabs.append(self.iteratedTabs)								 #Apend the NumID of the given tab to the list of deleted tabs
				break																	  #Job is done, exit the loop
			self.iteratedTabs += 1														 #Add one to the loop count
	
	def focus_on(self, tab):
		self.iteratedTabs = 0															  #Keep track of the number of loops made
		for b in self.tabVars.values():													#Iterate through the dictionary of tabs
			if b[1] == tab:																#Find the NumID of the given tab
				self.change_tab(self.iteratedTabs)										 #send the tab's NumID to change_tab to set focus, mimicking that of each tab's event bindings
				break																	  #Job is done, exit the loop
			self.iteratedTabs += 1														 #Add one to the loop count
		
