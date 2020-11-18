#!/usr/bin/python

import numpy as np
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)
sense.clear()

R = [255, 0, 0]
G = [0, 255, 0]
B = [0, 0, 255]
Y = [255, 255, 0]
C = [0, 255, 255]
M = [255, 255, 255]
X = [0, 0, 0]
W = [255, 255, 255]

TEST = [
W, R, G, B, Y, C, M, X,
W, R, G, B, Y, C, M, X,
W, R, G, B, Y, C, M, X,
W, R, G, B, Y, C, M, X,
W, R, G, B, Y, C, M, X,
W, R, G, B, Y, C, M, X,
W, R, G, B, Y, C, M, X,
W, R, G, B, Y, C, M, X
]

EXCLAIM = [
	X, X, X, W, W, X, X, X,
	X, X, X, W, W, X, X, X,
	X, X, X, W, W, X, X, X,
	X, X, X, W, W, X, X, X,
	X, X, X, W, W, X, X, X,
	X, X, X, X, X, X, X, X,
	X, X, X, W, W, X, X, X,
	X, X, X, W, W, X, X, X
	]



def display_message(message):
	sense.show_message(message)

def display_error():
	pass

def display_warning():
	WARNING = [
		X, Y, X, Y, X, Y, X, Y,
		Y, X, Y, X, Y, X, Y, X,
		X, Y, X, Y, X, Y, X, Y,
		Y, X, Y, X, Y, X, Y, X,
		X, Y, X, Y, X, Y, X, Y,
		Y, X, Y, X, Y, X, Y, X,
		X, Y, X, Y, X, Y, X, Y,
		Y, X, Y, X, Y, X, Y, X
		]

	for pos in range(10):
		sign = np.roll(WARNING, pos * 8 * 3)
		sign = np.add(sign, EXCLAIM)
		sign = np.clip(sign, a_min=0, a_max=255)

		display_sign(sign)
		time.sleep(0.1)


def display_sign(sign):
	sense.set_pixels(sign)

def set_low_light(enabled=True):
	sense.low_light = enabled

def clear():
	sense.clear()
