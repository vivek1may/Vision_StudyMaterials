import cv2
import numpy as np
from matplotlib import pyplot as plt

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)

img = cv2.imread("/../images/plant.jpg",-1)

kernel = np.ones((5,5),np.float32)/25.0
f_img = cv2.filter2D(img,-1,kernel=kernel)
showimg(f_img)

#gaussian filter
g_img = cv2.GaussianBlur(img,(5,5),0)
showimg(g_img)

#Median blur
#highly effective in removing salt and pepper noise

m_img = cv2.medianBlur(img,5)
showimg(m_img)

#The bilateral filter also uses a Gaussian filter in the space domain, but it also uses one more (multiplicative)
#  Gaussian filter component which is a function of pixel intensity differences. The Gaussian function of space
#  makes sure that only pixels are ‘spatial neighbors’ are considered for filtering, while the Gaussian component
# applied in the intensity domain (a Gaussian function of intensity differences) ensures that only those pixels with
#  intensities similar to that of the central pixel (‘intensity neighbors’) are included to compute the blurred
# intensity value. As a result, this method preserves edges, since for pixels lying near edges, neighboring pixels
#  placed on the other side of the edge, and therefore exhibiting large intensity variations when compared to the
# central pixel, will not be included for blurring.

b_img = cv2.bilateralFilter(img,9,75,95)

showimg(b_img)