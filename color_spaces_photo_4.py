import cv2
import numpy as np


def get_mask_by(image_bgr, color_rgb, color_format):
    image = cv2.cvtColor(image_bgr, color_format)
    thresh = 40

    color = cv2.cvtColor(np.uint8([[color_rgb]]), color_format)[0][0]
    min = np.array([color[0] - thresh, color[1] - thresh, color[2] - thresh])
    max = np.array([color[0] + thresh, color[1] + thresh, color[2] + thresh])
    maskBGR = cv2.inRange(image, min, max)

    return maskBGR


image_BGR = cv2.imread("media/laptops/laptop_1.jpg")

down_width = 800
down_height = 600
down_points = (down_width, down_height)
image_BGR = cv2.resize(image_BGR, down_points, interpolation= cv2.INTER_LINEAR)

rgb = [234, 78, 60]
thresh = 40

hsv = cv2.cvtColor( np.uint8([[rgb]] ), cv2.COLOR_RGB2HSV)[0][0]
brightHSV = cv2.cvtColor(image_BGR, cv2.COLOR_RGB2HLS)

minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
maskHSV_1 = cv2.inRange(brightHSV, minHSV, maxHSV)

image_rgb = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2RGB)
maskHSV_2 = get_mask_by(image_rgb, rgb, cv2.COLOR_RGB2BGR)

cv2.imshow("org", image_BGR)
cv2.imshow("mask1", maskHSV_1)
cv2.imshow("mask2", maskHSV_2)

cv2.waitKey()
