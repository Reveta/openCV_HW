import cv2

image_origin = cv2.imread('media/test.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Original Image', image_origin)

coof_up = 2.0
resize_line = cv2.resize(image_origin, None, fx=coof_up, fy=coof_up, interpolation=cv2.INTER_LINEAR)
resize_area = cv2.resize(image_origin, None, fx=coof_up, fy=coof_up, interpolation=cv2.INTER_AREA)
resize_nearest = cv2.resize(image_origin, None, fx=coof_up, fy=coof_up, interpolation=cv2.INTER_NEAREST)
resize_cubic = cv2.resize(image_origin, None, fx=coof_up, fy=coof_up, interpolation=cv2.INTER_CUBIC)

cv2.imshow("resize_line", resize_line)
cv2.imshow("resize_area", resize_area)
cv2.imshow("resize_nearest", resize_nearest)
cv2.imshow("resize_cubic", resize_cubic)

cv2.waitKey()
