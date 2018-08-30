import numpy as np
import cv2
import matplotlib.pyplot as plt

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#To improve the contrast of the image

hist, bins = np.histogram(image.flatten(),256,[0,256])
cdf = hist.cumsum()

cdf_normalized = cdf * hist.max()/cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(image.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')


img2 = cdf[image]
