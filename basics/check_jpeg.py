'''
save names, count and format of images that are not of type "jpeg" to output file

Usage: python check_jpeg.py --location <ABSOLUTE_PATH_TO_IMAGES_FOLDER> --output <NAME_OF_OUTPUT_FILE.EXTENSION>

'''

 

import argparse

import glob

import imghdr

 

# get location and output argument

ap = argparse.ArgumentParser()

ap.add_argument("-l", "--location", required=True, help="Complete path to images folder")

ap.add_argument("-o", "--output", required=True, help="Name of output file")

args = vars(ap.parse_args())

 

# correct location string if necessary

location, output_file = args["location"], args["output"]

if location[-1] != "/":

                location += "/"

 

# get absolute paths to all images

images = glob.glob(location+"*")

non_JPEG = {}  # "img-type": ["img1.extension", "img2.extension", .., "imgN.extension"]

 

# append non-JPEG images to their respective types

for img in images:

    img_type = imghdr.what(img)

    # ignore "csv" files      

    if img[-3:] == "csv":

        continue

    if img_type != "jpeg":

        # add to dictionary

        if img_type not in non_JPEG:

            non_JPEG[img_type] = [img.split("/")[-1]]

        else:

            non_JPEG[img_type].append(img.split("/")[-1])

 

# create a list of non JPEG images (flattening)

non_JPEG_images = []

for img_list in non_JPEG.values():

                non_JPEG_images += img_list

 

# write results to a file

with open(output_file, "w+") as file:

                file.write("Images folder: {}\n".format(location))

                file.write("\nnon-JPEG image types present: {}\n".format(non_JPEG.keys()))

                file.write("\n# of non-JPEG images: {}\n".format(len(non_JPEG_images)))

                file.write("\nList of non-JPEG images:\n")

                for img in non_JPEG_images:

                                file.write(img+"\n")