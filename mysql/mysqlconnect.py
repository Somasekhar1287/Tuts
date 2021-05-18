# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:29:04 2021

@author: eagle
"""

import mysql.connector 

try:
    mydb=mysql.connector.Connect(host="localhost",user="root",password="")
except Exception as e:
    print(e)
    
#mycursor=mydb.cursor()