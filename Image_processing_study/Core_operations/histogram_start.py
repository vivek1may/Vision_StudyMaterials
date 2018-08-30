import numpy as np
import cv2
import matplotlib.pyplot as plt
def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

hist = cv2.calcHist([image],[0],None,[16],[0,255])

plt.plot(hist)