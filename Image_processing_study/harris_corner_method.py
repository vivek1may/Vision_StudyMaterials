import numpy as np
import cv2

def nothing():
    pass

image = cv2.imread("D:/Images/plant.jpg",-1)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray,(500,500))
gray  = np.float64(gray)

win1 = np.array([[1,2],[3,4]],dtype=np.float64)
win2 = np.array([[1,2],[3,4]],dtype=np.float64).T


ret, ev1,evc1 = cv2.eigen((win1))
ret, ev2,evc2 = cv2.eigen((win2))


ev1 * ev2