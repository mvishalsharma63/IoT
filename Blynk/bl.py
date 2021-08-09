import BlynkLib
import time

blynk = BlynkLib.Blynk('r60XFYDh2ijKi_kSvKJfwr0d6rIEvrtY')

@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
    print('Current V0 value: {}'.format(value))

@blynk.VIRTUAL_READ(2)
def my_read_handler():
    for i in range(0,201,20):
        print(i)
        time.sleep(2)   
                 
    for i in range(200,0,-20):       
        print(i)
        time.sleep(2)

    blynk.virtual_write(2,i)

while True:

    blynk.run()
    
