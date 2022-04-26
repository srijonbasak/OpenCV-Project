import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512,512,3),np.int8) #blank img

#FUNCTION
def draw_circle(event,x,y,flags,pram):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(255,255,255),-1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)


#window for img
while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitkey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()