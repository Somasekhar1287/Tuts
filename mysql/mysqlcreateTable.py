# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:09:07 2021

@author: eagle
"""

import mysql.connector
from mysql.connector import errorcode

try:
    conn=mysql.connector.connect(host="localhost",
                             user="root",
                             password="password",
                             database="py_db"
                             )
    
    cursor=conn.cursor()
    #create_query="CREATE TABLE Users(id int NOT NULL,User_name VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL)"
    #cursor.execute(create_query)
    create_movieList="CREATE TABLE movies(m_id int NOT NULL,m_name VARCHAR(255) NOT NULL,m_genre VARCHAR(255) NOT NULL)"
    cursor.create(create_movieList)
    create_reviews="CREATE TABLE reviews(user_id int,movie_id int,rating float not null,intrest boolean,FOREIGN KEY(movie_id) REFERENCES movies(m_id),FOREIGN KEY (user_id) REFERENCES Users(id) )"
    cursor.execute(create_reviews)
    #insert_query="INSERT INTO Users(id,User_name,email) VALUES(12021,%s,%s)"
    #val=("soma sekhar","eaglesekhar03@gmail.com")
    #cursor.execute(insert_query,val)
    conn.commit()
    select_query="SELECT *FROM Users"
    cursor.execute(select_query)
    myres=cursor.fetchall()
    print(myres)
    
    
except mysql.connector.Error as err:
    if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
        print("something wrong with username and password")
    elif err.errno==errorcode.ER_BAD_DB_ERROR:
        print("Database doesnot exist")
    else:
        print(err)
else:
    conn.close()
    