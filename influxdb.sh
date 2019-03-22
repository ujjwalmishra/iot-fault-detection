docker pull influxdb

docker run -p 8086:8086 -v $PWD/influxdb:/var/lib/influxdb influxdb

