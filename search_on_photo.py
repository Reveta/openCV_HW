import cv2
import numpy as np


def get_extreme_points(image):
    height, width = image.shape[:2]
    w_left = width
    w_right = 0
    h_up = height
    h_down = 0

    for x in range(width -1):
        for y in range(height -1):
            b, g, r = image[y, x]
            sum = int(b) + int(g) + int(r)
            if sum > 0:
                if x > w_right:
                    w_right = x
                if x < w_left:
                    w_left = x
                if y > h_down:
                    h_down = y
                if y < h_up:
                    h_up = y

    p1 = (w_left, h_up)
    p2 = (w_right, h_up)
    p3 = (w_right, h_down)
    p4 = (w_left, h_down)

    return p1, p2, p3, p4


def draw_border_in_mask(image, mask):
    points = get_extreme_points(mask)

    pin_1 = points[0]
    pin_2 = points[1]
    pin_3 = points[2]
    pin_4 = points[3]

    cv2.line(image, pin_1, pin_2, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
    cv2.line(image, pin_2, pin_3, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
    cv2.line(image, pin_3, pin_4, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
    cv2.line(image, pin_4, pin_1, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)

    return image


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


def get_mask_by(image_bgr, color_rgb, color_format):
    image = cv2.cvtColor(image_bgr, color_format)
    thresh = 40

    color = cv2.cvtColor(np.uint8([[color_rgb]]), color_format)[0][0]
    min = np.array([color[0] - thresh, color[1] - thresh, color[2] - thresh])
    max = np.array([color[0] + thresh, color[1] + thresh, color[2] + thresh])
    maskBGR = cv2.inRange(image, min, max)

    return maskBGR


def find_on(image_bgr, color_rgb):
    maskLAB = get_mask_by(image_bgr, color_rgb, cv2.COLOR_BGR2LAB)
    maskYCB = get_mask_by(image_bgr, color_rgb, cv2.COLOR_BGR2YCrCb)
    maskHSV = get_mask_by(image_bgr, color_rgb, cv2.COLOR_BGR2HSV)

    result = bitwise(image_bgr, maskLAB, cv2.COLOR_BGR2LAB)
    result = bitwise(image_bgr, maskHSV, cv2.COLOR_HSV2RGB)
    # result = bitwise(result, maskYCB, cv2.COLOR_YUV2BGR)

    return result


def bitwise(image_bgr, mask, color_format):
    image = cv2.cvtColor(image_bgr, color_format)
    return cv2.bitwise_and(image, image, mask=mask)


rgb = [72, 120, 224]

image_1 = cv2.imread('media/laptops/laptop_1.jpg')
image_2 = cv2.imread('media/laptops/laptop_2.jpg')
image_3 = cv2.imread('media/laptops/laptop_3.jpg')


founded_1 = find_on(image_1, rgb)
result_1 = resize_photo(
    draw_border_in_mask(image_1, founded_1),
    1280,
    720)

founded_2 = find_on(image_2, rgb)
result_2 = resize_photo(
    draw_border_in_mask(image_2, founded_2),
    1280,
    720)

founded_3 = find_on(image_3, rgb)
result_3 = resize_photo(
    draw_border_in_mask(image_3, founded_3),
    1280,
    720)

cv2.imshow("result1", result_1)
cv2.imshow("result2", result_2)
cv2.imshow("result3", result_3)

cv2.waitKey()
cv2.destroyAllWindows()
