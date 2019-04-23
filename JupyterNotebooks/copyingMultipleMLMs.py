#!/usr/bin/python3

import subprocess as s
import os,sys,math

ALLTrains = "/mnt/e/L4ProjectLocal/MLRunArchive/AllTrains"

print("Changing pwd to "+ALLTrains)
os.chdir(ALLTrains)

print("Reading COUNT")
with open('./COUNT','r') as f:
	COUNT = int(f.read())
print("COUNT is at {}".format(COUNT))

ANNz_run = sys.argv[1]
print("Changing pwd to "+'../'+ANNz_run+'/regres/train/')
os.chdir('../'+ANNz_run+'/regres/train/')
DIRs = os.listdir()

length,progress = len(DIRs),0
print("\nNOW COPYING!")
for dir in DIRs:
	progress += 1
	
	if dir == 'postTrain': continue 
	
	completeness = math.floor(progress/length * 10)
	print("[{}>{}] {:3.0f}% ".format('='*completeness,' '*(10-completeness),progress/length*100)+"Now copying {} to {}    ".format(dir,"ANNZ_"+str(COUNT)), end='\r', flush=True)
	
	s.run(["cp","-r",dir,"/mnt/e/L4ProjectLocal/MLRunArchive/AllTrains/ANNZ_"+str(COUNT)])
	COUNT += 1
print("\nCOPYING COMPLETE!\n")

print("COUNT now at {}".format(COUNT))
print("Changing pwd to "+ALLTrains)
os.chdir(ALLTrains)
print("Writing COUNT")
with open('./COUNT','w') as f:
	f.write(str(COUNT))

print("\n\nAll done!")