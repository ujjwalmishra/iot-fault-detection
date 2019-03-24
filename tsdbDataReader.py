from influxdb import InfluxDBClient
import csv
import json
import random

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'complete_data')

chunk_size = 500

def shuffleData(data):
    shufleList = []
    counter = 0
    localList = []
    for item in data:
        localList.append(item)
        counter = counter +1
        if(counter == chunk_size):
            shufleList.append(localList)
            localList = []
            counter = 0

    random.shuffle(shufleList)
    flat_list = []
    for sublist in shufleList:
        for item in sublist:
            flat_list.append(item)
    print("Shuffle complete")
    return flat_list

def readData():
    data = client.query('select load,rate,gs,label from iot_fault_data;')

    return data.raw['series'][0]['values']

