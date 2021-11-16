
import cv2

# Task 1: Display .mp4 video
# Instead of using a stock video, I'm just going to do live playback from the webcam
# If you want to change to a pre-recorded video, just change pass a file location to 
# cv2.VideoCapture instead of 0 and get rid of the configuration lines after it.

cap = cv2.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height
cap.set(10, 5) # brightness

while True:
    success, img = cap.read()
    cv2.imshow("My video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)