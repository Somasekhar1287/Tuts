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
    
    def rotation(img,angle,rotPoint=None):
        (height,width)=img.shape[:2]
        
        if rotPoint is None:
            rotPoint=(width//2,height//2)
            
        rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
        dimensions=(width,height)
        
        return cv.warpAffine(img,rotMat,dimensions)
    
    rotated=rotation(img,45)
    cv.imshow("rotation",rotated)
    
    rotated1=rotation(img,-45)
    cv.imshow("rotation reverse",rotated1)
    
    ### rotating the rotated image
    rot2=rotation(rotated,45)
    cv.imshow("double rot",rot2)
    
    
    # resize 
    resized_sink=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
    resized_linear=cv.resize(img,(1280,1024 ),interpolation=cv.INTER_LINEAR)
    resized_cubic=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
    
    #cv.imshow("sink",resized_sink)
    #cv.imshow("linear",resized_linear)
    cv.imshow("cubic",resized_cubic)
    
    
    ### flip vertical
    flip=cv.flip(img,0)
    cv.imshow("flip",flip)
    
    ### flip horizontally
    flip2=cv.flip(img,1)
    cv.imshow("flip2",flip2)
    
    ## flip both
    flip3=cv.flip(img,-1)
    cv.imshow("flip3",flip3)
    
    cv.waitKey(0)
    
except Exception as e:
    print(e)