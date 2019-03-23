from influxdb import InfluxDBClient
import csv

json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64,
            "value2": 0.56
        }
    }
]

buffer_length = 4000

def readData():
    with open('./BaseLine-Faulty-merged.csv', 'r') as f:
        iot_data = csv.reader(f)
        for row in iot_data:
            print(row)

readData()


# client = InfluxDBClient('localhost', 8086, 'root', 'root', 'complete_data')

# client.create_database('complete_data')

# client.write_points(json_body)

# result = client.query('select value2 from cpu_load_short;')

# print("Result: {0}".format(result))