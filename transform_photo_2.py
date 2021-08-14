import cv2
import numpy as np

image = cv2.imread('media/test.jpg', cv2.IMREAD_COLOR)

# dividing height and width by 2 to get the center of the image
height, width = image.shape[:2]

# get tx and ty values for translation
# you can specify any value of your choice
tx, ty = width / 4, height / 4

# create the translation matrix using tx and ty, it is a NumPy array
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)

# apply the translation to the image
translated_image = cv2.warpAffine(src=image, M=translation_matrix, dsize=(width, height))

cv2.imshow("transleted_photo", translated_image)

cv2.waitKey()