from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import webbrowser
import requests
import sys
import os

# ser = Service('./chromedriver')
# wd = webdriver.Chrome(service = ser)
wd = webdriver.Chrome(ChromeDriverManager().install())
# url = 'https://www.airportal.go.kr/knowledge/airports/KfMain01.jsp?df_area=IATA%C4%DA%B5%E5'
url = 'https://www.airportal.go.kr/knowledge/airports/KfMain01.jsp?df_area=IATA%C4%DA%B5%E5&df_start=7660&df_end=7666&df_count=10&df_search_target=&df_search_keyword=&df_sort=&df_desc=&df_search_keyword2=null'
wd.get(url)
#699~766
#airport 공항명
#iata IATA
#icao ICAO
#country 국가명
#city 도시명
airport = []
iata = []
icao = []
country = []
city = []

result = []

# page = 1
# while page < 69:
#     for i in range(1,11):
#         airport.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(3) > a').text)
#         iata.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(4)').text)
#         icao.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(5)').text)
#         country.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(6)').text)
#         city.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(7)').text)
#
#
#     time.sleep(2)
#     # 페이지 Next 버튼
#     nextBtn = wd.find_element(By.CSS_SELECTOR,'body > table > tbody > tr:nth-child(5) > td:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(22) > td > table > tbody > tr > td:nth-child(5) > a').click()
#     page+=1

#마지막페이지
for i in range(1,7):
    airport.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(3) > a').text)
    iata.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(4)').text)
    icao.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(5)').text)
    country.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(6)').text)
    city.append(wd.find_element(By.CSS_SELECTOR,'table > tbody > tr:nth-child('+str(2*i)+') > td:nth-child(7)').text)



for i in range(len(airport)):
    # print(airport[i])
    # print(iata[i])
    # print(icao[i])
    # print(country[i])
    # print(city[i])
    c1 = airport[i]
    c2 = iata[i]
    c3 = icao[i]
    c4 = country[i]
    c5 = city[i]
    result.append([c1,c2,c3,c4,c5])
print(result)
data = pd.DataFrame(result)
data.columns = ['Airport','IATA','ICAO','Country','City']
filename = 'airportal4.csv'
data.to_csv(filename,index = True)

wd.close()