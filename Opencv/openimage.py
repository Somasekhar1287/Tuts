# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:21:15 2021

@author: eagle
"""

import cv2 as cv
try:
    img=cv.imread("C://Users//eagle//OneDrive//Documents//python//Opencv//images//adorable-cat.jpg")
    cv.imshow("img",img)
    cv.waitKey(0)
except Exception as e:
    print(e)