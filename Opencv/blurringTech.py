# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 22:21:16 2021

@author: eagle
"""

import cv2 as cv 
import numpy as np
try:
     img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//aladdin.jpg")
     cv.imshow("img",img)
     
     ### averaging
     avg=cv.blur(img,(3,3))
     
     avg1=cv.blur(img,(7,7))
     
     
     cv.imshow("avg",avg1)
     
     
     ### gaussian blur
     
     guass=cv.GaussianBlur(img,(7,7),0)
     cv.imshow("gauss",guass)
     
     
     ### median blur
     
     med=cv.medianBlur(img,9)
     cv.imshow("med",med)
     
     #### bilateral
     bilateral=cv.bilateralFilter(img, 15, 35, 35)
     cv.imshow("bila",bilateral)
     
     cv.waitKey(0)
except Exception as e:
        print(e)