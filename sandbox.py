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

product_grid = soup.find('div', {"data-comp": "ProductGrid"})
product_dict = {}
for e in product_grid.find_all('div'):
    product = e.find('span', {'data-at': 'sku_item_name'})
    price = e.find('span', {'data-at': 'sku_item_price_list'})
    if product is not None and product.text not in product_dict.keys():
        if price is not None:
            product_dict[product.text] = price.text

for product in product_dict.keys():
    print('PRODUCT: {product}\nPRICE: {price}\n\n'.format(
        product = product, 
        price = product_dict[product]))
