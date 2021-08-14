# Import dependencies
import cv2

# Read Images
image = cv2.imread('media/test.jpg', cv2.IMREAD_COLOR)

# Print error message if image is null
if image is None:
    print('Could not read image')

# Print X
pAZ_1 = (10, 10)
pBZ_1 = (100, 100)

pAZ_2 = (100, 10)
pBZ_2 = (10, 100)

cv2.line(image, pAZ_1, pBZ_1, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.line(image, pAZ_2, pBZ_2, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)

# Print Y
pAY_1 = (120, 10)
pBY_1 = (170, 60)

pAY_2 = (220, 10)
pBY_2 = (140, 100)

cv2.line(image, pAY_1, pBY_1, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.line(image, pAY_2, pBY_2, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)

# Print Z
pAZ_1 = (240, 10)
pBZ_1 = (290, 10)

pAZ_2 = (290, 10)
pBZ_2 = (240, 100)

pAZ_3 = (240, 100)
pBZ_3 = (290, 100)

cv2.line(image, pAZ_1, pBZ_1, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.line(image, pAZ_2, pBZ_2, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.line(image, pAZ_3, pBZ_3, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)

# define the center of circle
circle_center = (55, 55)
# define the radius of the circle
radius = 55
#  Draw a circle using the circle() Function
cv2.circle(image, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)

# define the center of circle
circle_center = (290 + 20 + radius, 55)
# define the radius of the circle
#  Draw a circle using the circle() Function
cv2.circle(image, circle_center, radius, (0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)

# define the center point of ellipse
ellipse_center = (415, 190)
# define the major and minor axes of the ellipse
axis1 = (100, 50)
axis2 = (125, 50)
# draw the ellipse
# Horizontal
cv2.ellipse(image, ellipse_center, axis1, 0, 30, 330, (255, 0, 0), thickness=3)
# Vertical
cv2.ellipse(image, ellipse_center, axis2, 90, 0, 360, (0, 0, 255), thickness=3)

# let's write the text you want to put on the image
text = 'I am a Happy dog!'
# org: Where you want to put the text
org = (10, 200)
# write the text on the input image
cv2.putText(image, text, org, fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2, color=(250, 225, 100))

cv2.imshow('Image Line', image)
cv2.waitKey(0)
