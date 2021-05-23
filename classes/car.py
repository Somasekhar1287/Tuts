# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:08:53 2021

@author: eagle
"""

class car():
    def __init__(self,car_name,speed):
        self.car_name=car_name
        self.speed=speed
        self.kms=0
        self.litres=0
        
    def details(self):
        print(self.car_name," ",self.speed)
    
    def mileage(self):
        print(self.kms/self.litres)
        
c=car("audi",90.5)
c.kms=100
c.litres=15
c.details()
c.mileage()

######## modifying from methods

class car1():
    def __init__(self,car_name,speed):
        self.car_name=car_name
        self.speed=speed
        self.kms=0
        self.litres=0
        
    def details(self):
        print(self.car_name," ",self.speed)
    
    def mileage(self,kms,lit):
        self.kms=kms
        self.litres=lit
        print(self.kms/self.litres)
        
d=car1("audi",90.5)

d.details()
d.mileage(120,24)