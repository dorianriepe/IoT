import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("----")
    print("topic: ",message.topic)
    print("message: " ,str(message.payload.decode("utf-8")))
    print("qos: ",message.qos)
    print("retain flag: ",message.retain)

broker_address="test.mosquitto.org"
port=1883

client = mqtt.Client("client1")
client.connect(broker_address, port) 

client.loop_start()

client.subscribe("iotcourse/channel", 2)
client.on_message=on_message 

time.sleep(90)
client.loop_stop()
