import cv2
import numpy as np

def draw_border(image):
    height, width = image.shape[:2]
    width = width - 1
    height = height - 1

    pin_1 = (1,1)
    pin_2 = (width,1)
    pin_3 = (width,height)
    pin_4 = (1,height)

    cv2.line(image, pin_1, pin_2, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    cv2.line(image, pin_2, pin_3, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    cv2.line(image, pin_3, pin_4, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    cv2.line(image, pin_4, pin_1, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)

    return image


bright = cv2.imread('media/laptops/laptop_1.jpg')
dark = cv2.imread('media/color_test_2.jpg')

down_width = 800
down_height = 600
down_points = (down_width, down_height)
bright = cv2.resize(bright, down_points, interpolation= cv2.INTER_LINEAR)
dark = cv2.resize(dark, down_points, interpolation= cv2.INTER_LINEAR)


brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)

darkLAB = cv2.cvtColor(dark, cv2.COLOR_BGR2LAB)
brightYCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)

darkYCB = cv2.cvtColor(dark, cv2.COLOR_BGR2YCrCb)
brightHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)


darkHSV = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)
# rgb = [96,8,32]
rgb = [234, 78, 60]

bgr = cv2.cvtColor( np.uint8([[rgb]] ), cv2.COLOR_RGB2BGR)[0][0]

thresh = 40
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

maskBGR = cv2.inRange(bright,minBGR,maxBGR)

resultBGR = cv2.bitwise_and(bright, bright, mask = maskBGR)
#convert 1D array to 3D, then convert it to HSV and take the first element
# this will be same as shown in the above figure [65, 229, 158]

hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])

maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)

resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask = maskHSV)
#convert 1D array to 3D, then convert it to YCrCb and take the first element

ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]
minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])

maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])
maskYCB = cv2.inRange(brightYCB, minYCB, maxYCB)

resultYCB = cv2.bitwise_and(brightYCB, brightYCB, mask = maskYCB)
#convert 1D array to 3D, then convert it to LAB and take the first element

lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])

maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)

resultLAB = cv2.bitwise_and(bright, bright, mask = maskLAB)
resultLAB = cv2.bitwise_and(resultLAB, resultLAB, mask = maskYCB)
resultLAB = cv2.bitwise_and(resultLAB, resultLAB, mask = maskHSV)
resultLAB = cv2.bitwise_and(resultLAB, resultLAB, mask = maskBGR)

cv2.imshow("Original", draw_border(bright))

# cv2.imshow("Result BGR", draw_border(resultBGR))
# cv2.imshow("Result HSV", draw_border(resultHSV))
# cv2.imshow("Result YCB", draw_border(resultYCB))

cv2.imshow("Output LAB", resultLAB)
cv2.waitKey()

cv2.destroyAllWindows()