# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:00:32 2021

@author: eagle
"""

import cv2 as cv

try:
    capture=cv.VideoCapture("C:/Users/eagle/Videos/codbops2.mp4")
    while True:
        isTrue,frame=capture.read()
        cv.imshow("Video",frame)
        if cv.waitKey(25) & 0xFF==ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()
except Exception as e:
    print(e)