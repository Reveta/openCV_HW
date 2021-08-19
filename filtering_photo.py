import cv2
import numpy as np

image = cv2.imread('media/SARS-CoV-2_EM.jpg')

# Print error message if image is null
if image is None:
    print('Could not read image')

# Apply identity kernel
kernel1 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

kernel11 = np.array([[0, 0.2, 0],
                    [0.2, 0.2, 0.2],
                    [0, 0.2, 0]])

identity1 = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
identity2 = cv2.bilateralFilter(src=image, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imshow('Original', image)
cv2.imshow('Identity1', identity1)
cv2.imshow('Identity2', identity2)
# cv2.imshow('Identity3', identity3)

cv2.waitKey()
cv2.imwrite('media/identity.jpg', identity1)
cv2.destroyAllWindows()

# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)

cv2.waitKey()
cv2.imwrite('media/blur_kernel.jpg', img)
cv2.destroyAllWindows()
