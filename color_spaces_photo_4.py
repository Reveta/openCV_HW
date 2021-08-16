import cv2
import numpy as np


def get_mask_by(image_rgb, color_rgb, color_format):
    image = cv2.cvtColor(image_rgb, color_format)
    thresh = 40

    color = cv2.cvtColor(np.uint8([[color_rgb]]), color_format)[0][0]
    min = np.array([color[0] - thresh, color[1] - thresh, color[2] - thresh])
    max = np.array([color[0] + thresh, color[1] + thresh, color[2] + thresh])
    maskBGR = cv2.inRange(image, min, max)

    return maskBGR


image = cv2.imread('media/color_test_1.jpg')

down_width = 800
down_height = 600
down_points = (down_width, down_height)
image = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

rgb = [234, 78, 60]
thresh = 40


hsv = cv2.cvtColor( np.uint8([[rgb]] ), cv2.COLOR_RGB2BGR)[0][0]
brightHSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
maskHSV_1 = cv2.inRange(brightHSV, minHSV, maxHSV)

maskHSV_2 = get_mask_by(image, rgb, cv2.COLOR_RGB2BGR)

cv2.imshow("org", image)
cv2.imshow("mask1", maskHSV_1)
cv2.imshow("mask2", maskHSV_2)

cv2.waitKey()
