# Coolometer

A device, [inspired by Futurama](https://www.youtube.com/watch?v=tXb7gLe0zNk), to measure your coolness with a "real" AI.


## Components

This are the components we used. Alternatives might work also

- Raspberry PI Model 3 B+
- Raspberry PI Camera
- Micro Servo SG90
- MAX 4218CNG LED Matrix
- L9110 Motor Driver
- DC Motor 3V 16500 RPM 0.35A 130 Type
- Pizzo Speaker
- 3.5 mm Headphone Jack
- LY591-4 speaker
- PAM8403 Mini Amplifier
- Button
- 5V 2.1 A PowerBank for Power supply

### Wiring

Raspberry PI Model 3 B+ has enough ground Pins for all parts. Only one 5V pin has to be shared by the LED Matrix and the Servo motor.

<p align="center">
<img src="imgs/wiring.jpg" width="400">
</p>

#### Micro Servo SG90
One 5V shared with MAX 4218CNG LED Matrix
Data on GPIO 17 / PIN 11

#### MAX 4218CNG LED Matrix
One 5V shared with MAX 4218CNG LED Matrix
DIN on GPIO 10 / PIN 19
CS on GPIO 8 / PIN 24
CLK on GPIO 11 / PIN 23

#### L9110 Motor Driver
VCC on 3.3 
IA1 on GPIO 26 / PIN 37
IB1 on GPIO 20 / PIN 38

#### Pizzo Speaker
VCC on 3.3
GND on GPIO 36 / PIN 16

#### Headphone Jack / Amplifier
The Headphone Jack uses the Audio Out from the Raspberry PI.
Solder the longest PIN of the Jack to the "I" PIN of the Amplifier Board
Solder the second longest PIN longest PIN of the Jack to the "R" PIN of the Amplifier Board. We only use one Channel here.

Solder the R OUT PINs the the speaker.

Use one 5V Pin from the Raspberry PI to power the Amplifier Board

#### Button
VCC on 3.3 
GND to GPIO 18 / PIN 12

#### Camera
The camera is connected on the Raspberry Camera slot.


## Install

TODO

## 3D Print and Lasercut files
TODO

## Usage

After you power your raspberry, it can take about 40 seconds to boot.
When the device is ready, the pizzo will make noise for a short time and the clockhand will go to zero.

Now press the button.

The clockhand will go to 50%  and the camera starts to search for a human face.

If the face is detected the clockhand will go to your coolness value and the pizzo will make noise according to the coolness.
If your coolness is 90% or higher, the thumb will come out and you will hear an "OH Yeah"

If your press the button again you will start from the beginning. 

HAVE FUN :)

## Train your own tensorflow lite model

The files contains our trained tensorflow lite model. The train data are our little secret. If you are not happy with it, here is a short description how to make your own model.

On your host machine with Linux, Python3 and pip:
```bash
pip3 install tensorflow
pip3 install tensorflow-hub[make_image_classifier]
```

Create a folder structure like the following one. And put picture into the cool / lame folder. Only JPG Files are allowed.
Base Folder
* coolometer (Folder)
    * cool (Folder)
        * img.jpg ...
    * lame (Folder)
        * img.jpg ..
* model (Folder)


In the Base folder call this command:
```bash
make_image_classifier   
--image_dir coolometer   
--tfhub_module https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4 
--image_size 224 
--saved_model_dir model/coolModel 
--batch_size 20  
--labels_output_file class_labels.txt 
--tflite_output_file tf_model_file.tflite
```
You can use other models if you exchange the tfhub_module link to something else from the [tensorflow hub ](https://tfhub.dev/). Make sure you adjuste the image_size to your choosen model.
In your base folder should now be a class_labels.txt and a tf_model_file.tflite file. Copy this to your Raspberry into the Coolometer folder.

If you have a new model, make sure to share it with us by open a pull request with your model data.


## Credits

Big thanks to the futurama creators comming up with this great Idea.
The OhYeah sound is from here: https://www.youtube.com/watch?v=c4c-egnkdLI