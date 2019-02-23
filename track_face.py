#! /usr/bin/env python
# -*- coding: UTF-8 -*-


try: import cv2
except ModuleNotFoundError:
   print('OpenCV not installed, you can just try')
   print('$ sudosudo apt-get install python3-opencv')
   exit(1)
import numpy as np
import detection as dtct
import matplotlib.pyplot as plt
from time import time, sleep


import serial
dev = '/dev/ttyUSB0'
baud=9600
try: arduino = serial.Serial(dev,baud)   # create serial object named arduino
except serial.serialutil.SerialException:
   print('Arduino is not connected')
   exit(1)
alpha0 = 120

cap = cv2.VideoCapture(1)
#kernel = np.ones((5,5),np.uint8)

print('Initial positioning')
x0_deg = 90
pos_x = bytes(str(x0_deg).encode('utf-8'))
arduino.write( pos_x )
sleep(1)
print('done')

out = False
pos_x = '90'
pos_y = '90'
prev_angle = 90
while not out:
   a, img = cap.read()
   img = cv2.flip( img, 0 )
   vid_y, vid_x, _ = img.shape

   # Look for faces
   centers, corners = dtct.face(img)

   # Draw a box around each face
   dtct.box(corners, img)

   if len(centers) > 0:
      # Find centroid of all the faces (weighted by the size of the face)
      M = np.array(centers)
      X = M[:,0]
      Y = M[:,1]
      A = M[:,2]
      x0 = np.average(X,weights=A)  # position in pixels
      y0 = np.average(Y,weights=A)  #
      x0_deg = 180 - (170*(x0/vid_x)+10)

      x0_deg = (0.5-(x0/vid_x))*2  # \in [-1,1]
      if abs(x0_deg) > 0.05:
         x0_deg = 5*x0_deg  #/abs(x0_deg)
      else: x0_deg = 0
      new_angle = prev_angle+x0_deg
      pos_x = bytes(str(new_angle).encode('utf-8'))
      arduino.write( pos_x )
      # XXX To be included when I can implement the second servo
      #pos_y = bytes(str(x0).encode('utf-8'))
      #arduino.write( pos_y )

      prev_angle = new_angle

   # ===============================
   #    Shows the processed image
   # ===============================
   cv2.imshow('face',img)
   k = cv2.waitKey(5) & 0xFF  #   Waits for  <Esc> key
   if k == 27:                # to exit the infinite loop
     out = True               #
     break                    #

cv2.destroyAllWindows()
print('Final positioning')
x0_deg = '90'
pos_x = bytes(x0_deg.encode('utf-8'))
arduino.write( pos_x )
sleep(1)
arduino.write( pos_x )   # XXX For some reason some times it doesn't return to
sleep(1)                 # 90 position right away
print('done')
arduino.close()
