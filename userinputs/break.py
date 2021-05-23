# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:29:28 2021

@author: eagle
"""

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