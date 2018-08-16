import numpy as np
import cv2

image =cv2.imread("/../images/plant.jpg",-1)
image.shape

#getTickCount() returns number of clock count
#getTickFrequency() return number of clock-cycles per second.

start_time = cv2.getTickCount()
for i in range(1,50,2):
    cv2.medianBlur(image,i)

print((cv2.getTickCount()-start_time)/cv2.getTickFrequency())


#set opencv as optimized mode
cv2.setUseOptimized(True)
cv2.useOptimized()
