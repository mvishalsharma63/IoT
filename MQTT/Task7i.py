import paho.mqtt.client as mqtt
def on_connect(client,userdata,flags,rc):
    print("Connected with result code [0]".format(str(rc)))
    client.subscribe("qwerty")
def on_message(client,userdata,msg):
    print("Message recieved-> " + msg.topic+ " " +str(msg.payload))
while(1) :
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.mqtt-dashboard.com",1883,60)
    client.loop_forever()   
