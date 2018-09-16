import cv2
import numpy as np


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread(r"D:\Code Base\Image_processing_study\images\chess.jpg",-1)
image.dtype

#Sift algorithm
#1 . Scale space Extrema
#scale-space filtering is used. In it, Laplacian of Gaussian is found for the image with various \sigma values.
# SIFT algorithm uses Difference of Gaussians which is an approximation of LoG. Difference of Gaussian is obtained as the difference of Gaussian blurring of an image with two different \sigma,
# let it be \sigma and k\sigma. This process is done for different octaves of the image in Gaussian Pyramid.

#2. Key point localization
#Refined to get more accurate result.
#ntensity at this extrema is less than a threshold value (0.03 as per the paper), it is rejected. This threshold is called contrastThreshold in OpenCV
#Remove edges (Hessian matrix) edgeThreshold  = 10 as given in paper

#3. Orientation Assignment
#Creates keypoint with same location and scale with different orientation. It contributes to stability of matching.

#4. keypoint descriptor
#Now keypoint descriptor is created. A 16x16 neighbourhood around the keypoint is taken.
# It is devided into 16 sub-blocks of 4x4 size. For each sub-block, 8 bin orientation histogram is created.
# So a total of 128 bin values are available. It is represented as a vector to form keypoint descriptor.
# In addition to this, several measures are taken to achieve robustness against illumination changes, rotation etc

#5 . Keypoint matching
#if 2 matches found, ration of those will decide the correct one.

#build opencv with non-free flag
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)