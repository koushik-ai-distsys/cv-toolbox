# usage: python convert_to_grayscale.py --video <PATH_TO_INPUT_VIDEO> --output <PATH_TO_OUTPUT_VIDEO>

# import necessary packages
import cv2
import argparse

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path to input video")
ap.add_argument("-o", "--output", required=True, help="Path to save output")
args = vars(ap.parse_args())

# function to convert video to grayscale
def cvt2gray(input_video, output_video):
	# read the input video
	vid = cv2.VideoCapture(input_video)
	# we want the output video to have the same properties as input video
	width, height, fps = int(vid.get(3)), int(vid.get(4)), round(vid.get(cv2.CAP_PROP_FPS))
	# define the codec and create a VideoWriter object. The output is stored in "output_video" file
	out = cv2.VideoWriter(output_video, 
						  cv2.VideoWriter_fourcc(*'mp4v'),
						  fps,
						  (width, height),
						  0)

	count = 0
	# convert each frame to grayscale and write
	while True:
		grabbed, frame = vid.read()
		if grabbed:
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			out.write(frame)
			count += 1
			if count%100 == 0:
				print("[INFO] Processed {} frames.".format(count))
		else:
			print("[INFO] Processing done!")
			break

	out.release()


input_video, output_video = args["video"], args["output"]
cvt2gray(input_video, output_video)