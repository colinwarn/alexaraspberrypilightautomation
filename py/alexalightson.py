import RPi.GPIO as GPIO
from time import sleep
import synchronized_lights
from multiprocessing import Process
import os
import sys
import atexit
import threading

def end():
    GPIO.setmode(GPIO.BOARD)
    gpioArray  = [11, 12, 13, 15, 16, 18, 22, 7]
    buttonPin = 29
    for i in gpioArray:
        GPIO.setup(i, GPIO.OUT)
    GPIO.cleanup()
    quit()

def run():
    GPIO.setmode(GPIO.BOARD)
    gpioArray  = [11, 12, 13, 15, 16, 18, 22, 7]
    buttonPin = 29
    for i in gpioArray:
        GPIO.setup(i, GPIO.OUT)

    try:
        while True:
            for i in gpioArray:
                GPIO.output(i, True)
        
            
            
                
                
              
                    

                    
                    
    finally:
        GPIO.cleanup()
        quit()



    

#atexit.register(onExit)

##if __name__ == '__main__':
##    run()
