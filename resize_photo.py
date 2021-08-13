import cv2
import numpy as np

# Read the image using imread function
image = cv2.imread('media/test.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Original Image', image)

# Get original height and width
h,w,c = image.shape
print("Original Height and Width:", h,"x", w)

# let's downscale the image using new  width and height
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

# let's upscale the image using new  width and height
up_width = 400
up_height = 600
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation= cv2.INTER_LINEAR)

# Display images
cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey()
cv2.imshow('Resized Up image by defining height and width', resized_up)
cv2.waitKey()

# Scaling Up the image 1.2 times by specifying both scaling factors
scale_up_x = 1.2
scale_up_y = 1.2
# Scaling Down the image 0.6 times specifying a single scale factor.
scale_down = 0.6

scaled_f_down = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(image, None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)

cv2.imshow("scaled_f_up", scaled_f_up)
cv2.imshow("scaled_f_down", scaled_f_down)

cv2.waitKey()
#press any key to close the windows
cv2.destroyAllWindows()