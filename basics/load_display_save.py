import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

# load the image and show some basic information on it
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

# show the image and wait for keypress
cv2.imshow("Input image", image)
cv2.waitKey(0)

# save the image
cv2.imwrite("image_copy.jpg", image)