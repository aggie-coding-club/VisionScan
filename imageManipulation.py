#
# Project Name:         VisionScan
# Chapter:              1
# Program:              Opening an Image
# Date:                 11/05/2021
# Edited by:            Albert Ma
#

import cv2
import numpy as np

sampleImg = cv2.imread('Resources\lena.png')
kernel = np.ones((5,5), np.uint8)   # to be used for dilation

imgColorConvert = cv2.cvtColor(sampleImg,cv2.COLOR_BGR2GRAY)    # Color Conversion
imgBlur = cv2.GaussianBlur(sampleImg, (7,7), 0) # De-noising the Image by blurring it
imgCanny = cv2.Canny(sampleImg, 150, 200)   # Edge Detection
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)    # Increases thickness of edges from canny using iterations
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)    # Essentially the opposite of dilation

cv2.imshow("Gray Image", imgColorConvert)
cv2.imshow("Blurred Image", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dilation", imgDilation)
cv2.imshow("Image Erosion", imgEroded)
cv2.waitKey(0)