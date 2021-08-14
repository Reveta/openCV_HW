import cv2

image = cv2.imread('media/test.jpg', cv2.IMREAD_COLOR)
image = cv2.resize(image, (500, 500), cv2.INTER_LINEAR)
cv2.imshow('Original Image', image)
print(image.shape)

imgheight = image.shape[1]
imgwidth = image.shape[0]

M = imgheight // 3
N = imgwidth // 3
x1 = 0
y1 = 0

for y in range(0, imgheight, M):
    for x in range(0, imgwidth, N):
        if (imgheight - y) < M or (imgwidth - x) < N:
            break

        y1 = y + M
        x1 = x + N

        # check whether the patch width or height exceeds the image width or height
        if x1 >= imgwidth and y1 >= imgheight:
            x1 = imgwidth - 1
            y1 = imgheight - 1
            # Crop into patches of size MxN
            tiles = image[y:y + M, x:x + N]
            # Save each patch into file directory
            cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 >= imgheight:  # when patch height exceeds the image height
            y1 = imgheight - 1
            # Crop into patches of size MxN
            tiles = image[y:y + M, x:x + N]
            # Save each patch into file directory
            cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= imgwidth:  # when patch width exceeds the image width
            x1 = imgwidth - 1
            # Crop into patches of size MxN
            tiles = image[y:y + M, x:x + N]
            # Save each patch into file directory
            cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            # Crop into patches of size MxN
            tiles = image[y:y + M, x:x + N]
            # Save each patch into file directory
            cv2.imwrite('saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)


# Save full image into file directory
cv2.imshow("Patched Image", image)
cv2.imwrite("media/patched.jpg", image)

cv2.waitKey()
cv2.destroyAllWindows()