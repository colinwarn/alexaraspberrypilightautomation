from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import subprocess
import os
from multiprocessing import Process
import synchronized_lights
import alexalightsOFF
import alexalightson
import SocketServer
import RPi.GPIO as GPIO
import threading
from time import sleep


app = Flask(__name__)

offp = Process(target=alexalightsOFF.run)
p = Process(target=synchronized_lights.main)
onp = Process(target=alexalightson.run)
pEnd = Process(target=synchronized_lights.end)
onpEnd = Process(target=alexalightson.end)
offpEnd = Process(target=alexalightsOFF.end)

ask = Ask(app, "/partymode")


        

SocketServer.TCPServer.allow_reuse_address = True

#Plan b setup button press code
GPIO.setmode(GPIO.BOARD)
buttonPin = 29
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
isPartyModeOn = False

def errorChecking():
        print(onp.is_alive())
        print(offp.is_alive())
        print(p.is_alive())


def startPartyMode():
        

        #subprocess.call("cd home/pi/lightshowpi/py")
        #subprocess.Popen(["python", "/home/pi/lightshowpi/py/synchronized_lights.py"], shell=True)
        #os.system("sudo python /home/pi/lightshowpi/py/cleanupGPIO.py")
##        if p.is_alive():
##            p.terminate()

        #os.system("sudo python /home/pi/lightshowpi/py/synchronized_lights.py")
##        onpEnd = Process(target=alexalightson.end)
##        onpEnd.start()
       
##        onpEnd = Process(target=alexalightson.end)
##        offpEnd = Process(target=alexalightsOFF.end)

        p = Process(target=synchronized_lights.main)
        


        
##        onpEnd.start()
##        
##        offpEnd.start()
##        
        
        
        sleep(1)
        p.start()
        errorChecking()
        sleep(2)
        buttonPressed()

def lightsOn():

        #print("LIghts onnn")
   # os.system("sudo python /home/pi/lightshowpi/py/cleanupGPIO.py")
    #os.system('sudo python /home/pi/lightshowpi/py/hardware_controller.py --state=cleanup')
        #sleep(4)

        #os.system("sudo python /home/pi/lightshowpi/py/alexalightson.py")
##    if onp.is_alive():
##        onp.terminate()
##    pEnd = Process(target=synchronized_lights.end)
##    pEnd.start()

##    pEnd = Process(target=synchronized_lights.end)
##    
##    offpEnd = Process(target=alexalightsOFF.end)
##    
##    offpEnd.start()
##    
##    pEnd.start()
##    
    
    onp = Process(target=alexalightson.run)

    

    
    sleep(1)
    onp.start()
    errorChecking()
    sleep(2)
    buttonPressed()

def lightsOff():
    sleep(5)
    os.system('reboot')
##    offp = Process(target=alexalightsOFF.run)
##    offpEnd = Process(target=alexalightsOFF.end)
##    if p.is_alive():
##        pEnd.start()
##    if onp.is_alive():
##        onpEnd.start()
##    
##    offp.start()


modeNumber = 0
def buttonPressed():
    global isPartyModeOn
    global modeNumber
    
    #print(buttonState)
    if GPIO.input(buttonPin) == False:
        
        print("presseddddddddddddddd")
        

        modeNumber += 1
        print(modeNumber)
        if modeNumber == 1:
            print("Party mode started")
            startPartyMode()
            isPartyModeOn = True
            sleep(2)
            

            #startPartyMode()
        elif modeNumber >= 5:
            print('Lights off')
            lightsOff()
            
        elif modeNumber >= 2 & modeNumber < 5:
            #lightsOn()
            print("Lights on")
            lightsOn()
            isPartyModeOn = False
            

            sleep(2)
            
        
    threading.Timer(0.1, buttonPressed).start()
        

buttonPressed()



partyMode = False


    
@app.route('/')
def homepage():
    return "Hi there"

@ask.launch
def start_skill():
    message =  "Ground control started.  Options: Party Mode, Lights On, Lights Off,"
    return question(message)
    
@ask.intent("PartyModeIntent")
def partyMode():
    #synchronized_lights.main()
    
    startPartyMode()
    return statement("Party Mode is On")
    
if partyMode == True:
    startPartyMode()

@ask.intent("LightsOnIntent")
def lightsOnAlexa():
    lightsOn()
    return statement("Lights On")



@ask.intent("LightsOffIntent")
def lightsOffAlexa():
    t1 = threading.Thread(target=lightsOff, args=[]).start()
    return statement("Lights Off")



if __name__ == '__main__':
    app.run(debug=False)
    
