import cv2
import numpy as np


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
cimg = image.copy()

gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edge_img = cv2.Canny(gray_img,127,255)

circles = cv2.HoughCircles(gray_img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=1,maxRadius=1)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()