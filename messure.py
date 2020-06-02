import argparse
import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite



class messure:
    def __init__(self):
        self.interpreter = tflite.Interpreter("tf_model_file.tflite")
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        # NxHxWxC, H:1, W:2
        self.height = self.input_details[0]['shape'][1]
        self.width = self.input_details[0]['shape'][2]
        self.labels = self.load_labels("class_labels.txt")

    def getCoolness(self):
        img = Image.open("image.jpg").resize((self.width, self.height))
         # add N dim
        input_data = np.expand_dims(img, axis=0)
        input_data = (np.float32(input_data) - 127.5) / 127.5
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        results = np.squeeze(output_data)
        print('{:08.6f}: {}'.format(float(results[0]), self.labels[0]))
        print('{:08.6f}: {}'.format(float(results[1]), self.labels[1]))

        return float(results[0])

    def load_labels(self, filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]

    

    

    




