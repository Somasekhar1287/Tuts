# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:29:52 2021

@author: eagle
"""

####### printing only odd numbers
cur_num=0
while cur_num<=10:
    cur_num+=1
    if cur_num % 2==0:
        continue
    print(cur_num)
    

####### printing only even numbers
cur_num=0
while cur_num<=10:
    cur_num+=1
    if cur_num % 2==0:
        print(cur_num)
    else:
        continue
   
    
####### avoiding infinte loops
x=1
while x<=5:
    print(x)
    x+=1