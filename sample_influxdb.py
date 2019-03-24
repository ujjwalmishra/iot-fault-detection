from influxdb import InfluxDBClient

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
    },
        {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T14:00:00Z",
        "fields": {
            "value": 0.64,
            "value2": 0.56
        }
    }
]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')

client.create_database('example')

client.write_points(json_body)

result = client.query('select value,value2 from cpu_load_short;')

print(result.raw['series'][0]['values'])
data = result.raw['series'][0]['values']
for row in data:
    print(row)
print("Result: {0}".format(result))