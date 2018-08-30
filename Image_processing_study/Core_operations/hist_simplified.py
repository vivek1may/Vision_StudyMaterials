import numpy as np
import cv2
import matplotlib.pyplot as plt

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",0)
image.shape

#Histogram equalization
equ = cv2.equalizeHist(image)

res = np.hstack((image,equ ))
showimg(res)


#CLAHE Contrast Limited Adaptive Histogram Equalization

clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
c1 = clahe.apply(image)

clahe_res = np.hstack((image,c1))

showimg(clahe_res)


#hist for each channel
hist = cv2.calcHist([image],[0],None,[180,255],[0,140])