# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:06:22 2021

@author: eagle
"""



import square
import area
from area import rect_area
li=[1,2,3,4,5,6,7]

for i in li:
    print(square.Square(i))
    

sq_area=area.square_area(5)
sq_area=area.square_area()
print("Square area is : ",sq_area)

print(rect_area(5,6))

print(area.greet())
