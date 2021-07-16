# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 21:34:03 2021

@author: eagle
"""

import cv2 as cv
import numpy as np
try:
     img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//aladdin.jpg")
     cv.imshow("img",img)
     
     b,g,r=cv.split(img)
     
     cv.imshow("Red",r)
     cv.imshow("Green",g)
     cv.imshow("blue",b)
     
     print(img.shape)
     print(r.shape)
     print(g.shape)
     print(b.shape)
     
     merged=cv.merge([b,g,r])
     cv.imshow("Merged Image",merged)
     
     blank=np.zeros(img.shape[:2],dtype="uint8")
     
     blue=cv.merge([b,blank,blank])
     
     green=cv.merge([blank,g,blank])
     
     red=cv.merge([blank,blank,r])
     
     
     cv.imshow("RED",red)
     cv.imshow("Green",green)
     cv.imshow("Blue",blue)
     
     
     cv.waitKey(0)
except Exception as e:
        print(e)