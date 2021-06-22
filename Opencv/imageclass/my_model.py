0# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:29:06 2021

@author: eagle
"""

import cv2 as cv
import os
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

DataDir="C://Users//eagle//OneDrive//Documents//git//python//Tuts//Tuts//Opencv//imageclass"
categories=["sekhar","suji"]

img_size=50
clear_view=200
train_data=[]

img1=[]

def create_train_data():
    for category in categories:
        path=os.path.join(DataDir,category)
        class_num=categories.index(category)
        for img in os.listdir(path):
            try:
                img_array=cv.imread(os.path.join(path,img))
                #img1.append(cv.resize(img_array,(clear_view,clear_view)))
                new_img_array=cv.resize(img_array,(img_size,img_size))
                train_data.append([new_img_array,class_num])
            except Exception as e:
                print(e)

create_train_data()

print(len(train_data))          

print(type(train_data))

X=[]
Y=[]

for features,label in train_data:
    X.append(features)
    Y.append(label)
    
    
X=np.array(X).reshape(-1,img_size,img_size,3)

Y=np.array(Y)    

X=X/255

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)



     



def plot_sample(x,y,index):
  plt.figure(figsize=(15,2))
  #plt.imshow(cv.cvtColor(x[index],cv.COLOR_BGR2RGB))
  plt.imshow(x[index])
  plt.xlabel(categories[y[index]])

plot_sample(X_train,Y_train,10)

#X_train=X_train/255
#X_test=X_test/255

Filter_size=3
Num_filters=32
Input_size=32
Maxpool_size=2
Batch_Size=32
Steps_per_Epoch=X_train.shape[0]//Batch_Size
Epochs=10


import  tensorflow as tf
from keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras import models
model=Sequential()
model.add(layers.Conv2D(filters=Num_filters,activation="relu",kernel_size=(Filter_size,Filter_size),input_shape=(50,50,3)))
model.add(layers.Conv2D(filters=Num_filters,activation="relu",kernel_size=(Filter_size,Filter_size)))
model.add(layers.MaxPooling2D((Maxpool_size, Maxpool_size)))
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(filters=Num_filters*2,activation="relu",kernel_size=(Filter_size,Filter_size)))
model.add(layers.Dropout(0.2))
model.add(layers.Conv2D(filters=Num_filters*2,activation="relu",kernel_size=(Filter_size,Filter_size)))
model.add(layers.Dropout(0.2))
model.add(layers.MaxPooling2D((Maxpool_size, Maxpool_size)))
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(128,activation="relu"))
model.add(layers.Dense(1,activation="sigmoid"))
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model.fit(X_train,Y_train,validation_data=(X_test,Y_test),epochs=500,batch_size=50)

train_data_generator=tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=40,width_shift_range=0.1, height_shift_range=0.1,shear_range=0.1,zoom_range=0.1, horizontal_flip=True)
traingset=train_data_generator.flow(X_train,Y_train,batch_size=Batch_Size)
model.fit(traingset,validation_data=(X_test,Y_test),epochs=300,verbose=1)

model.evaluate(X_test,Y_test)
y_pred=model.predict(X_test)
y_classes=[np.argmax(element) for element in y_pred]
print(y_classes[:20])
print(Y_test[:20])

plot_sample(X_test,Y_test,2)

print(categories[y_classes[2]])
