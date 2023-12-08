import cv2
import numpy as np

# Webcam
cap = cv2.VideoCapture(0)
# Define Width
cap.set(3, 640)
# Define Height
cap.set(4, 480)
# Change Brightness
# cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
