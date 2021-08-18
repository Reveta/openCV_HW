import cv2
import numpy as np

image = cv2.imread('media/filtering_color_test.jpg')

# Print error message if image is null
if image is None:
    print('Could not read image')

# Apply identity kernel
kernel1 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

identity1 = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
identity2 = cv2.filter2D(src=identity1, ddepth=-1, kernel=kernel1)
identity3 = cv2.filter2D(src=identity2, ddepth=-1, kernel=kernel1)

cv2.imshow('Original', image)
cv2.imshow('Identity1', identity1)
cv2.imshow('Identity2', identity2)
cv2.imshow('Identity2', identity3)

cv2.waitKey()
cv2.imwrite('identity.jpg', identity1)
cv2.destroyAllWindows()

cv2.waitKey()
cv2.destroyAllWindows()
