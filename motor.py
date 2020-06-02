import sys
import time
import RPi.GPIO as GPIO



class motor:
    def __init__(self):
        self.IsOutside = True
        GPIO.setup(26, GPIO.OUT,initial=False)
        GPIO.setup(20, GPIO.OUT,initial=False)
        self.forward = GPIO.PWM(26, 100)
        self.backward = GPIO.PWM(20, 100)
        

    def outside(self):
        if self.IsOutside == True:
            return
        time.sleep(0.5)
        self.forward.start(35)
        time.sleep(0.5)
        self.forward.stop()
        time.sleep(0.5)
        self.IsOutside = True

    def inside(self):
        if self.IsOutside == False:
            return
        time.sleep(0.5)
        self.backward.start(35)
        time.sleep(0.5)
        self.backward.stop()
        time.sleep(0.5)
        self.IsOutside = False
