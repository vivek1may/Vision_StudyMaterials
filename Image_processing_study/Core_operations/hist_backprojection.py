import numpy as np
import cv2
import matplotlib.pyplot as plt

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape


#Convert the image into hsv for mapping
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#Set a target image
target = image[100:300,200:400]
thsv = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

roihist = cv2.calcHist(thsv,[0,1],None,[180,256],[0,180,0,256])

#normalize histogram
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)

#Find backprojection on base image
dist = cv2.calcBackProject([hsv],[0,1],roihist,[0,180,0,256],1)

#Convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(image,-1,disc,dist)

ret , thresh = cv2.threshold(dist,20,255,1)

result = cv2.bitwise_and(image,image,mask=thresh)
showimg(result)