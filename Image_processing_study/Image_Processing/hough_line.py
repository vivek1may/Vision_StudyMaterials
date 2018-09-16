import cv2
import numpy as np


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)

showimg(image)

gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edge_img = cv2.Canny(gray_img,127,255)

#pixel wise cofigurations
minlinelen = 20
maxlinegatp = 3

#Hough line Probability mode
lines = cv2.HoughLinesP(edge_img,1,np.pi/180,100,None,minlinelen,maxlinegatp)

for x1,y1,x2,y2 in lines[0]:
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)

showimg(image)    