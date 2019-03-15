from os.path import dirname, join as pjoin
import scipy.io as sio
import numpy as np 
import pandas as pd
import os

#Convert to csv
for filename in os.listdir("./matFiles"):
    print(filename)
    baseline_Data = sio.loadmat("./matFiles/" + filename)
    df = pd.DataFrame(baseline_Data['bearing'][0])
    print(df)
    df = pd.DataFrame(df['gs'][0])
    df.to_csv("./csvFiles/" + filename +".csv")


# Load baseline data
# baseline_Data = sio.loadmat("baseline_1.mat")

# print(baseline_Data['bearing'])

# print(baseline_Data['bearing'].shape)

# df = pd.DataFrame(baseline_Data['bearing'][0])

# print(df)

# populate rows to the count of total samples

# def popRows(df):
#     rCount = len(df['gs'][0]) 
#     newDf = pd.DataFrame(columns=['sr','gs','load','rate'])
#     sr = df['sr'][0]
#     load = df['load'][0]
#     rate = df['rate'][0]
#     for i in range(rCount):
#         newDf = newDf.append({'sr': sr, 'gs': df['gs'][0][i], 'load': load, 'rate': rate}, 
#         ignore_index=True)
#         print(i)
#     print(newDf)
#     print(newDf.shape)   
#     newDf.to_csv("baseline_1.csv") 

# print((df['gs'][0][0]))

# print(df.shape)

# popRows(df)