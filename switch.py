import RPi.GPIO as GPIO
import time

class Switch:
    def __init__(self,switchPin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(switchPin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        self.switchPin = switchPin

    def waitForSwitch(self):
        while True:
            time.sleep(0.01)
            if GPIO.input(self.switchPin):
                return
                

