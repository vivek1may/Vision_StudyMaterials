import cv2
import numpy as np


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread(r"D:\Code Base\Image_processing_study\images\chess.jpg",-1)
image.dtype

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = np.float32(image)

dst = cv2.cornerHarris(gray,2,3,.04)
dst = cv2.dilate(dst,None)

image[dst >0.01*dst.max()] = [0,0,255]
showimg(image)

