#!/usr/bin/python

import time
import pantilthat as pt
import cv2
import numpy as np

from picamera import PiCamera
from picamera.array import PiRGBArray

Orientation ={"LEFT": (90, 65), "RIGHT": (-90, 65), "UP": (0, 0), "DOWN": (0, 90), "FORWARD": (0, 65)}
Direction = {"UP": (0, -15), "RIGHT": (-15, 0), "DOWN": (0, 15), "LEFT": (15, 0)}

camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(640, 480))
curr_pan = 0
curr_tilt = 65

def get_stream():
	return camera.capture_continuous(rawCapture, format="bgr", use_video_port=True), rawCapture

def get_image():
	camera.capture(rawCapture, format="bgr")
	return rawCapture.array

def show_camera():
	for frame in get_stream():
		image = frame.array
		cv2.imshow("MARC-V Main Camera", image)
		key = cv2.waitKey(1) & 0xFF
		rawCapture.truncate(0)
		if key == ord("q"):
			break

def move(direction):
	global curr_pan, curr_tilt

	curr_pan += direction[0]
	curr_tilt += direction[1]

	curr_pan = np.clip(curr_pan, -90, 90)
	curr_tilt = np.clip(curr_tilt, 0, 90)

	update_pan_tilt()

def update_pan_tilt():
	global curr_pan, curr_tilt

	pt.pan(curr_pan)
	pt.tilt(curr_tilt)

	time.sleep(1)

def set_orientation(orientation):
	global curr_pan, curr_tilt

	curr_pan = orientation[0]
	curr_tilt = orientation[1]
	
	update_pan_tilt()

def reset():
	set_orientation(Orientation["FORWARD"])
