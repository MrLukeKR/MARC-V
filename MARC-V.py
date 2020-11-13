#!/usr/bin/python

import math
import time
import RPi.GPIO as GPIO
import pyttsx3
import Camera as cam
import Display as disp
import cv2
import numpy as np

from PIL import Image
from time import sleep
from sense_hat import SenseHat
import pantilthat as pt
from picamera import PiCamera

engine = pyttsx3.init()
sense = SenseHat()

GPIO.setmode(GPIO.BCM)

ML_F = 17
ML_B = 18
MR_F = 22
MR_B = 23

GPIO.setup(ML_F, GPIO.OUT)
GPIO.setup(ML_B, GPIO.OUT)
GPIO.setup(MR_F, GPIO.OUT)
GPIO.setup(MR_B, GPIO.OUT)

def main():

	#m1f = GPIO.PWM(M1_F, 200)
	#m1b = GPIO.PWM(M1_B, 200)
	#m2f = GPIO.PWM(M2_F, 200)
	#m2b = GPIO.PWM(M2_B, 200)

	cam.reset()
	stream, rawCapture = cam.get_stream()

	for frame in stream:
		image = frame.array
		cv2.imshow("MARC-V Main Camera", image)
		size = (8,8)

		key = cv2.waitKey(1) & 0xFF
		rawCapture.truncate(0)
	
		if key == ord("q"):
			break
		elif key == ord("w"):
			print("Moving UP")
			cam.move(cam.Direction["UP"])
		elif key == ord("W"):
			print("Setting Position to UP")
			cam.set_orientation(cam.Orientation["UP"])
		elif key == ord("s"):
			print("Moving DOWN")
			cam.move(cam.Direction["DOWN"])
		elif key == ord("S"):
			print("Setting Position to DOWN")
			cam.set_orientation(cam.Orientation["DOWN"])
		elif key == ord("a"):
			print("Moving LEFT")
			cam.move(cam.Direction["LEFT"])
		elif key == ord("A"):
			print("Setting Position to LEFT")
			cam.set_orientation(cam.Orientation["LEFT"])
		elif key == ord("d"):
			print("Moving RIGHT")
			cam.move(cam.Direction["RIGHT"])
		elif key == ord("D"):
			print("Setting Position to RIGHT")
			cam.set_orientation(cam.Orientation["RIGHT"])
		elif key == ord(" "):
			print("Resetting Camera")
			cam.reset()
		else:
			img = Image.fromarray(image)
			img = img.resize(size, Image.ANTIALIAS)

			img = np.asarray(img)
	
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			img = np.reshape(img, (64, 3))
			disp.display_sign(img)
		


	disp.set_low_light()
	#m1f.ChangeDutyCycle(100)
	#m2f.ChangeDutyCycle(100)

	#m1f.stop()
	#m2f.stop()

	disp.display_warning()
	disp.clear()
	GPIO.cleanup()



def say(message):
	engine.say(message)
	engine.runAndWait()

def run_tests():
	test_pantilt()

def test_pantilt():
	say("Testing pan and tilt module")
	for orientation in ["LEFT", "UP", "RIGHT", "DOWN", "FORWARD"]:
		print(orientation)
		say(orientation)
		disp.display_message(orientation)
		cam.set_direction(cam.Orientation[orientation])


if __name__ == "__main__":
    main()
