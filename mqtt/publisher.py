import paho.mqtt.client as paho
import datetime
import random
import time

broker="test.mosquitto.org"
port=1883

def on_publish(client,userdata,result):
    print("data published \n")
    pass

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client1 = paho.Client("client1")                

client1.on_publish = on_publish   
client1.on_message = on_message

client1.connect(broker,port)                                 

while True:

    temperature_bedroom = round(random.gauss(21, 1),1)

    data = {
        "time":datetime.datetime.now().strftime("%Y.%M.%d, %H:%M:%S.%f"),
        "id": 420,
        "temp": temperature_bedroom
    }

    ret = client1.publish("iotcourse/channel",str(data))   

    time.sleep(5)
