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

#Moment
moment = cv2.moments(cnt)
print(moment)

#Contour area
area = cv2.contourArea(cnt)


#perimeter
perimeter = cv2.arcLength(cnt,True)

#contour approximation
epsilon = .1 * cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

#convex hull
hull = cv2.convexHull(cnt)


#Checking convexity
k = cv2.isContourConvex(cnt)
k

#Bounding rectangle
#Straight
x,y,w,h = cv2.boundingRect(cnt)

#Rotated
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)


#min enclosing circle
(x,y), radius = cv2.minEnclosingCircle(cnt)



#Fitting an ellipse
ellipse = cv2.fitEllipse(cnt)


