# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:00:32 2021

@author: eagle
"""

import cv2 as cv

try:
    def rescale(frame,scale=0.75):
       width=int(frame.shape[1]*scale)
       height=int(frame.shape[0]*scale)
       dims=(width,height)
       return cv.resize(frame,dims,interpolation=cv.INTER_AREA)
        
        
    capture=cv.VideoCapture("C:/Users/eagle/Videos/vtest.avi")
    while True:
        isTrue,frame=capture.read()
        resize_frame=rescale(frame,0.25)
        cv.imshow("Resize Video",resize_frame)
        cv.imshow("Video",frame)
        if cv.waitKey(25) & 0xFF==ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()
except Exception as e:
    print(e)