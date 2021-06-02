exit# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:29:03 2021

@author: eagle
"""

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