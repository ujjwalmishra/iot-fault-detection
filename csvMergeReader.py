from os import listdir
from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np 
import pandas as pd
import os
import csv
import itertools
import glob

entries = []
bwstart = 0
bwend = 500
files = os.listdir("./csvFiles/")
for file in files:
	print file

	for x in range(100):
		if file.startswith("baseline_1"):
			print file
			with open('./csvFiles/baseline_1.mat.csv', 'r') as f:
			    mycsv = csv.reader(f)
			    for row in itertools.islice(mycsv, bwstart,bwend):
			        entries.append(row)
		if file.startswith('InnerRaceFault_vload_1'):
			print file
			with open('./csvFiles/InnerRaceFault_vload_1.mat.csv', 'r') as f:
			    mycsv = csv.reader(f)
			    for row in itertools.islice(mycsv, bwstart,bwend):
			        entries.append(row)
		if file.startswith('OuterRaceFault_1'):
			print file
			with open('./csvFiles/OuterRaceFault_1.mat.csv', 'r') as f:
			    mycsv = csv.reader(f)
			    for row in itertools.islice(mycsv, bwstart,bwend):
			        entries.append(row)
		if file.startswith('OuterRaceFault_vload_1'):
			print file
			with open('./csvFiles/OuterRaceFault_vload_1.mat.csv', 'r') as f:
			    mycsv = csv.reader(f)
			    for row in itertools.islice(mycsv, bwstart,bwend):
			        entries.append(row)

with open('BaseLine-Faulty-merged.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(entries)
