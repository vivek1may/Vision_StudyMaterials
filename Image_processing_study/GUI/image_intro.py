import cv2
import numpy as np
import matplotlib.pyplot as plt

image =cv2.imread("/../images/plant.jpg",-1)
image.shape

#change part of the image

image[10:100,20:200] = [0,0,255]

cv2.imshow("iwindow",image)
cv2.waitKey(0)

plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()