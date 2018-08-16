import numpy as np
import cv2


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

#Sobel
#Gaussian smoothing + differentiation operations

sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
showimg(sobelx)
sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
showimg(sobely)

sobel_8u = cv2.Sobel(image,cv2.CV_8U,1,0,ksize=5)
showimg(sobel_8u)
#laplacian
#Derivation is happening on both the directions

laplacian = cv2.Laplacian(image,cv2.CV_64F)
showimg(laplacian)

