# task 2: # Displaying and manipulating an image with image processing

import cv2
import numpy as np

img = cv2.imread("resources/linktocat.jpg")
kernel = np.ones((5,5), np.uint8)

mods = []
mods.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)) # greyscale
mods.append(cv2.GaussianBlur(img, (15,15), 0)) # blurring
mods.append(cv2.Canny(img, 100, 100)) # edge detector
mods.append(cv2.dilate(mods[-1], kernel, iterations=1)) # dilation (increases thickness of edges)
mods.append(cv2.erode(mods[-1], kernel,iterations=1)) # erosion is the opposite of dilation; it makes the lines thinner

for mod in mods:
    cv2.imshow("Modded Image", mod)
    cv2.waitKey(1000)