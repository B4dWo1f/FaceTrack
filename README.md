# Face-Tracking
In this repo I develop a simple code to track faces with a webcam, an arduino and a small servo.

We need to install a few dependencies:
 - the Arduino idle. check it out [here](https://www.arduino.cc/en/guide/linux)
 - OpenCV. Installing the latest version usually requires compiling from [source](https://github.com/opencv/opencv) and it is  a bit cumbersome, for our purposes, in Ubuntu 18.04, it is enough to install it from the apt-get repo:
```
$ sudo apt-get install python3-opencv 
```

First you need to upload the arduino code into the arduino. You can check if it works using the code in ``` myservo.py ```


Then you can just run
```
$ python track_face.py
```
