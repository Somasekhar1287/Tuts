# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:59:54 2021

@author: eagle
"""

import cv2 as cv
import numpy as np
try:
    img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//aladdin.jpg")
    cv.imshow("img",img)
    
    blank=np.zeros(img.shape[:2],dtype="uint8")
    mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
    cv.imshow("mask",mask)
    
    masked=cv.bitwise_and(img,img,mask=mask)
    cv.imshow("masked",masked)
    
    cv.waitKey(0)
except Exception as e:
        print(e)