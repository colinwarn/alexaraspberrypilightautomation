import os
import RPi.GPIO as GPIO
from multiprocessing import Process
import synchronized_lights

pEnd = Process(target=synchronized_lights.end)
print("Different!!!!")
def cleanupGPIO():
    
    if pEnd.is_alive():
        pEnd.terminate()
    
    pEnd.start()
    GPIO.cleanup()

cleanupGPIO()
