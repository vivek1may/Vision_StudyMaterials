import numpy as np
import cv2


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)

image =cv2.imread("/../images/plant.jpg",-1)
image.shape

#convert image to gray
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#Thresholding
#binary
ret, bin_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
showimg(bin_img)

#binary inverse
ret, bininv_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
showimg(bininv_img)

#OTSU
ret, otsu_img = cv2.threshold(gray,127,255,cv2.THRESH_OTSU)
showimg(otsu_img)

#Trunc
ret, trunc_img = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
showimg(trunc_img)

#tozero
ret, tozero_img = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
showimg(tozero_img)

#Visual similarities of these these can be found
#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

#Adaptive threshold

adptive = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
showimg(adptive)