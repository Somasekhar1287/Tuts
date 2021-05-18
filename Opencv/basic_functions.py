# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:03:07 2021

@author: eagle
"""

import cv2 as cv

try:
    img=cv.imread("C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//images//adorable-cat.jpg")
    cv.imshow("cat",img)
    
    class effects():
       
        def grayscale():
            ### gray scale
            gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            cv.imshow("grayscale",gray)
    
        def blur():
            #### blur
            blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
            cv.imshow("blur",blur)
            return blur()
        
        def canny():
            #### edge cascade
            blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
            edge=cv.Canny(blur,125,175)
            cv.imshow("canny",edge)
      
        def dilate():
            ####dilated
            blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
            edge=cv.Canny(blur,125,175)
            dilated=cv.dilate(edge,(7,7),iterations=3)
            cv.imshow("dilate",dilated)
    
        def erode():
            ### erode
            blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
            edge=cv.Canny(blur,125,175)
            dilated=cv.dilate(edge,(7,7),iterations=3)
            erode=cv.erode(dilated,(3,3),iterations=1)
            cv.imshow("erode",erode)
    
        def resize():
            #### resize 
            resize=cv.resize(img,(500,500))
            cv.imshow("resize",resize)
        def crop():
            ### cropping
            crop=img[20:200,200:400]
            cv.imshow("crop",crop)
    
    effects.grayscale()
    effects.crop()
    cv.waitKey(0)
    
except Exception as e:
    print(e)