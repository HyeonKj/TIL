# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:11:20 2022

@author: user
"""
import pymysql
import requests
import bs4
#첫번째 미션 
# company info
url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
res = requests.get(url)
html_str = res.text
bs_obj = bs4.BeautifulSoup(html_str)
data_head = bs_obj.find_all('th')
data = bs_obj.find_all('td')

columns = [i.text for i in data_head]

page_data = []
temp = []
target = ['\r','\n','\t']
for i in data:
    if len(temp) == len(columns):
        page_data.append(temp)
        temp = []
    if len(temp) == 7:
        x = i.text
        for j in target:
            x = x.replace(j,'')
        temp.append(x)
    else:
        temp.append(i.text)


# sql code
conn = pymysql.connect(host='localhost',user='root',password='1111',
                       db='INVESTAR',charset='utf8')
cur = conn.cursor()
# sql part
cur.execute(f'create table if not exists company_info'
            f'({columns[0]} char(25),'
            f'{columns[1]} char(6))')

sql="""insert into company_info values (%s, %s);"""
for i,data in enumerate(page_data):
    
    sql = """insert into company_info (회사명,종목코드) values (%s, %s);"""   
    cur.execute(sql, (data[0], data[1]))
    
# 두 번째 미션 
# company code
primary_key = []
for i in page_data:
    primary_key.append(i[1])
primary_key


# craw price info
price_info = []
i = 1
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
for company_code in primary_key:
    url = 'http://finance.naver.com/item/sise_day.nhn?code='+company_code
    res = requests.get(url,headers=headers)
    html_str = res.text
    bs_obj = bs4.BeautifulSoup(html_str)
    data = bs_obj.find_all('span',{'class':'tah p11'})
    price_info.append(data[0].text)
    print(f'success load {i}/{len(primary_key)}')
    i += 1
    if i == 50:
        break
price_info

conn = pymysql.connect(host='localhost',user='root',password='1111',
                       db='INVESTAR',charset='utf8')
cur = conn.cursor()
cur.execute(f'create table if not exists price_info('
            f'{columns[1]} char(6),'
            f'today_price char(20))')
cur.execute('alter table price_info add constraint foreign key(종목코드) references company_info(종목코드);')
cur.execute('ALTER DATABASE investar CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;')

cur.execute('ALTER TABLE company_info CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
sql = """insert into price_info values (%s, %s);"""
for i in range(len(primary_key)):
    cur.execute(sql,(primary_key[i],price_info[i]))


conn.commit()
conn.close()
