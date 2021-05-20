# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:02:47 2021

@author: eagle
"""

######## functions #########

def helloworld():
    print("Hello world")
    
helloworld()

def hello(greet="Hello"):
    print(greet)
    
hello()
hello("Hello Sanju ! ")
###############

def avg(first,*rest):
    return(first+sum(rest))/(1+len(rest))

avg(1,3,4,58,2,45)

##################  multiple return values

def mult_ret(a,b,c):
    a=a*2
    b=b*3
    c=c*4
    return a,b,c

values=mult_ret(1,2,3)
print(values)
print(values[0])
###########################

def multiple_args(*args,**kwargs):
    for arg in args:
        print(arg)
    print(kwargs)
    
multiple_args('item','class','id','span',width='width',height='height')
