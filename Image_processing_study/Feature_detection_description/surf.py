import cv2
import numpy as np


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread(r"D:\Code Base\Image_processing_study\images\chess.jpg",-1)
image.dtype

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create(50000)

kp, des = surf.detectAndCompute(gray)

img2 = cv2.drawKeypoints(image,kp)

