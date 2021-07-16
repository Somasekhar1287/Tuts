# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 21:56:05 2021

@author: eagle
"""

import cv2 as cv
import numpy as np
try:
    img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//aladdin.jpg")
    cv.imshow("img",img)
    
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    
    lap=cv.Laplacian(gray,cv.CV_64F)
    lap=np.uint8(np.absolute(lap))
    
       
    cv.imshow("lap",lap)
    
    ### sobel
    
    sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
    sobely=cv.Sobel(gray,cv.CV_64F,0,1)
    
    cv.imshow("sobel x ",sobelx)
    cv.imshow("sobel y",sobely)
    
    sobel_tot=cv.bitwise_or(sobelx,sobely)
    cv.imshow("combined sobel",sobel_tot)
    
    cv.waitKey(0)
except Exception as e:
        print(e)