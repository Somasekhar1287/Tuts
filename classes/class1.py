# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:47:30 2021

@author: eagle
"""

class example():
   
    def disp(msg):
        msg="Hello "+msg
        print(msg)
    def ret_disp(msg):
        return msg
        

class example1():
    m="hello"
    def disp(msg):
        msg=m+msg
        print(msg)
    def ret_disp():
        return msg




class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def student_print(self):
        print("Name is: ",self.name.title()," Age is: ",self.age)
        
        
student("soma",33).student_print()
student=student("sanju","22")
student.student_print()

