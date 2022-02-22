# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:40:27 2022

@author: student
"""

import pandas as pd
from bs4 import BeautifulSoup
import pymysql, calendar, time, json
import requests
from datetime import datetime
from threading import Timer

class DBUpdater: 
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',
            password='1111', db='INVESTAR10', charset='utf8')
        
        with self.conn.cursor() as curs:
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
                company VARCHAR(40),
                last_update DATE,
                PRIMARY KEY (code))
            """
            curs.execute(sql)
            sql = """
            CREATE TABLE IF NOT EXISTS daily_price (
                code VARCHAR(20),
                date DATE,
                open BIGINT(20),
                high BIGINT(20),
                low BIGINT(20),
                close BIGINT(20),
                diff BIGINT(20),
                volume BIGINT(20),
                PRIMARY KEY (code, date))
            """
            curs.execute(sql)
            
        self.conn.commit()
        self.codes = dict()
    
    def __del__(self):
        self.conn.close()     
    
    # krx 데이터 크롤링
    def read_krx_code(self):
        """KRX로부터 상장기업 목록 파일을 읽어와서 데이터프레임으로 반환"""
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method='\
            'download&searchType=13'
        krx = pd.read_html(url, header=0)[0]
        krx = krx[['종목코드', '회사명']]
        krx = krx.rename(columns={'종목코드': 'code', '회사명': 'company'})
        krx.code = krx.code.map('{:06d}'.format)
        
        return krx
        

    def update_comp_info(self):
        """종목코드를 company_info 테이블에 업데이트 한 후 딕셔너리에 저장"""
        sql = "SELECT * FROM company_info"
        df = pd.read_sql(sql, self.conn)
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]] = df['company'].values[idx]
        
        with self.conn.cursor() as curs:
            sql = "SELECT max(last_update) FROM company_info"
            curs.execute(sql)
            rs = curs.fetchone()
            today = datetime.today().strftime('%Y-%m-%d')
            
            if rs[0] ==None or rs[0].strftime('%Y-%m-%d') < today:
                krx = self.read_krx_code()
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    
                    sql = f"REPLACE INTO company_info (code, compnay, last"\
                        f"_update) VALUES ('{code}','{company}','{today}')"
                    curs.execute(sql)
                    self.codes[code]= company
                    
                    #logs
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%m')
                    print(f"[{tmnow}] #{idx+1:04d} REPLACE INTO compnay_info "\
                          f"VALUES ({code}, {company}, {today})")
                    
                self.conn.commit()
                        
            
            
            
        #self.read_krx_code
'''    
    # naver 데이터 크롤링
    def read_naver(self, code, company, pages_to_fetch):
        pass
    
    def replace_into_db(self, df, num, code, company):
        pass
    
    def update_daily_price(self, pages_to_fetch):
        self.read_naver
        
        self.replace_into_db
        
    def execute_daily(self):
        self.update_company_info()
        self.update_daily_price
'''       

if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.update_company_info()