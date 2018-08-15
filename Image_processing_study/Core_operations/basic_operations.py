import numpy as np
import cv2

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

#change pixel value of 1 channel
image[10:100,20:200,1] = [255]

showimg(image)

#access pixel values through better method

image.get