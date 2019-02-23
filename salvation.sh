#!/bin/bash

sudo modprobe v4l2loopback video_nr=2,3

sudo gst-launch-1.0 -v v4l2src device=/dev/video0 ! tee name=t \
    t. ! queue ! videoscale ! videoconvert ! v4l2sink device=/dev/video2 \
    t. ! queue ! videoscale ! videoconvert ! v4l2sink device=/dev/video3

