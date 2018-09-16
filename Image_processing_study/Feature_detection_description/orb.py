import cv2
import numpy as np


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread(r"D:\Code Base\Image_processing_study\images\chess.jpg",-1)
image.dtype

img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,image,color=(0,255,0), flags=0)
showimg(img2)