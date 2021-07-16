# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:34:54 2021

@author: eagle
"""

import cv2 as cv 
import numpy as np
try:
    #img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//aladdin.jpg")
    #cv.imshow("img",img)
    blank=np.zeros((400,400),dtype="uint8")
    
    rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
    circle=cv.circle(blank.copy(),(200,200),200,255,-1)
    
    cv.imshow("rect",rectangle)
    cv.imshow("circle",circle)
    
    bitwise_and=cv.bitwise_and(rectangle,circle)
    cv.imshow("bitwise and",bitwise_and)
    
    bitwise_or=cv.bitwise_or(rectangle,circle)
    cv.imshow("bitwise or",bitwise_or)
    
    bit_xor=cv.bitwise_xor(rectangle,circle)
    cv.imshow("bit wise xor",bit_xor)
    
    bit_not=cv.bitwise_not(rectangle)
    cv.imshow("rect not",bit_not)
    
    cv.waitKey(0)
except Exception as e:
        print(e)