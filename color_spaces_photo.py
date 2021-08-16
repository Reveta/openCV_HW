import cv2

image = cv2.imread('media/test.jpg', cv2.IMREAD_COLOR)
image_split = cv2.split(image)
cv2.imshow("image_1", image_split[0])
cv2.imshow("image_2", image_split[1])
cv2.imshow("image_3", image_split[2])
cv2.waitKey()

image_cvt = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
image_split = cv2.split(image_cvt)
cv2.imshow("image_1", image_split[0])
cv2.imshow("image_2", image_split[1])
cv2.imshow("image_3", image_split[2])
cv2.waitKey()

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_split = cv2.split(image_hsv)
cv2.imshow("image_1", image_split[0])
cv2.imshow("image_2", image_split[1])
cv2.imshow("image_3", image_split[2])
cv2.waitKey()

image_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
image_split = cv2.split(image_YCrCb)
cv2.imshow("image_1", image_split[0])
cv2.imshow("image_2", image_split[1])
cv2.imshow("image_3", image_split[2])
cv2.waitKey()

cv2.destroyAllWindows()