import time
import sys
import os
from time import sleep
import urllib.request

myapi = "LG8S2IQOSQJLKRJA"
delay = 3
print("Activating...")
baseurl = 'https://api.thingspeak.com/update?api_key=%s'%myapi
print(baseurl)

while True:
    for i in range (0,200,20):
        print(i)
        urllib.request.urlopen(baseurl + "&field1=%s"%str(i))
        time.sleep(3)
    for i in range(200,0,-20):
        print(i)
        urllib.request.urlopen(baseurl + "&filed1=%s"%str(i))
        time.sleep(3)
