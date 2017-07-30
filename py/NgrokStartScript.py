import os
import threading
from time import sleep

def turnOnApp():
    sleep (45)
    os.system('sudo python /home/pi/lightshowpi/py/app.py')
    

t1 = threading.Thread(target=turnOnApp, args=[]).start()

os.system('sudo /home/pi/Desktop/Python\ Projects/./ngrok http -subdomain=groundcontrol 5000')
