# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:02:47 2021

@author: eagle
"""

######## functions #########

def helloworld():
    print("Hello world")
    
helloworld()


###############

def avg(first,*rest):
    return(first+sum(rest))/(1+len(rest))

avg(1,3,4,58,2,45)


###########################

def multiple_args(*args,**kwargs):
    print(args)
    for arg in args:
        print(arg)
    print(kwargs)
    
multiple_args('item','class','id','span',width='width',height='height')
