# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:22:16 2021

@author: eagle
"""

import cv2 as cv
import numpy as np
try:
    img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//4.jpg")
    img=cv.resize(img,(800,800))
    cv.imshow("img",img)
    
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("gray image",gray)
    
    harcade=cv.CascadeClassifier("harcade.xml")
    faces_rect=harcade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)
    
    print(f'Number of faces found={len(faces_rect)}')
    
    for (x,y,w,h) in faces_rect:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
    cv.imshow("detected",img)
    
    
    cv.waitKey(0)
except Exception as e:
        print(e)