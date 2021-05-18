# -*- coding: utf-8 -*-
"""
Created on Tue May 18 00:02:28 2021

@author: eagle
"""

import cv2 as cv
import numpy as np

try:
    blank=np.zeros((500,500,3),dtype="uint8")
    
    def rescale(frame,scale=0.50):
       width=int(frame.shape[1]*scale)
       height=int(frame.shape[0]*scale)
       dims=(width,height)
       return cv.resize(frame,dims,interpolation=cv.INTER_AREA)
    
    
    cv.imshow("blank",blank)
    
    ####### fill with color
    #blank[:]=0,255,0
    #cv.imshow("green",blank)
    
    #### fill desired portion with color
    
    #blank[200:300, 300:400]=0,0,255
    #cv.imshow("some portion",blank)
    
    
    ############################# Rectangle #################################
    
    #### draw a rectangle with thickness 2
    #cv.rectangle(blank,(0,0),(200,200),(0,255,0),thickness=2)
    
    ##### draw a rectangle with filled color
    #cv.rectangle(blank,(0,0),(200,200),(0,255,0),thickness=cv.FILLED)
    
    ###### draw rectangle with width and height specified as multiples
    #cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=4)
    #cv.imshow("rectangle",blank)
    
    #############################  Circle #####################################
    
    
    #cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=5)
    cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
    cv.imshow("circle",blank)
    
    
    ############################# line ############################################
    
    cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
    cv.imshow("line",blank)
    
    ############################ Text ##########################################
    cv.putText(blank,"Hello",(200,250),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,255),2)
    cv.imshow("text",blank)
    
    #img =cv.imread("C://Users//eagle/OneDrive/Pictures/Saved Pictures/Nature/969650.jpg")
    #r_img=rescale(img)
    #cv.imshow("img",r_img)
    cv.waitKey(0)
    
except Exception as e:
    print(e)
