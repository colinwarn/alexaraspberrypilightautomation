import RPi.GPIO as GPIO
from time import sleep
import os
import sys

def run():

    try:
        os.system("sudo python /home/pi/lightshowpi/py/hardware_controller.py --state=cleanup")
        lightsOn = False
        GPIO.setmode(GPIO.BOARD)
        gpioArray  = [11, 12, 13, 15, 16, 18, 22, 7]
        for i in gpioArray:
            GPIO.setup(i, GPIO.OUT)
        for i in gpioArray:
            GPIO.output(i, False)
    finally:
        GPIO.cleanup()
        quit()
        


def end():
    GPIO.setmode(GPIO.BOARD)
    gpioArray  = [11, 12, 13, 15, 16, 18, 22, 7]
    for i in gpioArray:
        GPIO.setup(i, GPIO.OUT)
    GPIO.cleanup()
    quit()


##if __name__ == '__main__':
##    run()
