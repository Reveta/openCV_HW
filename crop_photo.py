import cv2

image = cv2.imread('media/test.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Original Image', image)
print(image.shape)

cv2.waitKey()
cv2.destroyAllWindows()

# cropped_image = image[80:280, 150:330]
cropped_image_1 = image[10:130, 10:130]
cropped_image_2 = image[130:270, 10:130]
cropped_image_3 = image[10:130, 130:270]
cropped_image_4 = image[130:270, 130:270]
# cropped_image_2 = image[300:1000, 150:330]
cv2.imshow("1", cropped_image_1)
cv2.imshow("2", cropped_image_2)
cv2.imshow("3", cropped_image_3)
cv2.imshow("4", cropped_image_4)
# cv2.imshow("cropped_photo_2", cropped_image_2)
# print(cropped_image.shape)
# print(cropped_image_2.shape)

cv2.waitKey()
cv2.destroyAllWindows()
