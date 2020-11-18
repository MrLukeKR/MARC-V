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

# 30FPS @ 2592x1944
# 60FPS @ 1280x720
# 90FPS @ 640x480
resolution = (640, 480)

camera.resolution = resolution
camera.framerate = 90
rawCapture = PiRGBArray(camera, size=resolution)
curr_pan = 0
curr_tilt = 65

def get_stream():
	return camera.capture_continuous(rawCapture, format="bgr", use_video_port=True), rawCapture

def get_image():
	camera.capture(rawCapture, format="bgr")
	return rawCapture.array

def detect_faces(image):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(greyscale, 1.1, 4)
    
    return faces

def draw_face_bounding_boxes(image, faces):
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return image

def recognise_face():
    pass

def control_camera():
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        return True
    elif key == ord("w"):
        print("Moving UP")
        move(Direction["UP"])
    elif key == ord("W"):
        print("Setting Position to UP")
        set_orientation(Orientation["UP"])
    elif key == ord("s"):
        print("Moving DOWN")
        move(Direction["DOWN"])
    elif key == ord("S"):
        print("Setting Position to DOWN")
        set_orientation(Orientation["DOWN"])
    elif key == ord("a"):
        print("Moving LEFT")
        move(Direction["LEFT"])
    elif key == ord("A"):
        print("Setting Position to LEFT")
        set_orientation(Orientation["LEFT"])
    elif key == ord("d"):
        print("Moving RIGHT")
        move(Direction["RIGHT"])
    elif key == ord("D"):
        print("Setting Position to RIGHT")
        set_orientation(Orientation["RIGHT"])
    elif key == ord(" "):
        print("Resetting Camera")
        reset()
    return False

def run_vision_loop():
    stream, rawCapture = get_stream()
    
    for frame in stream:
        image = frame.array
        
        faces = detect_faces(image)
        image = draw_face_bounding_boxes(image, faces)
        cv2.imshow("MARC-V Main Camera", image)
        size = (8,8)
        
        rawCapture.truncate(0)
        
        if control_camera():
            break

def show_camera():
    stream, rawCapture = get_stream()
    
    for frame in stream:
        image = frame.array
        cv2.imshow("MARC-V Main Camera", image)
        size = (8,8)
        
        rawCapture.truncate(0)
        img = Image.fromarray(image)
        img = img.resize(size, Image.ANTIALIAS)
        
        img = np.asarray(img)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.reshape(img, (64, 3))
        disp.display_sign(img)
        
        if control_camera():
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
