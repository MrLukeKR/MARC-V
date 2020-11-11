#!/usr/bin/python

import time
import pantilthat as pt
from picamera import PiCamera

Direction ={"LEFT": (90, 65), "RIGHT": (-90, 65), "UP": (0, 0), "DOWN": (0, 90), "FORWARD": (0, 65)}

camera = PiCamera()
camera.rotation = 180


def set_direction(direction):
	pt.pan(direction[0])
	pt.tilt(direction[1])
	time.sleep(1)

def reset():
	set_direction(Direction["FORWARD"])
