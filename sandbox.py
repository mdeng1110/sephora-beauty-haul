from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("C:\/Users\/butte\/Documents\/ChromeDriver\/chromedriver", chrome_options=options)
driver.get("https://www.sephora.com/search?keyword=urban decay&pageSize=300")
page_source = driver.page_source.encode('utf-8')
soup = BeautifulSoup(page_source, 'lxml')
