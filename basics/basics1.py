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
data=["acme",50,91.1,(2021,5,8)]
names,count,price,date=data

print(names)

names,count,price,(year,mon,day)=data
year

mon

day

data[0]="Acme"

_,count,shares,_=data
print(shares)


##################### strings ###########

s='Hello'
a,b,c,d,e=s
a

###################### unpacking elements from arbitary length ################
grades=[87,56,67,78,98,77,80]

first,*middle,last=grades
type(middle[0])

sum1=0

for mid in middle:
    sum1=sum1+mid
    
avg=sum1/len(middle)
avg

avg=sum(middle)/len(middle)


####    2nd example
sales=[1,2,3,4,5,6,7,8,9]

*previous_sales,current_sales=sales

avg_sales=sum(previous_sales)/len(previous_sales)


########################### records of multiple data cols ##########

record=("Dave","dave@gmail.com","123-456-789","california","us")
name,email,phone,*address=record
