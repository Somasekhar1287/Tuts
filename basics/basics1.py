# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:19:39 2021

@author: eagle
"""

#########################  tuple is unmutable #######################################################
#########################  tuple unpacking    #######################################################
p=(4,5)

print(p[0])

######### it will throw error ####################################################
p[0]=6

x,y=p

print(x)

print(y)



############ it shows error as there are only two variables in it ##################
x,y,z=p



############# lists are mutable ###########################
data=["acme",50,91.1,(20,2,2021)]
names,count,price,date=data

print(names)

data[0]="Acme"



##################### s