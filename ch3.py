# task 3: Resizing images
import cv2

def display(img, title="Image"):
    cv2.imshow(title, img)
    cv2.waitKey(1000)

img = cv2.imread("resources/linktocat.jpg")
print(img.shape) # height x width x channels 

display(img)

# just for kicks
resized = cv2.resize(img, (1920, 1080))
display(resized)

resized = cv2.resize(img, (400, 400))
display(resized)

# cropping; remeber that opencv defines positive y from north to south
cropped = resized[0:200, 100:300] # height range then width range
display(cropped)