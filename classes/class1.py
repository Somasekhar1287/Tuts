# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:47:30 2021

@author: eagle
"""

class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def student_print(self):
        print("Name is: ",self.name.title()," Age is: ",self.age)
        
        
student("soma",33).student_print()
student=student("sanju","22")
student.student_print()



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
