# usage: python save_all_frames.py --video <PATH_TO_INPUT_VIDEO> --output <PATH_TO_OUTPUT_FOLDER>

# import necessary packages
import cv2
import argparse

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path to input video")
ap.add_argument("-o", "--output", required=True, help="Path to output folder")
args = vars(ap.parse_args())

# function to write all frames to folder
def save_frames(input_video, ouput_folder):
	# read the input video
	vid = cv2.VideoCapture(input_video)
	# save all frames to folder
	filename = output_folder+"frame_{}.jpg"
	frame_number = 0

	while True:
		grabbed, frame = vid.read()
		if grabbed:
			cv2.imwrite(filename.format(frame_number), frame)
			if frame_number%100 == 0:
				print("[INFO] Written {} frames.".format(frame_number))
			frame_number += 1
		else:
			print("[INFO] All frames written to {}".format(output_folder))
			break

input_video = args["video"]
# add "/" to end of output path if needed
if args["output"][-1] != "/":
	output_folder = args["output"]+"/"
else:
	output_folder = args["output"]

save_frames(input_video, output_folder)



