# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:56:52 2021

@author: eagle
"""

def rect_area(l=1,b=1):
    if l==0 and b==0:
        return 0
    elif l==0 or b==0:
        return 0
    else:
        return l*b

def square_area(a=1):
    if a==0:
        return 0
    else:
        return a*a
    
