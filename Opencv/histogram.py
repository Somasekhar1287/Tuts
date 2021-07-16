# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 21:54:54 2021

@author: eagle
"""

import cv2 as cv
import numpy as np
try:
    img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//aladdin.jpg")
    cv.imshow("img",img)
    cv.waitKey(0)
except Exception as e:
        print(e)