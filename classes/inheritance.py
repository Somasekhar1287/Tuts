# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:17:33 2021

@author: eagle
"""


########## inheritance

class car():
    def __init__(self,model,year):
        self.model=model
        self.year=year
    
    def get_car(self):
        return (self.model,"",self.year)

class sub_car(car):
    def __init__(self,model,year):
        super().__init__(model,year)
       
        

scar=sub_car("electric",2020)
print(scar.get_car())

############ sub class properties

class car():
    def __init__(self,model,year):
        self.model=model
        self.year=year
    
    def get_car(self):
        return (self.model,"",self.year)

class sub_car(car):
    def __init__(self,model,year):
        super().__init__(model,year)
        self.mode="battery"
        
    def sproperty(self):
        print("this is car mode"+self.mode)
        
        
scar=sub_car("electric",2020)
print(scar.get_car())
scar.sproperty()
