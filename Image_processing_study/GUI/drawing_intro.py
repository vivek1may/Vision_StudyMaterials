import numpy as np
import cv2

def showimg(image):
    cv2.imshow("iwin", image)
    cv2.waitKey(0)

image =cv2.imread("/../images/plant.jpg",-1)

#make line
image_line =cv2.line(image,(0,20),(10,300),(0,0,255),3)

#rectangle
image_rect = cv2.rectangle(image,(10,10),(300,300),(0,0,255))
showimg(image_rect)

#Draw circle
image_circle = cv2.circle(image,(400,400),30,(255,0,0))
showimg(image_circle)
#ellipse
image_ellipse = cv2.ellipse(image,(100,100),(50,50),30,0,270,(0,0,255))
showimg(image_ellipse)

#Drawing polygon
pts = np.array([[100,50],[200,300],[70,200],[50,100]], np.int32)
pts
pts =pts.reshape((-1,1,2))

image_poly = cv2.polylines(image,[pts],False,(0,0,255))
showimg(image_poly)