from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import cv2


class camera:
    def __init__(self):
        self.camera = PiCamera()
        self.rawCapture = PiRGBArray(self.camera)
        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def takePicture(self):
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.05, 3)
            self.rawCapture.truncate(0)
            print(faces)
            sleep(0.1)
            if len(faces) != 0:
                cv2.imwrite("image.jpg", image)
                break


#self.camera.start_preview()
#sleep(1)
#self.camera.capture('/home/pi/CoolOMeter/picture.jpg')
#self.camera.stop_preview()