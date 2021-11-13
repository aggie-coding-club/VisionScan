#
# Project Name:         VisionScan
# Chapter:              1
# Program:              Opening and Displaying Video
# Date:                 11/05/2021
# Edited by:            Albert Ma
#

import cv2

vidfeed = cv2.VideoCapture(0)
vidfeed.set(3,640)  # Horizontal Resolution (ID 3)
vidfeed.set(4,480)  # Vertical Resolution (ID 4)


while True:
    success, img = vidfeed.read() # success is a boolean, img is a separate variable for displaying the video
    cv2.imshow("Video", img)
    if cv2.waitKey(1) and 0xFF == ord('q'): # if q is pressed, waitKey is True, video feed stops
        break