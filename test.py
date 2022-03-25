import cv2

print(cv2.__version__)
path = 'Resources/2022-BMW-M240i-profile.jpg'
img = cv2.imread(path)
cv2.imshow('Test',img)
cv2.waitKey(0)