import cv2
import numpy as np


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread(r"D:\Code Base\Image_processing_study\images\chess.jpg",-1)
image.dtype

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#gray = np.float32(image)

corners = cv2.goodFeaturesToTrack(gray,60,.01,20)
type(corners)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(image,(x,y),(5),(0,0,255))

showimg(image)

