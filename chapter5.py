import cv2
import numpy as np

img = cv2.imread('Resources/cards.jpeg')
img = cv2.resize(img,(int(img.shape[1]*.25),int(img.shape[0]*.25)))

width,height = 250,350

pts1 = np.float32([[886,280],[1138,246],[921,615],[1217,591]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow('Output',imgOutput)

cv2.waitKey(10000)  