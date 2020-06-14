# usage: python compute_frames.py --video <PATH_TO_VIDEO>

# import necessary libraries
import cv2
import argparse

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path to video file")
args = vars(ap.parse_args())

# function to get frame count
def count_frames(video):
	vid = cv2.VideoCapture(video)
	num_frames = 0
	while True:
		grabbed, frame = vid.read()
		if not grabbed:
			break
		num_frames+=1
	return num_frames

video_path = args["video"]
video_name = video_path.split("/")[-1]

frame_count = count_frames(video_path)

print("{} has {} frames".format(video_name, frame_count))