import argparse
import time

from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("C:\/Users\/butte\/Documents\/ChromeDriver\/chromedriver", chrome_options=options)

def main():
    # argparse
    # processing
    # cleanup
    pass

if __name__: '__main__':
    main()