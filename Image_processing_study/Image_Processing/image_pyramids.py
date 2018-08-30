import numpy as np
import cv2

def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)

image =cv2.imread("/../images/plant.jpg",-1)
image.shape

#Explation
# Set of images with different resolution is called image pyramids

# 1. Gaussian Pyramid
# 2. Laplacian Pyramid

# Area reduced to one fourth of original image is called octave


lower_resolution = cv2.pyrDown(image)
image.shape
lower_resolution.shape

high_reso = cv2.pyrUp(lower_resolution)
high_reso.shape


# Laplacian Pyramids are formed from the Gaussian Pyramids. There is no exclusive function for that.
# Laplacian pyramid images are like edge images only. Most of its elements are zeros. They are used in image compression. A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid.
# The three levels of a Laplacian level will look like below (contrast is adjusted to enhance the contents):

