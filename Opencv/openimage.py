# -*- coding: utf-8 -*-
"""
Created on Sun May  9 22:21:15 2021

@author: eagle
"""

import cv2 as cv

def open_image(image):
    try:
        img=cv.imread(image)
        return img
    except Exception as e:
        print(e)