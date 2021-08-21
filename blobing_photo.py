# !/usr/bin/python

# Standard imports
import cv2
import numpy as np

# Read image
# image_original = cv2.imread("media/blobs/blob.jpg", cv2.IMREAD_GRAYSCALE)
image_original = cv2.imread("media/blobs/microchips_1.png", cv2.IMREAD_COLOR)
# image_original = cv2.imread("media/blobs/microchips_2.png", cv2.IMREAD_COLOR)

th, image = cv2.threshold(image_original, 150, 255, cv2.THRESH_BINARY)
image = cv2.medianBlur(src=image, ksize=3)
image = cv2.bitwise_not(image)
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 150
params.maxThreshold = 255

# params.filterByColor = True
# params.blobColor = 203

# Filter by Area.
# params.filterByArea = True
# params.minArea = 100
#
# Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.7

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(image)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
th, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
im_with_keypoints = cv2.drawKeypoints(image_original, keypoints, np.array([]), (0, 0, 255),
                                      cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

down_width = 800
down_height = 800
down_points = (down_width, down_height)
image_original = cv2.resize(image_original, down_points, interpolation= cv2.INTER_LINEAR)
im_with_keypoints = cv2.resize(im_with_keypoints, down_points, interpolation= cv2.INTER_LINEAR)

# Show blobs
cv2.imshow("original", image_original)
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
