from influxdb import InfluxDBClient
import csv
import json
import random

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'complete_data_result')
# client.drop_database('complete_data')
client.create_database('complete_data_result')

buffer_length = 4000

buffered_payload = []

def writeResults(row0, row1, row2, row3, label):
    row_count = 0
    global buffered_payload
    for i in range(len(label)):
        data = {}
        data['measurement'] = "iot_fault_data_result"
        data['time'] = row0[i]
        fields = {}
        fields['load'] = row1[i]
        fields['rate'] = row2[i]
        fields['gs'] = row3[i]
        fields['label'] = label[i]
        data['fields'] = fields
        buffered_payload.append(data)
        row_count = row_count + 1
        if row_count == buffer_length:
            # print(buffered_payload)                  
            client.write_points(buffered_payload)
            row_count = 0 
            buffered_payload = []




def getResult():
    result = client.query('select load,rate,gs,label from iot_fault_data_result;')

    print(list(result.get_points(measurement='iot_fault_data_result')))
    data = result.raw['series'][0]['values']
    for row in data:
        print(row)
    