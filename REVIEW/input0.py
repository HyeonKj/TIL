# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:56:02 2022

@author: user
"""

import pymysql 

conn, cur = None, None 
sql = ""

#메인 코드
conn=pymysql.connect(host='localhost',user='root',password='1111', \
                     db='shoppingDB', charset='utf8')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS userTable (id char(4), userName \
            char(15), email char(20), birthYear int)")
    
cur.execute("INSERT INTO userTable VALUES('john', 'John bann', 'john@naver.com',1990)")
cur.execute("INSERT INTO userTable VALUES('kim', 'kim mike', 'kim@naver.com',1980)")
cur.execute("INSERT INTO userTable VALUES('park', 'park minseo', 'park@naver.com',2000)")

conn.commit()
conn.close()

