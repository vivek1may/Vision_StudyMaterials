# For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
# findContours function modifies the source image. So if you want source image even after finding contours, already store it to some other variables.
# In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

import numpy as np
import cv2

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

img, contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

showimg(thresh)

img_contour = cv2.drawContours(img, contour, -1, (0,255,0), 3)
showimg(img_contour)