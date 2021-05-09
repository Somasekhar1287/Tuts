# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:54:37 2021

@author: eagle
"""

import cv2 as cv
import numpy as np
port=0
def rescaleFrame(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

try:
    #img=cv.imread('C://Users//eagle//OneDrive//Pictures//Saved Pictures//Nature//17597.jpg')
    #r_img=rescaleFrame(img)
    #cv.imshow('nature',r_img)
    cap=cv.VideoCapture(port)
    while (True):
        ret,frame=cap.read()
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        r_gray=rescaleFrame(gray)
        cv.imshow('frame',r_gray)
        if cv.waitKey(0) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()
except Exception as e:
    print(e)