import numpy as np
import cv2

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)

image =cv2.imread("/../images/plant.jpg",-1)
image.shape

#Multistage algorithm
#Will go through each stage
# 1.Noise removal
# 2. Finding intensity gradient of images
# 3. Non-maximum supression
# 4. Hysteresis thresholding


edges = cv2.Canny(image,100,200)
showimg(edges)
