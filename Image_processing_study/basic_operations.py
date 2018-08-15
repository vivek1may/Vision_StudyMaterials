import numpy as np
import cv2

def ishow(image):
    cv2.imshow("iwindow",image)
    cv2.waitKey(0)

image = cv2.imread("D:/Images/plant.jpg",-1)

image[20:50,50:60] = [0,0,0]


img_index = image[:,:,0] < 127

image[img_index] = [0,0,0]

ishow(image)