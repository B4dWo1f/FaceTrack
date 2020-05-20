#!/bin/bash

sudo depmod -a

sudo modprobe v4l2loopback devices=2

ffmpeg -f v4l2 -i /dev/video0 -f v4l2 /dev/video2 -f v4l2 /dev/video3
