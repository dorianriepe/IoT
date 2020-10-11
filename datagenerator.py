# Author: @dorianriepe, Date: October 2020

from influxdb import InfluxDBClient
import time
import random

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('IoT')

while True:

    temperature_bedroom = round(random.gauss(21, 1),1)
    temperature_entry = round(random.gauss(19, 1),1)
    temperature_outside = round(random.gauss(8, 1),1)

    json_body = [
        {
            "measurement": "temperature_sensor",
            "tags": {
                "room": "bedroom",
            },
            "fields": {
                "temperature": temperature_bedroom,
            }
        },
        {
            "measurement": "temperature_sensor",
            "tags": {
                "room": "entry",
            },
            "fields": {
                "temperature": temperature_entry,
            }
        },
        {
            "measurement": "temperature_sensor",
            "tags": {
                "room": "outside",
            },
            "fields": {
                "temperature": temperature_outside,
            }
        }
    ]

    print(temperature_bedroom)
    print(temperature_entry)
    print(temperature_outside)
    time.sleep(5)
    client.write_points(json_body)