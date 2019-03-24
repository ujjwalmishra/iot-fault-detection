from influxdb import InfluxDBClient
import csv
import json


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'complete_data')

# client.create_database('complete_data')

buffer_length = 4000

buffered_payload = []

def readData():
    with open('./BaseLine-Faulty-merged.csv', 'r') as f:
        iot_data = csv.reader(f)
        row_count = 0
        global buffered_payload
        for row in iot_data:
            data = {}
            data['measurement'] = "iot_fault_data"
            data['time'] = row[3]
            fields = {}
            fields['load'] = row[1]
            fields['rate'] = row[2]
            fields['gs'] = row[0]
            fields['label'] = row[4]
            data['fields'] = fields
            buffered_payload.append(data)
            row_count = row_count + 1
            if row_count == buffer_length:
                # json_data = json.dumps(buffered_payload)
                print(buffered_payload)                  
                client.write_points(buffered_payload)
                row_count = 0 
                buffered_payload = []

readData()






result = client.query('select load from iot_fault_data;')

print("Result: {0}".format(result))