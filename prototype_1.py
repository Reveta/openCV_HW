import cv2
import numpy as np


def resize_photo(image, width, height):
    down_points = (width, height)
    image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
    return image

def processing(image_original):
    image = image_original
    th, image = cv2.threshold(image_original, 100, 255, cv2.THRESH_BINARY)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    image = cv2.filter2D(image, -1, kernel)

    # image = cv2.medianBlur(src=image, ksize=5)
    image = cv2.bitwise_not(image)
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    # params.minThreshold = 150
    params.maxThreshold = 255

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 400

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.01

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

    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # th, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)

    image = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
    im_with_keypoints = cv2.drawKeypoints(image_original, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

    return image, im_with_keypoints

# vid_capture = cv2.VideoCapture("media/project/proj_1/Chip_%03d.tif")
vid_capture = cv2.VideoCapture("media/project/proj_2/Chip_%03d.jpg")

while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if not ret:
        break

    mask, result = processing(frame)
    mask = resize_photo(mask, 950, 740)
    result = resize_photo(result, 950, 740)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    cv2.waitKey()
