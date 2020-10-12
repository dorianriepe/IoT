# IoT
Programming assignment for 'Internet of Things' elective @ DHBW Stuttgart

Data-Generator Python Script for InfluxDB
Visualization in Grafana


## Setup



### Influx DB

Start InfluxDB Docker Container:
```
docker run --name influx -p 8086:8086 -p 8088:8088 -d influxdb
```
Get IP-Address of InfluxDB Container:
```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' influx
```
Go to InfluxDB Container bash and create a new Database named 'IoT':
```
docker exec -it influx bash
influx -precision rfc3339
CREATE DATABASE IoT
```



### Datagenerator Python Script

```
python3 datagenerator.py
```



### Grafana

Start Grafana Docker Container:
```
docker run --name grafana -d -p 3000:3000 grafana/grafana
```

Go to `http://localhost:3000/login` and sign in with the default user `admin` and password `admin`

Go to `http://localhost:3000/datasources/new` and create a new Datasource, Select `InfluxDB`:

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/datasource.png "Add a new Datasource")

Insert URL: `http://<INFLUX_DOCKER_CONTAINER_IP>:8086` and Database: `IoT`

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/configure.png "Configure Datasource")

Then `Save & Test`

Go to `http://localhost:3000/dashboard/import` and copy & paste [Dashboard Panel JSON File](https://github.com/dorianriepe/IoT/blob/main/dashboard.json "Dashboard JSON File") and `Load`

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/dashboard.png "Import Dashboard")


## Dashboard

You can now visit the IoT Dashboard

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/grafana-dashboard.png "Grafana IoT Dashboard")


