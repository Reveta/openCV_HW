import cv2
import numpy as np


def draw_border(image):
    height, width = image.shape[:2]
    width = width - 1
    height = height - 1

    pin_1 = (1, 1)
    pin_2 = (width, 1)
    pin_3 = (width, height)
    pin_4 = (1, height)

    cv2.line(image, pin_1, pin_2, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    cv2.line(image, pin_2, pin_3, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    cv2.line(image, pin_3, pin_4, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    cv2.line(image, pin_4, pin_1, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA)

    return image


def resize_photo(image, width, height):
    down_points = (width, height)
    image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
    return image


def get_mask_by(image_rgb, color_rgb, color_format):
    image = cv2.cvtColor(image_rgb, color_format)
    thresh = 40


    color = cv2.cvtColor(np.uint8([[color_rgb]]), color_format)[0][0]
    min = np.array([color[0] - thresh, color[1] - thresh, color[2] - thresh])
    max = np.array([color[0] + thresh, color[1] + thresh, color[2] + thresh])
    maskBGR = cv2.inRange(image, min, max)

    cv2.imshow("find_on", resize_photo(maskBGR, 1920, 1020))
    return maskBGR


def find_on(image_rgb, color_rgb):
    maskBGR = get_mask_by(image_rgb, color_rgb, cv2.COLOR_RGB2BGR)
    maskLAB = get_mask_by(image_rgb, color_rgb, cv2.COLOR_RGB2LAB)
    maskYCB = get_mask_by(image_rgb, color_rgb, cv2.COLOR_RGB2YCrCb)
    maskHSV = get_mask_by(image_rgb, color_rgb, cv2.COLOR_RGB2HSV)

    result = bitwise(image_rgb, maskBGR, cv2.COLOR_RGB2BGR)
    # result = bitwise(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), maskLAB, cv2.COLOR_RGB2LAB)
    # result = bitwise(cv2.cvtColor(result, cv2.COLOR_LAB2RGB), maskHSV, cv2.COLOR_RGB2HSV)
    # result = bitwise(cv2.cvtColor(result, cv2.COLOR_HSV2RGB), maskYCB, cv2.COLOR_RGB2YCrCb)

    return cv2.cvtColor(result, cv2.COLOR_YUV2RGB)


def bitwise(image_rgb, mask, color_format):
    image = cv2.cvtColor(image_rgb, color_format)
    cv2.imshow("bitwise", image)
    return cv2.bitwise_and(image, image, mask=mask)


rgb = [72, 120, 224]

image_1 = cv2.imread('media/laptops/laptop_1.jpg')
image_2 = cv2.imread('media/laptops/laptop_2.jpg')
image_3 = cv2.imread('media/laptops/laptop_3.jpg')

founded_1 = find_on(image_1, rgb)
result_1 = resize_photo(
    draw_border(founded_1),
    1920,
    1020
)

cv2.imshow("result", result_1)

cv2.waitKey()
cv2.destroyAllWindows()
