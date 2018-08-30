import numpy as np
import cv2

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

edge = cv2.Canny(image,20,100)

ret, contours , hier = cv2.findContours(edge,cv2.CHAIN_APPROX_SIMPLE,cv2.RETR_TREE)

cnt = contours[10]
cv2.matchShapes(contours[1],contours[10],1,0)

#Convexity defect
hull = cv2.convexHull(cnt,returnPoints = False)
cv2.convexityDefects(cnt,hull)