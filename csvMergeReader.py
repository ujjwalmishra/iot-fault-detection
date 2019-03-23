from os import listdir
from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np 
import pandas as pd
import os
import csv
import itertools
import glob
import random

entries = []
bwstart = 0
bwend = 500
files = os.listdir("./csvFiles/")


for x in range(100):
	rand = random.randint(1,4)
	if rand == 1:
		with open('./csvFiles/baseline_1.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)  #rate
				row.append(0)
				entries.append(row[1:])
				
	if rand == 3:
		with open('./csvFiles/InnerRaceFault_vload_1.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(0) #load
				row.append(25)  #rate
				row.append(1)
				entries.append(row[1:])
	if rand == 4:
		with open('./csvFiles/OuterRaceFault_1.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)  #rate
				row.append(2)
				entries.append(row[1:])
	if rand == 2:
		with open('./csvFiles/OuterRaceFault_vload_1.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(25) #load
				row.append(25)  #rate
				row.append(2)
				entries.append(row[1:])

	bwstart = bwend
	bwend = bwend + 500

with open('BaseLine-Faulty-merged.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(entries)
