#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
https://makerprojekt.com/portfolio/python-arduino-servo-control/
"""

import serial
from time import time

def move_servo(alpha,dev='/dev/ttyUSB0',baud=9600):
   print('moving to',alpha)
   arduino = serial.Serial(dev,baud)   # create serial object named arduino
   pos = str(int(alpha))
   pos = bytes(pos.encode('utf-8'))
   told = time()
   arduino.write( pos )                          # write position to serial port
   #a = arduino.readline().strip()
   print('-->',time()-told)
   arduino.close()

if __name__ == '__main__':
   from random import randint
   print('empty value to exit')
   a = int(input('Move servo to angle: '))
   move_servo( a )
