import numpy as np
import cv2
import time
import math

Image = cv2.VideoCapture(0,cv2.CAP_DSHOW)


while True:

    ret, frame = Image.read()
    cv2.namedWindow("Smile", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Smile",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Smile',frame)
    Key = cv2.waitKey(125)
    Counter = 39
    if Key == ord(' '):
        while Counter>=0:
            ret, frame = Image.read()
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(frame,str(math.floor(Counter//10)),(550,450), font, 7,(255,255,255),5,cv2.LINE_AA)
            cv2.imshow('Smile',frame)
            cv2.waitKey(125)
            Counter = Counter-1
        else:
            cv2.imshow('Smile',frame)
            cv2.waitKey(1000)
            ret, frame = Image.read()
            cv2.imwrite('output.jpg',frame)
            break
cv2.destroyAllWindows()
