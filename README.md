# IoT
Programming assignment for 'Internet of Things' elective @ DHBW Stuttgart

Data-Generator Python Script for InfluxDB
Visualization in Grafana

## Architecture

### InfluxDB

[InfluxDB](https://www.influxdata.com/products/influxdb-overview/) is an open-source time series database. It is written in Go and optimized for fast, high-availability storage and retrieval of time series data in fields such as operations monitoring, application metrics, Internet of Things sensor data, and real-time analytics.

### Grafana

[Grafana](https://grafana.com) is an open source software used for visualization and analysis. By default, Grafana has many different data sources, such as AWS CloudWatch, Elasticsearch, Graphite, InfluxDB, MySQL, OpenTSDB, PostgreSQL and Prometheus. 
With Grafana it is easy to create dashboards. The individual components of dashboards are the panels, which are used to visualize queries.
In this implementation the [Grafana docker container](https://grafana.com/docs/grafana/latest/installation/docker/) is used.

### Datagenerator

The script '[datagenerator.py](https://github.com/dorianriepe/IoT/blob/main/datagenerator.py)' generates random values to imitate temperature data and stores them in the database using the 'InfluxDBClient' for Python.

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/architecture.png)

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
pip install influxdb
python3 datagenerator.py
```



### Grafana

Start Grafana Docker Container:
```
docker run --name grafana -d -p 3000:3000 grafana/grafana
```

Go to [`http://localhost:3000/login`](http://localhost:3000/login) and sign in with the default user `admin` and password `admin`

Go to [`http://localhost:3000/datasources/new`](http://localhost:3000/datasources/new) and create a new Datasource, Select `InfluxDB`:

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/datasource.png "Add a new Datasource")

Insert URL: `http://<INFLUX_DOCKER_CONTAINER_IP>:8086` and Database: `IoT`

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/configure.png "Configure Datasource")

Then `Save & Test`

Go to [`http://localhost:3000/dashboard/import`](http://localhost:3000/dashboard/import) and copy & paste [Dashboard Panel JSON File](https://github.com/dorianriepe/IoT/blob/main/dashboard.json "Dashboard JSON File") and `Load`

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/dashboard.png "Import Dashboard")


## Dashboard

You can now visit the IoT Dashboard

![alt text](https://github.com/dorianriepe/IoT/blob/main/documentation/grafana-dashboard.png "Grafana IoT Dashboard")


