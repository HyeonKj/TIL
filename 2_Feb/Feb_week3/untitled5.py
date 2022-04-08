# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:19:02 2022

@author: user
"""

import pandas as pd

code1 = pd.read_csv(r'C:\Users\user\Desktop\빅데이터\python\DBMS\data.csv',
                         encoding='cp949')
print(code1)

import pymysql 

conn, cur = None, None 
data1, data2, data3, data4 = "","","",""
row=None

#메인 코드
conn=pymysql.connect(host='localhost',user='root',password='1111', \
                     db='mulcam', charset='utf8')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS userTable (userName char(4), usersex \
            char(2), class char(2), attend char(3))")
    
cur.execute("INSERT INTO userTable VALUES('강주오', '남', 'A','O')")
cur.execute("INSERT INTO userTable VALUES('서명교', '남', 'A','O')")
cur.execute("INSERT INTO userTable VALUES('김윤명', '여', 'A','O')")
cur.execute("INSERT INTO userTable VALUES('김성겸', '남', 'A','O')")
cur.execute("INSERT INTO userTable VALUES('배명진', '여', 'A','O')")
cur.execute("INSERT INTO userTable VALUES('박은선', '여', 'A','O')")
cur.execute("INSERT INTO userTable VALUES('김요셉', '남', 'A','O')")
cur.execute("INSERT INTO userTable VALUES('백주원', '여', 'A','O')")
cur.execute("INSERT INTO userTable VALUES('서승덕', '남', 'B','O')")
cur.execute("INSERT INTO userTable VALUES('심동혁', '남', 'B','O')")
cur.execute("INSERT INTO userTable VALUES('이영림', '여', 'B','O')")
cur.execute("INSERT INTO userTable VALUES('이인준', '남', 'B','O')")
cur.execute("INSERT INTO userTable VALUES('하승철', '남', 'B','O')")
cur.execute("INSERT INTO userTable VALUES('황규진', '여', 'B','X')")
cur.execute("INSERT INTO userTable VALUES('박정혜', '여', 'A','X')")
cur.execute("INSERT INTO userTable VALUES('백승현', '남', 'B','X')")
cur.execute("INSERT INTO userTable VALUES('장성우', '남', 'B','X')")
cur.execute("INSERT INTO userTable VALUES('이준영', '남', 'B','X')")
cur.execute("INSERT INTO userTable VALUES('서준식', '남', 'B','X')")

conn.commit()

cur.execute("SELECT*FROM userTable")

print("이름    성별    소속    참석여부")
print("___________________________________")




conn.close()