#!/usr/bin/python3

import subprocess as s
import os,sys,math
import numpy as np

ALLTrains = "/mnt/e/L4ProjectLocal/MLRunArchive/AllTrains"
ANNZroot = "/home/andrew/ProjectInstalls/ANNZ"
ANNZoutputFolder = "/testingdirectory"

print("Changing pwd to "+ALLTrains)
os.chdir(ALLTrains)

print("Reading COUNT")
with open('./COUNT','r') as f:
	COUNT = int(f.read())

n_MLMs = 20

randomMLMS = np.random.randint(0, COUNT, n_MLMs)

print("Copying MLMs")

for i,mlm in enumerate(randomMLMS):
	# s.run(["ll"],stdout=sys.stdout)
	print("Making copying from ANNZ_{} to ANNZ_{}    ".format(mlm,i),end='\r')
	# s.run(["ln","--symbolic",ALLTrains+"/ANNZ_"+str(mlm),ANNZroot+"/output"+ANNZoutputFolder+"/regres/train/"+"ANNZ_"+str(i)])
	s.run(["cp","-r",ALLTrains+"/ANNZ_"+str(mlm),ANNZroot+"/output"+ANNZoutputFolder+"/regres/train/"+"ANNZ_"+str(i)])
print("Copying Complete!                         ")









print("ALL DONE!")