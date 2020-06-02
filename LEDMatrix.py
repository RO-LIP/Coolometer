import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas


class LEDMatrix:
    def __init__(self):
        serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(serial, 8, 8, 1, 0)

    def clear(self):
        with canvas(self.device) as draw:
            draw.rectangle(self.device.bounding_box, outline="black", fill="black")
    
    def show(self):
        with canvas(self.device) as draw:
            draw.rectangle(self.device.bounding_box, outline="white", fill="white")

        for i in range(0 , 255):
            self.device.contrast(i)
            time.sleep(0.003)
        for i in range(255 , 0):
            self.device.contrast(i)
            time.sleep(0.003)
        for i in range(0 , 255):
            self.device.contrast(i)
            time.sleep(0.005)
        for i in range(255 , 0):
            self.device.contrast(i)
            time.sleep(0.005)
        self.clear()

