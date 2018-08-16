import numpy as np
import cv2


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape
image2 = cv2.imread("D:/Code Base/Image_processing_study/images/fall.jpg",-1)
image2.shape

#Change to HSV

img_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
showimg(img_hsv)

img_hsl = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
showimg(img_hsl)

#Convert value to hsv
green = np.array([0,255,0],np.uint8)
green = green.reshape((-1,1,3))
green_hsv = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

green_hsv