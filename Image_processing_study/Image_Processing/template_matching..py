import numpy as np
import cv2

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

template = image[200:300,100:200]

result = cv2.matchTemplate(image,template,cv2.TM_SQDIFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = min_loc
w,h = template.shape[:2]
bottom_right = (top_left[0]+w, top_left[1]+h)

r_image = cv2.rectangle(image,top_left,bottom_right,(255,255,0),3)

showimg(r_image)