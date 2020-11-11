#!/usr/bin/python

import math
import time
import RPi.GPIO as GPIO
import pyttsx3
import Camera as cam
import Display as disp

from time import sleep
from sense_hat import SenseHat
import pantilthat as pt
from picamera import PiCamera

engine = pyttsx3.init()
sense = SenseHat()

GPIO.setmode(GPIO.BCM)


def main():
	#M1_F = 17
	#M1_B = 18
	#M2_F = 22
	#M2_B = 23

	#GPIO.setup(M1_F, GPIO.OUT)
	#GPIO.setup(M1_B, GPIO.OUT)
	#GPIO.setup(M2_F, GPIO.OUT)
	#GPIO.setup(M2_B, GPIO.OUT)

	#m1f = GPIO.PWM(M1_F, 200)
	#m1b = GPIO.PWM(M1_B, 200)
	#m2f = GPIO.PWM(M2_F, 200)
	#m2b = GPIO.PWM(M2_B, 200)

	cam.reset()
	disp.set_low_light()
	#m1f.ChangeDutyCycle(100)
	#m2f.ChangeDutyCycle(100)

	#m1f.stop()
	#m2f.stop()

	GPIO.cleanup()
	disp.display_warning()


def say(message):
	engine.say(message)
	engine.runAndWait()

def run_tests():
	test_pantilt()

def test_pantilt():
	say("Testing pan and tilt module")
	for direction in ["LEFT", "UP", "RIGHT", "DOWN", "FORWARD"]:
		print(direction)
		say(direction)
		disp.display_message(direction)
		cam.set_direction(cam.Direction[direction])


if __name__ == "__main__":
    main()
