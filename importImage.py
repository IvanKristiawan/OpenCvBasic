import cv2
import numpy as np

# Import Image
img = cv2.imread("Resources/lena.png")

cv2.imshow("Output", img)
cv2.waitKey(0)
