import colourdescriptor
import argparse
import glob
import cv2

# parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to image directory")
ap.add_argument("-i", "--index", required=True,
                help="Path to storage directory")

args = vars(ap.parse_args())

# initialize color descriptor
cd = colourdescriptor.ColourDescriptor((8, 12, 3))

# open output index file to write to
output = open(args["index"], "w")

# using glob, loop over paths of images
for path in glob.glob(args["dataset"] + "/*.png"):
    # get the image file name from path
    # load the image
    imageID = path[path.rfind("/") + 1:]
    image = cv2.imread(path)

    # get the image features
    features = cd.describe(image)

    # write features onto a file
    features = [str(f) for f in features]
    output.write("%s, %s\n" % (imageID, ",".join(features)))

# close outpte index file
output.close()
