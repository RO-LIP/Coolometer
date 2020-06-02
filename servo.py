import RPi.GPIO as GPIO




class Servo:
    def __init__(self,servoPin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPin, GPIO.OUT)
        self.servo = GPIO.PWM(servoPin, 50) # GPIO with PWM 50Hz
        self.servo.start(2.5) #init

    def setservo(self, degree):
        if degree < 0:
            degree = 0
        elif degree > 180:
            degree = 180
        self.servo.ChangeDutyCycle(degree/18 + 2.5)
        

    def cleanup(self):
        self.servo.ChangeDutyCycle(2.5)
        self.servo.stop()
        GPIO.cleanup()
