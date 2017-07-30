import threading
import RPi.GPIO as GPIO
#import alexalightson

GPIO.setmode(GPIO.BOARD)
buttonPin = 29
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
isPartyModeOn = False

def buttonPressed():
    global isPartyModeOn
    
    #print(buttonState)
    if GPIO.input(buttonPin) == False:
        print("presseddddddddddddddd")
        if isPartyModeOn == False:
            print("Party mode started")
            isPartyModeOn = True

            #startPartyMode()
        else:
            #lightsOn()
            print("Lights on")
            isPartyModeOn = False
    threading.Timer(0.1, buttonPressed).start()





        

buttonPressed()
