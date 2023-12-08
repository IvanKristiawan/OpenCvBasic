import cv2
import numpy as np

# Image Index
img = cv2.imread("Resources/lena.png")
print(img.shape)

# Resize Image
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

# Crop Image
imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)

# Black Image
img = np.zeros((512,512))
print(img.shape)

# Color Image
img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:] = 255,0,0

# Create Line
# cv2.line(img, (0,0), (300,300), (0,255,0), 3)
# cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)

# Create Rectangle
# cv2.rectangle(img, (0,0), (250,350), (0,0,255), 2)
# cv2.rectangle(img, (0,0), (250,350), (0,0,255), cv2.FILLED)

# Create Circle
# cv2.circle(img, (400,50), 30, (255,255,0), 5)

# Create Text
cv2.putText(img, " OPENCV ", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
