import numpy as np
import  cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
events
start = False
def scratch(event,x,y,flags,params):
    global start
    if event == cv2.EVENT_LBUTTONDOWN:
        start = True
    if event == cv2.EVENT_LBUTTONUP:
        start = False
    if start:
        cv2.circle(image, (x, y), 3, (0, 0, 255), -1)

image = np.zeros((500,500,3),np.uint8)
cv2.namedWindow("drawit")
cv2.setMouseCallback("drawit",scratch)

while True:
    cv2.imshow("drawit",image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()