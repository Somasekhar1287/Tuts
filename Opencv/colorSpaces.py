# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 23:14:50 2021

@author: eagle
"""

import cv2 as cv
import matplotlib.pyplot as plt
try:
     img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//aladdin.jpg")
     cv.imshow("img",img)
     
     #### BGR to grayscale
     gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
     cv.imshow("gray",gray)
     
     ### BGR to HSV
     hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
     #cv.imshow("Hsv",hsv)
     
     ### BGR to l a b
     lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
     #cv.imshow("LAB",lab)
     
     #### BGR to RGB 
     rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
     #cv.imshow("RGB",rgb)
     
     
     ### hsv - bgr
     hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
     #cv.imshow("hsv - bgr",hsv_bgr)
     
     #### gray to BGR
     gray_BGR=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
     cv.imshow("gray2bgr",gray_BGR)
     
     ### plot in pyplot
     #plt.imshow(rgb)
     #plt.show()
     
     cv.waitKey(0)
except Exception as e:
        print(e)