import cv2
from matplotlib import pyplot as plt

# The function cv2.imread() is used to read an image.
img_grayscale = cv2.imread('media/test.jpg', cv2.IMREAD_COLOR)

# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('graycsale image', img_grayscale)
cv2.imshow('graycsale image 2', img_grayscale)

# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(1000)

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()

plt.imshow(img_grayscale)
plt.imshow(cv2.cvtColor(img_grayscale, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

# The function cv2.imwrite() is used to write an image.
cv2.imwrite('../media/grayscale.jpg', img_grayscale)
