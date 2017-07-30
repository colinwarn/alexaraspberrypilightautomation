import os
from time import sleep

#os.system('sudo /home/pi/Desktop/Python\ Projects/./ngrok http -subdomain=groundcontrol 5000')
sleep(60)
os.system('sudo python /home/pi/lightshowpi/py/app.py')
