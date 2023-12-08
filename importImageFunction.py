import cv2
import numpy as np

# Import Image Function
img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

# GrayScale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
# Edge Detector
imgCanny = cv2.Canny(img, 150, 200)
# Dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# Eroded
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
