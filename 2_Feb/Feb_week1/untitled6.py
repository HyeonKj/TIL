import pymysql

import pandas as pd

url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'

# HTML 데이터 프레임 읽기
tables = pd.read_html(url)
tables2 = tables[0]
print(len(tables2))

# 데이터 프레임에서 회사명, 종목코드 열만 출력
company = tables2
print(company)

# HTML을 DB에 밀어넣기
con, cur = None, None
data1, data2 = "",""
row = None

conn = pymysql.connect(host= 'localhost', user = 'root', password = '1111', db = 'investar', charset= 'utf8')
cur = conn.cursor()

cur.execute("create table if not exists investar.company_info (company char(10), number char(8))")

for data in company:
    row1=data[0]
    row2=data[1]
    
        
    sql = """insert into company_info (company, number) values (%s, %s);"""
    cur.execute(sql,(row1,row2))
print(data[0])

conn.commit()
conn.close()