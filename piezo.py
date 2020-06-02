import RPi.GPIO as GPIO
from multiprocessing import Value
import time


class Piezo:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)


    def trigger(self, waitTime):
        try:
            while True:
                if waitTime.value == 0.0:
                    time.sleep(1.0)
                    continue
                GPIO.output(self.pin, True)
                time.sleep(0.05)
                GPIO.output(self.pin, False)
                time.sleep(1.0 - waitTime.value)
        except KeyboardInterrupt:
            pass


