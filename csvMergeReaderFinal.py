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
import datetime


entries = []
bwstart = 0
bwend = 500
# files = os.listdir("./csvFiles/")


for x in range(1000):
	rand = random.randint(1,20)
	if rand == 1:
		with open('./csvFiles/baseline_1.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)  #rate
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/97656)				
				row.append(0)
				entries.append(row[1:])
				
	if rand == 2:
		with open('./csvFiles/InnerRaceFault_vload_1.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(0) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)				
				row.append(1)
				entries.append(row[1:])
	if rand == 3:
		with open('./csvFiles/OuterRaceFault_1.mat.csv', 'r') as f:
			current_timestamp = datetime.datetime.now()
			mycsv = csv.reader(f)
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/97656)	
				row.append(2)
				entries.append(row[1:])
	if rand == 4:
		with open('./csvFiles/OuterRaceFault_vload_1.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(25) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(2)
				entries.append(row[1:])
	if rand == 5:
		with open('./csvFiles/baseline_2.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270)
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/97656)
				row.append(0)
				entries.append(row[1:])
	if rand == 6:
		with open('./csvFiles/InnerRaceFault_vload_2.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(0) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(1)
				entries.append(row[1:])
	if rand == 7:
		with open('./csvFiles/OuterRaceFault_2.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/97656)	
				row.append(2)
				entries.append(row[1:])
	if rand == 8:
		with open('./csvFiles/OuterRaceFault_vload_2.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(2)
				entries.append(row[1:])
	if rand == 9:
		with open('./csvFiles/baseline_3.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270)
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/97656)
				row.append(0)
				entries.append(row[1:])
	if rand == 10:
		with open('./csvFiles/InnerRaceFault_vload_3.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(0) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(1)
				entries.append(row[1:])
	if rand == 11:
		with open('./csvFiles/OuterRaceFault_3.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/97656)	
				row.append(2)
				entries.append(row[1:])
	if rand == 12:
		with open('./csvFiles/OuterRaceFault_vload_3.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(2)
				entries.append(row[1:])
	if rand == 13:
		with open('./csvFiles/InnerRaceFault_vload_4.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(0) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(1)
				entries.append(row[1:])
	if rand == 14:
		with open('./csvFiles/InnerRaceFault_vload_5.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(0) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(1)
				entries.append(row[1:])
	if rand == 15:
		with open('./csvFiles/InnerRaceFault_vload_6.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(0) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(1)
				entries.append(row[1:])
	if rand == 16:
		with open('./csvFiles/InnerRaceFault_vload_7.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(0) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(1)
				entries.append(row[1:])
	if rand == 17:
		with open('./csvFiles/OuterRaceFault_vload_4.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(2)
				entries.append(row[1:])
	if rand == 18:
		with open('./csvFiles/OuterRaceFault_vload_5.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(2)
				entries.append(row[1:])
	if rand == 19:
		with open('./csvFiles/OuterRaceFault_vload_6.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(2)
				entries.append(row[1:])
	if rand == 20:
		with open('./csvFiles/OuterRaceFault_vload_7.mat.csv', 'r') as f:
			mycsv = csv.reader(f)
			current_timestamp = datetime.datetime.now()
			for row in itertools.islice(mycsv, bwstart,bwend):
				row.append(270) #load
				row.append(25)
				row.append(current_timestamp.utcnow())			
				#increment timestamp
				current_timestamp = current_timestamp + datetime.timedelta(seconds=1/48828)	
				row.append(2)
				entries.append(row[1:])
	bwstart = bwend
	bwend = bwend + 500

with open('BaseLine-Faulty-merged.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(entries)
