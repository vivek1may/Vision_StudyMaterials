import cv2
import numpy as np
import matplotlib.pyplot as plt

dest_foler = "D:/DataSets/faces/"

face_cascade = cv2.CascadeClassifier('C:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(r"D:\Code Base\Image_processing_study\images\video.mp4")
counter =0
frame_counter =0
if camera.isOpened():
    while True:
        ret, frame = camera.read()
        if ret:
            if frame_counter >=30:
                frame_counter =0
                cv2.imshow("video_stream",frame)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.imwrite(dest_foler+str(counter)+".jpg",frame[y:y+h,x:x+w])
                    cv2.imshow("face",frame[y:y+h,x:x+w])
                    counter+=1

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                frame_counter +=1

camera.release()
cv2.destroyAllWindows()









