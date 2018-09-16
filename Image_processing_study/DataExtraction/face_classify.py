import numpy as np
import cv2
import  os
import shutil
dest_foler = "D:/DataSets/faces/"
scale = (100,100)
nivin =cv2.imread("D:/DataSets/faces/6.jpg",0)
naz = cv2.imread("D:/DataSets/faces/5.jpg",0)

nivin = cv2.resize(nivin,scale)
naz = cv2.resize(naz,scale)
nivin_rm = np.mean(nivin,axis=0)
nivin_cm = np.mean(nivin,axis=1)

naz_rm = np.mean(naz,axis=0)
naz_cm = np.mean(naz,axis=1)

for file in os.listdir(dest_foler):
    imfile = cv2.imread(dest_foler+file,0)
    imfile = cv2.resize(imfile,scale)
    im_rm = np.mean(imfile,axis=0)
    im_cm = np.mean(imfile, axis=1)

    nivin_diff = np.linalg.norm(nivin_rm-im_rm) + np.linalg.norm(nivin_cm-im_cm)
    naz_diff = np.linalg.norm(naz_rm - im_rm) + np.linalg.norm(naz_cm - im_cm)

    if(nivin_diff < naz_diff):
        #belong to nivin
        shutil.copy(dest_foler+file,dest_foler+"nivin/"+file)
    else:
        shutil.copy(dest_foler+file,dest_foler+"naz/"+file)





