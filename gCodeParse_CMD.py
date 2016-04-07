###This is a command line version of gcode compare. 
### It only requires python 3.2
### Files are passed in as args, or hard coded.


import sys
import string
import time
import csv
import os
import os.path

def ReadGcode(File1, File2, outfile):
	LastLine = 185 #where the actual Gcode begins. 
	startTime = time.time()
	print("File1 = " + File1 + "\nFile2 = "+ File2+"\nOutput File = " + outfile+"\n");
	with open(File1) as myFile1:
		with open(File2) as myFile2:
			readLines1 = myFile1.readlines()[0:LastLine]
			readLines2 = myFile2.readlines()[0:LastLine]
			for i in range(len(readLines1)):
				if(readLines1[i] != readLines2[i]):
					print("LINE["+str(i)+"] " + readLines1[i] +" is NOT= " + readLines2[i])
	elapsedTime = time.time() - startTime
	m, s = divmod(elapsedTime, 60)
	h, m = divmod(m, 60)
	print("The operations took: %02d:%02d:%02d (H:M:S)" % (h, m, s))
	print("Finished!")

def main():
	#you can hard code a DB and query or pass them as arguments
	File1 = os.environ["USERPROFILE"] +r"\Documents\Python\HandOfThe_King.gcode" #"File1.gcode"
	File2 = os.environ["USERPROFILE"] +r"\Documents\Python\HandOfThe_King2.gcode"#"File2.gcode"
	testOutputcsv = "outputfile here"
	if len(sys.argv) == 3:
		File1 = sys.argv[1]
		File2 = sys.argv[2]
		testOutputcsv = sys.argv[3]
	if len(sys.argv) == 1:
		print("\n###USING HARD CODED VALUES###\n")
	else:
		print("IMPROPER ARGUMENTS!!!\n\n Expected format:\n File1\n File2\n output file\n (quotations are your friend with complicated names/paths)")
		
	if(os.path.isfile(File1) and os.access(File1, os.R_OK)
	and os.path.isfile(File2) and os.access(File2, os.R_OK)):
			ReadGcode(File1, File2, testOutputcsv)
	else:
		print("\n!!!!File missing or unreadable!!!\n")
		print("File1 Tried: " + str(File1))
		print("File2 Tried: " + str(File2))
	sys.exit()
	
if __name__ == "__main__":
	main()
