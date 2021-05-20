# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:19:47 2021

@author: eagle
"""

import cv2 as cv
try:
    def rescale(frame,scale=0.75):
       width=int(frame.shape[1]*scale)
       height=int(frame.shape[0]*scale)
       dims=(width,height)
       return cv.resize(frame,dims,interpolation=cv.INTER_AREA)
    
    img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//adorable-cat.jpg")
    
    r_img=rescale(img)
    cv.imshow("img",r_img)
    cv.waitKey(0)
    
   
    
except Exception as e:
    print(e)
