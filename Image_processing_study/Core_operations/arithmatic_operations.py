import numpy as np
import cv2


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape
image2 = cv2.imread("D:/Code Base/Image_processing_study/images/fall.jpg",-1)
image2.shape


#Image addition
#openCV addition in saturated
i2 = cv2.add(image,30)
showimg(i2)

#Numpy addition is modular operation
i2 = image + 200

##Image blending
image2 = cv2.resize(image2,(image.shape[1],image.shape[0]))
w_image =cv2.addWeighted(image,.8,image2,.2,0)

showimg(w_image)

##Bitwise operation
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

img = cv2.bitwise_and(image,image,mask=thresh)

showimg(img)