from pymongo import MongoClient
import bs4
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

url='https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mn=NKFS_03_01_12'
driver.get(url=url)


#이름
#높이
#지역

#정보를 전체 가져옴
mountain_list = driver.find_elements_by_class_name('list_info')
for i in mountain_list:
    print(i.text)

#


