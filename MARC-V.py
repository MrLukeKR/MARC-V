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
    disp.set_low_light()
    cam.run_vision_loop()
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
