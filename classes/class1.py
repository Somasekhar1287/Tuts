# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:47:30 2021

@author: eagle
"""

class example():
   
    def disp():
        msg1="Hello "
        print(msg1)
    
     
example().disp()    





class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def student_print(self):
        print("Name is: ",self.name," Age is: ",self.age)
        
        
student("soma",33).student_print()
student=student("sanju","22")
student.student_print()

