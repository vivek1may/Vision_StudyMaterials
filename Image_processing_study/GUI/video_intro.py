import cv2
import numpy as np
import matplotlib.pyplot as plt


def play_cam_video():
    camera = cv2.VideoCapture(0)

    if camera.isOpened():
        while True:
            ret, frame = camera.read()
            if ret:
                cv2.imshow("video_stream",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


    camera.release()
    cv2.destroyAllWindows()

def play_file_video():
    camera = cv2.VideoCapture("/../images/video.mp4")

    if camera.isOpened():
        while True:
            ret, frame = camera.read()
            if ret:
                cv2.imshow("video_stream",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


    camera.release()
    cv2.destroyAllWindows()


import numpy as np
import cv2
def write_video_cam():
    camera = cv2.VideoCapture(0)
    writer = cv2.VideoWriter("out.avi",cv2.VideoWriter_fourcc(*'XVID'),20.0,(int(camera.get(3)),int(camera.get(4))))
    if camera.isOpened():
        while True:
            ret, frame = camera.read()
            if ret:
                cv2.imshow("video_stream",frame)
                writer.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    camera.release()
    writer.release()
    cv2.destroyAllWindows()