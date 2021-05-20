# -*- coding: utf-8 -*-
"""
Created on Thu May 20 19:12:46 2021

@author: eagle
"""

import cv2 as cv
import numpy as np

try:
    img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//aladdin.jpg")
    cv.imshow("img",img)
    
    def translate(img,x,y):
        transMat=np.float32([[1,0,x],[0,1,y]])
        dimensions=(img.shape[1],img.shape[0])
        return cv.warpAffine(img,transMat,dimensions)
    
    ## -x ---> left
    ## -y ---> up
    ## x ---> right
    ## y ---> down
    
    translated=translate(img,100,100)
    cv.imshow("translated",translated)
    
    cv.waitKey(0)
    
except Exception as e:
    print(e)