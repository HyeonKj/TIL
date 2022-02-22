# -*- coding: utf-8 -*-
"""
네이버로 항공권 예매하기 
@author: HyeonKj

"""
import time
from selenium import webdriver



#selenium을 사용해서 사이트 직접 열기
driver=webdriver.Chrome(r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
url="https://flight.naver.com/"
driver.get(url)
time.sleep(1)
# 도착지 선택
destination = "LAX"  # 로스앤젤리스,미국
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i').click()
time.sleep(1)
# 도착지 입력
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[1]/div/input').send_keys(destination)
time.sleep(1)
# 목록 중 첫번 째 선택
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/div/a/div[1]/i[1]').click()
time.sleep(1)

#가는 날 
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]').click()
time.sleep(2)

#오는날 선택
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td[5]').click()
time.sleep(2)

#항공권 검색
driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()
time.sleep(30)

#최저가 항공권 정보 불러오기
elements=driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div[3]/div[1]')
print(elements.text) #원래 목적지로 가는 가장 저렴한 항공 정보 출력
 
