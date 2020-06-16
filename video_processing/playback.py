# usage: python playback.py --video <PATH_TO_VIDEO>

''' OpenCV isn't built to playback video files. 
When we try to display a video, if the video has low FPS, it appears as if it is being played at 2x or more.
This program is an attempt to introduce delay between frames so that the video playback appears "normal" '''

# import necessary packages
import cv2
import argparse

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path to input video")
args = vars(ap.parse_args())

# create a VideoCapture object and read from the input file
vid = cv2.VideoCapture(args["video"])
fps = cv2.CAP_PROP_FPS

# calculate delay necessary (in milliseconds)
delay = int(1/fps * 100)

# check if video is read successfully
if vid.isOpened()==False:
	print("Error opening video file")

# read and display until video is completed
while vid.isOpened():
	grabbed, frame = vid.read()
	if not grabbed:
		break
	else:
		cv2.waitKey(delay)
		cv2.imshow("Frame", frame)

# release video capture object
vid.release()

# destroy all windows
cv2.destroyAllWindows()