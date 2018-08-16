import numpy as np
import cv2

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

#change pixel value of 1 channel
image[10:100,20:200,1] = [255]

showimg(image)

#access pixel values through better method
#get item
image.item(10,10,1)

#set item
image.itemset((10,10,1),255)

#image properties
image.shape
image.dtype
image.size



#splitting and merging channels

b,g,r = cv2.split(image)

#merge by exchanging channels

image_ex = cv2.merge((r,g,b))

showimg(image_ex)

#Making border of an image

img1 = cv2.copyMakeBorder(image_ex,10,30,200,300,cv2.BORDER_REFLECT)
showimg(img1)