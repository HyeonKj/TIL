# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:23:42 2022

@author: user
"""
import pymysql
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

for company_code in primary_key:
    url ='http://finance.naver.com/item/sise_day.nhn?code='+company_code
    res = requests.get(url, headers=headers)
    html_str = res.text
    bs_obj = bs4.BeautifulSoup(html_str)
    data= bs_obj.find_all('span',{'class':'tah p11'})
    price_info.append(data[0].text)
    print(f'success load {i}/{len(primary_key)}')
    i+=1
price_info


response = requests.get(url)


# company code
primary_key = []
for i in page_data:
    primary_key.append(i[1])
primary_key


# craw price info
price_info = []
i = 0
for company_code in primary_key:
    url = 'https://finance.naver.com/item/main.naver?code='+company_code
    res = requests.get(url)
    html_str = res.text
    bs_obj = bs4.BeautifulSoup(html_str)
