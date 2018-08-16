import cv2
import numpy as np
from matplotlib import pyplot as plt

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)

img = cv2.imread("images/o.jpg",-1)
img.shape

image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



#Erosion

eroded = cv2.erode(image,(3,3))
showimg(eroded)

#Dilute
dilated = cv2.dilate(image,(7,7),iterations=5)
showimg(dilated)

#Opening
#Erosion followed by dilation

opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,(5,5))
showimg(opening)

#closing
#Dilation followed by erosion
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,(7,7))
showimg(closing)


#Gradiance
#Difference between the dilation and erosion
grad = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,(7,7))
showimg(grad)


#Structing element

cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))