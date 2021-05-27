import time
from multiprocessing import Process, Value

import servo 
import switch
import camera
import speaker
import motor
import LEDMatrix
import piezo
import messure

import RPi.GPIO as GPIO




if __name__ == '__main__':

    piz = piezo.Piezo(16)
    print("Piezo init")
    pointer = servo.Servo(17)
    print("Servo init")
    sw = switch.Switch(18)
    print("Switch init")
    cam = camera.camera()
    time.sleep(0.1)
    print("Camera init")
    speak = speaker.speaker("OhYeah.mp3")
    print("Speaker init")
    mot = motor.motor()
    print("Motor init")
    matrix = LEDMatrix.LEDMatrix()
    print("LEDMatrix init")
    mes = messure.messure()
    print("messure init")
    #start piezo in parallel
    time.sleep(0.1)
    pizWait = Value('d', 0.4)
    p = Process(target=piz.trigger, args=(pizWait,))
    p.start()
    print("Task init")
    coolness = 0
    time.sleep(1.0)

    try:
        while True:
    # cleanup
            coolness = 0
            pizWait.value = 0.0 
            time.sleep(0.1)
            matrix.clear()
            print("Matrix clear")
            time.sleep(0.1)
            pointer.setservo(0)
            print("Servo clear")
            print("Motor clear")
            time.sleep(0.1)
            mot.inside()
    # wait for Sitch
            sw.waitForSwitch()
            pointer.setservo(90)
    #if pressed
            cam.takePicture()

            coolness = mes.getCoolness()
            print(coolness)

    # show coolness
            pizWait.value = coolness
            pointer.setservo((1-coolness) * 180)
            
    # if someone is extremly cool
            if coolness >= 0.9:
                time.sleep(0.3)
                mot.outside()
                time.sleep(0.6)
                speak.playSound()
                time.sleep(1) 
                matrix.show()

                
                
    # restart on switch
            sw.waitForSwitch()
        


    except KeyboardInterrupt:
    # Abbruch mit [Strg][C],
    # Servo auf 0 Grad, PWM beenden
        pointer.cleanup()
        p.join()


