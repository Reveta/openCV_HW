import cv2

image = cv2.imread('media/laptops/laptop_1.jpg')

trans = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
trans = cv2.cvtColor(trans, cv2.COLOR_BGR2LAB)
trans = cv2.cvtColor(trans, cv2.COLOR_LAB2BGR)
trans = cv2.cvtColor(trans, cv2.COLOR_BGR2HSV)
trans = cv2.cvtColor(trans, cv2.COLOR_HSV2RGB)
trans = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
trans = cv2.cvtColor(trans, cv2.COLOR_BGR2LAB)
trans = cv2.cvtColor(trans, cv2.COLOR_LAB2BGR)
trans = cv2.cvtColor(trans, cv2.COLOR_BGR2HSV)
trans = cv2.cvtColor(trans, cv2.COLOR_HSV2RGB)
trans = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
trans = cv2.cvtColor(trans, cv2.COLOR_BGR2LAB)
trans = cv2.cvtColor(trans, cv2.COLOR_LAB2BGR)
trans = cv2.cvtColor(trans, cv2.COLOR_BGR2HSV)
trans = cv2.cvtColor(trans, cv2.COLOR_HSV2RGB)
trans = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
trans = cv2.cvtColor(trans, cv2.COLOR_BGR2LAB)
trans = cv2.cvtColor(trans, cv2.COLOR_LAB2BGR)
trans = cv2.cvtColor(trans, cv2.COLOR_BGR2HSV)
trans = cv2.cvtColor(trans, cv2.COLOR_HSV2RGB)

cv2.imshow("original", image)
cv2.imshow("trans", trans)

cv2.waitKey()
