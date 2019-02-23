#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import cv2
import sys
import time
import numpy as np
import os
import xml.etree.ElementTree as ET


def detect_object(img,haa_cas): 
   """
     Returns the vertices of the rectangles containing the faces of the picture
   as well as the img itself.
   You can specify both the path to the picture you want to analyse or the
   image (the array) itself.
   """
   tree = ET.parse(haa_cas)
   root = tree.getroot()
   size = root[0][0].text
   x = int(size.split(' ')[0])
   y = int(size.split(' ')[1])
   cascade = cv2.CascadeClassifier(haa_cas)

   rects = cascade.detectMultiScale(img, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (x,y))
   if len(rects) == 0:
       return []
   rects[:, 2:] += rects[:, :2]
   return rects


def face(image, haa_cas='cascades/frontal_face.xml'):
   rects = detect_object(image, haa_cas)
   #box(rects, img)
   centers = center(rects) #, image.shape[0]*image.shape[1])
   return centers, rects


def box(rects, img, wr = False):
   """
     Draws a green rectangle  with vertices at rects in the picture img
   if wr argument is True saves it to a file "detected.jpg"
   """
   for x1, y1, x2, y2 in rects:
      cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
   if wr:
     cv2.imwrite('detected.jpg', img);


def center(rects,N=1):
   """
     Returns the position (center) and area of each face detected in one
   list with format:
          [X0, Y0, Area]
     The Area will be normalized to the size of the picture
   """
   centers = []
   for x1, y1, x2, y2 in rects:
      X = int((x1+x2)/2.)
      Y = int((y1+y2)/2.)
      AREA = (x2 - x1) * (y2 - y1)
      centers.append([X,Y,AREA/N])
   return centers
