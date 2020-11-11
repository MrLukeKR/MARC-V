#!/usr/bin/python

from picamera import PiCamera
import pantilthat as pt
import math
import time
import RPi.GPIO as GPIO
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

M1_F = 17
M1_B = 18
M2_F = 22
M2_B = 23

sense.show_message("Hello world!")
GPIO.setup(M1_F, GPIO.OUT)
GPIO.setup(M1_B, GPIO.OUT)
GPIO.setup(M2_F, GPIO.OUT)
GPIO.setup(M2_B, GPIO.OUT)

m1f = GPIO.PWM(M1_F, 200)
m1b = GPIO.PWM(M1_B, 200)
m2f = GPIO.PWM(M2_F, 200)
m2b = GPIO.PWM(M2_B, 200)

camera = PiCamera()
camera.rotation = 180

camera.start_preview(alpha=200)
pt.tilt(45)

m1f.ChangeDutyCycle(100)
m2f.ChangeDutyCycle(100)

m1f.stop()
m2f.stop()


while True:
	t = time.time()
	a = math.sin(t * 2) * 90
	a = int(a)
	pt.pan(a)

GPIO.cleanup()

