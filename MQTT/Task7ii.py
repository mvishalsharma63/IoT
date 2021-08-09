import paho.mqtt.client as mqtt
import time
while (1):
    a = input("Enter Data:")
    client = mqtt.Client()
    client.connect("broker.mqtt-dashboard.com", 1883,60)
    client.publish("qwerty",a)
    time.sleep(1)
    client.disconnect()
