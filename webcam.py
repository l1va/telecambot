#!/usr/bin/python3
import signal
import traceback
import cv2
import time
import logging
import os
repeat = True

def exit_gracefully(signum, frame):
    global repeat
    repeat = False


def infinite_webcam():


	try:
		webcam = cv2.VideoCapture(-1)
		print(webcam)
		while repeat:
			ok, img = webcam.read()
			if ok:
				cv2.imwrite("img.png", img)
			else:
				print("failed to read image")
				break
			time.sleep(5)
			# to skip cache: the av-based linux capture code is using an internal fifo (5 frames, iirc) (c)
			for j in range(1, 10):
				webcam.read()

		webcam.release()
		cv2.destroyAllWindows()
		time.sleep(5)

		print("webcam done")
	except Exception:
		logging.error("webcam error:" + traceback.format_exc())
		time.sleep(5)


def run_webcam():
    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGTERM, exit_gracefully)
    infinite_webcam()


if __name__ == "__main__":
    while True:
	        run_webcam()
