#
# Project Name:         VisionScan
# Chapter:              1
# Program:              Opening an Image
# Date:                 11/05/2021
# Edited by:            Albert Ma
#
import cv2
print("Package Imported")

image = cv2.imread('Resources/lena.png')    # Functions in nearly the same way as open()

cv2.imshow("Image", image)    # Displays file using identifier
cv2.waitKey(0)  # The amount of time in milliseconds the image displays, 0 meaning infinite