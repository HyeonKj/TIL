# # -*- coding: utf-8 -*-
# """
# Created on Thu Feb 10 10:26:08 2022

# @author: user
# """
# import pandas as pd
# import pymysql
# from datetime import timedelta
# from datetime import datetime
# import re

# class MarketDB:
#     def __init__(self):
#         self.conn = pymysql.connect(host='localhost', user='root',
#                         password='1111', db='INVESTAR10', charset='uft8')
        
#         self.get_comp_info()
#         self.codes = {}
        
#     def __del__(self):
#         self.conn.close()
        
#     def get_comp_info(self):
    
#         """종목코드를 company_info 테이블에 업데이트 한 후 딕셔너리에 저장"""
#         sql = "SELECT * FROM company_info"
#         krx = pd.read_sql(sql, self.conn)
#         for idx in range(len(krx)):
#             self.codes[krx['code'].values[idx]] = krx['company'].values[idx]
       
    
    
#     def get_daily_price(self,code,start_date=None, end_date = None):
#         """KRX 종목의 일별 시세를 데이터 프레임 형태로 반환
#             - code       : krx 종목코드('145020') 또는 상장기업명('휴젤')
#             - start_date : 조회 시작일('2022-02-10'), 미입력 시 1년 전 오늘
#             - end_date   : 조회 종료일('2022-12-31'), 미입력 시 오늘 날짜
#             """
#         if start_date is None:
#             one_year_ago = datetime.today() - timedelta(days=365)
#             start_date = one_year_ago.strtime('%Y-%m-%d')
#             print("start_date is initialized to '{}'".format(start_date))
            
#         else:
#             start_lst = re. split('\D+',start_date)
            
#             start_year = int(start_lst[0])
#             start_month = int(start_lst[1])
#             start_day = int(start_lst[2])
#             if start_year < 1900 or start_year > 2200:
#                 print(f"ValueError: start_year({start_year:d}) is wrong.")
#                 return
#             if start_month < 1 or start_month >12:
#                 print(f"ValueError: start_month({start_month:d}) is wrong.")
#                 return
#             if start_day < 1 or start_day > 31:
#                 print(f"ValueError: start_day({start_day:d}) is wrong.")
#                 return
#             start_date = f"{start_year:04d}-{start_month:02d}-{start_day:02d}"
            
#         if end_date is None:
#             end_date = datetime.today().strftime('%Y-%m-%d')
#             print("end_date is initalized to '{}'".format(end_date))
            
#         else:
#             end_lst = re. split('\D+',start_date)
            
#             end_year = int(start_lst[0])
#             end_month = int(start_lst[1])
#             end_day = int(start_lst[2])
#             if end_year < 1900 or start_year > 2200:
#                 print(f"ValueError: start_year({start_year:d}) is wrong.")
#                 return
#             if end_month < 1 or start_month >12:
#                 print(f"ValueError: start_month({start_month:d}) is wrong.")
#                 return
#             if end_day < 1 or start_day > 31:
#                 print(f"ValueError: start_day({start_day:d}) is wrong.")
#                 return
#             end_date = f"{start_year:04d}-{start_month:02d}-{start_day:02d}"
            
#         codes_keys = list(self.codes.keys())
#         codes_values = list(self.codes.values())
        
#         if code in codes_keys:
#             pass
#         elif code in codes_values:
#             idx = codes_values.index(code)
#             code = codes_keys[idx]
#         else:
#             print(f"ValueError: Code({code}), doesn't exist.")
            
#         sql = f"SELECT * FROM daily_price WHERE code = '{code}'"\
#             f"and date >= '{start_date}' and date <='{end_date}'"
#         df = pd.read_sql(sql, self.conn)
#         df.index = df['date']
#         return df
            
# dbm = MarketDB()
# df= dbm.get_daily_price('145020', "2016-01-01","2022-02-09")
# print(df)
            
            
            
            
            
            
            
            