import cv2
import numpy as np


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread(r"D:\Code Base\Image_processing_study\images\chess.jpg",-1)
image.dtype

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()

#Find key points
kp = fast.detect(image,None)

#Draw key points
img = cv2.drawKeypoints(image,kp,image)
showimg(img)

# #Default parameter of Fast
# print("Threshold: ", fast.getInt('threshold'))
# print("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
# print("neighborhood: ", fast.getInt('type'))
# print("Total Keypoints with nonmaxSuppression: ", len(kp))