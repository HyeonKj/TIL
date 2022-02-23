# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 09:57:39 2022

@author: user
"""

import pandas as pd
import pymysql

table = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')
table2= table[0]
head = table[0].columns
body = table[0].iloc[:,:]
print(head)
len(table[0])
body = table[0].iloc[:,[0,1]]
print(body)


con, cur =None, None
data1, data2="",""
row=None

conn=pymysql.connect(host='localhost',user='root',password='1111', \
                     db='INVESTAR', charset='utf8')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS company_info (company char(20), code char(6))")
    
for data in table2:
    row1 = data[0]
    row2 = data[1]
    
    sql="""insert into INVESTAR (company, code) values(%s, %s);"""
    cur.execute(sql,(row1, row2))

conn.commit()
conn.close()
