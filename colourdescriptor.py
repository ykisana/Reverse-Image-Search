import numpy as np
import cv2
import imutils


class ColourDescriptor:
    def __init__(self, bins):
        # number of bins for histogram (3D HSV Color)
        self.bins = bins

    def describe(self, image):
        # convert image to HSV color space
        # quantify image and initialize features
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []

        # compute center of the image
        (height, width) = image.shape[:2]
        (centerX, centerY) = int(width * 0.5), int(height * 0.5)

        # divide image into regions for features
        # four rectangles (corners) and a central ellipse

        # rectangles(corners)
        rectangles = [(0, centerX, 0, centerY), (centerX, width, 0, centerY),
                      (0, centerX, centerY, height), (0, centerX, centerY, height)]

        # central ellipse
        (x_length, y_length) = (int(width * 0.75) // 2, int(height * 0.75) // 2)
        ellipse_mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.ellipse(ellipse_mask, (centerX, centerY), (x_length, y_length), 0, 0, 360, 255, -1)

        # loop over rectangles
        for (startX, endX, startY, endY) in rectangles:
            # create a mask for each corner of the image
            # without the elliptical center by subtracting it
            corner_mask = np.zeros(image.shape[:2], dtype="uint8")
            cv2.rectangle(corner_mask, (startX, startY), (endX, endY), 255, -1)
            corner_mask = cv2.subtract(corner_mask, ellipse_mask)

            # colours histogram creates from the image and corner mask
            # update the feature vector (for rectangle)
            hist = self.histogram(image, corner_mask)
            features.extend(hist)

        # colours histogram creates from the image and ellipse mask
        # update the feature vector (for ellipse)
        hist = self.histogram(image, ellipse_mask)
        features.extend(hist)

        # return feature vector
        return features

    def histogram(self, image, mask):
        # 3D colour histogram created from masks
        # masks from describe() and bins initialized in constructor
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
                            [0, 180, 0, 256, 0, 256])

        # normalize histogram for OpenCV
        # normalization takes care of different sized images
        # first, if OpenCV versions 2.4 else for 3+
        if imutils.is_cv2():
            hist = cv2.normalize(hist).flatten()

        else:
            hist = cv2.normalize(hist, hist).flatten()

        return hist
