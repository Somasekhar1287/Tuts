# -*- coding: utf-8 -*-
"""
Created on Sat May 22 22:29:08 2021

@author: eagle
"""

### 
i=input("Enter your name: ")
print("Hello ",i)


t=input("How tall you are: ")
t=int(t)
if t>=175:
    print("you are tall")
else:
    print("you are short")
    
    
#### 
prompt="we need your details"
prompt+="\n whats your name: "
msg=" "
while msg!='quit':
    msg=input(prompt)
    print(msg)
    
################ exit loop using flag

prompt="we need your details"
prompt+="\n whats your name: "

flag=True

while flag:
    msg=input(prompt)
    
    if msg=="quit":
        flag=False
    elif msg=="q":
        flag=False
    elif msg=="exit":
        flag=False
    
    print(msg)

############## another way to exit loop


prompt="Enter your fav city"
prompt+="\n(what you visited : ) "

flag=True

while flag:
    msg=input(prompt)
    
    if msg=="quit":
        break
    elif msg=="q":
       break
    elif msg=="exit":
        break
    
    print(msg)
    
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