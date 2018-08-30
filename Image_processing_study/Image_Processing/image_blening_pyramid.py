import numpy as np
import cv2


def showimg(image):
    cv2.imshow("iwin",image)
    cv2.waitKey(0)
image =cv2.imread("/../images/plant.jpg",-1)
image.shape

image2 = cv2.imread("D:/Code Base/Image_processing_study/images/fall.jpg",-1)
image2.shape

image =cv2.resize(image,tuple(reversed(image2.shape[:2])))


#Generate gaussian pyramid for image
G = image.copy()
gpA =[G]
for i in range(5):
    G = cv2.pyrDown(G)
    gpA.append(G)

#Generate gaussian pyramid for image1
G = image2.copy()
gpB =[G]
for i in range(5):
    G = cv2.pyrDown(G)
    gpB.append(G)


#Generate Laplacian pyramid
lpA= [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    GE =cv2.resize(GE,tuple(reversed(gpA[i-1].shape[:2])))
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    GE =cv2.resize(GE,tuple(reversed(gpB[i-1].shape[:2])))
    L = cv2.subtract(gpA[i-1],GE)
    lpB.append(L)

test = np.hstack((image,image2,image))
test = np.vstack((test,test))
showimg(test)

#add left and right part of the image in eachlevel

LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))
    LS.append(ls)

#Now reconstruct
ls_ = LS[0]

for i in range(1,6):
    ls_ =  cv2.pyrUp(ls_)
    ls_ = cv2.resize(ls_,tuple(reversed(LS[i].shape[:2])))
    ls_ = cv2.add(ls_,LS[i])

#Result of blened imgage
showimg(ls_)