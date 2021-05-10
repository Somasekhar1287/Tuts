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


items=[1,7,10,35,46]


def sum_items(item):
    head,*tail=item
    return head+sum(tail) if tail else head
  
sum_items(items)  

########################### records of multiple data cols ##########

record=("Dave","dave@gmail.com","123-456-789","california","us")
name,email,phone,*address=record


#######################################################################
record=("Acme",51,36.7,(12,8,2012))
names,*_,(*_,year)=record
names
year

####################### finding largest and smallest number ###########

import heapq

nums=[1,89,76,23,12,36,9]
print(heapq.nlargest(1,nums))
print(heapq.nlargest(3,nums))

print(heapq.nsmallest(3,nums))
print(heapq.nsmallest(2,nums))

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])



################## finding common in dictonaries ####################

a={
   'x':1,
   'y':2,
   'z':3
   }
b={
   'w':4,
   'x':12,
   'y':2
   }
print(a)
print(b)

print(a.keys()&b.keys())
print(a.keys()-b.keys())

c=a.items()&b.items()
print(c)
########################### Riddle ####################################

import random


riddle=[{'statement': 'we can sit but we cannot take it','answer':'chair'},
        {'statement': "I'm tall when I'm young and I'm short when I'm old. What am I?",'answer':'candle'},
        {'statement': 'What can travel around the world while staying in a corner?','answer':'stamp'},
        {'statement': 'What has hands but can not clap?','answer':'clock'},
        {'statement': 'You can drop me from the tallest building and I will be fine, but if you drop me in water I die. What am I?','answer':'paper'},
        {'statement': 'What has a head and a tail, but no body?','answer':'coin'}
        ]

#leng=len(riddle)

item=random.choice(riddle)
print(item['statement'])
answer=input("ENTER THE ANSWER: ")
if item['answer']==answer:
    print("correct answer")
else:
    print("wrong answer")


########################################## bubble sort #################################

def bubble_sort(item_list):
    for item in range (len(item_list)-1,0,-1):
        for idx in range(item):
            if item_list[idx]>item_list[idx+1]:
                temp=item_list[idx]
                item_list[idx]=item_list[idx+1]
                item_list[idx+1]=temp
    return item_list

item_list=[89,2,1,67,11,5]
items=bubble_sort(item_list)
