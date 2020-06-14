# usage: python get_video_stats.py --video <PATH_TO_VIDEO>

# import necessary libraries
import cv2
import argparse

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path to video file")
args = vars(ap.parse_args())

# function to get video stats
def video_stats(video):
	vid = cv2.VideoCapture(video)
	frame_width, frame_height, fps = int(vid.get(3)), int(vid.get(4)), round(vid.get(cv2.CAP_PROP_FPS))
	return {'width':frame_width, 'height':frame_height, 'fps':fps}

video_path = args["video"]
video_name = video_path.split("/")[-1]

stats = video_stats(video_path)

print("\nStats for {}:\n".format(video_name))
for item in stats:
	print("{} --> {}".format(item, stats[item]))