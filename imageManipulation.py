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
# kernel = np.ones()

imgColorConvert = cv2.cvtColor(sampleImg,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(sampleImg, (7,7), 0)
imgCanny = cv2.Canny(sampleImg, 150, 200)

cv2.imshow("Gray Image", imgColorConvert)
cv2.imshow("Blurred Image", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.waitKey(0)