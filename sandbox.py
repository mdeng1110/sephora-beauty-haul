from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("C:\/Users\/butte\/Documents\/ChromeDriver\/chromedriver", chrome_options=options)

page = 1
product_dict = {}

while True:
        driver.get("https://www.sephora.com/search?keyword=urban%20decay&pageSize=12&currentPage=" + str(page))
        page_source = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(page_source, 'lxml')
        if soup.find('div', {'data-comp': 'NoResults Box'}):
                print('DONE!')
                break
        
        product_grid = soup.find_all('div', {"data-comp": "ProductGrid"})

        for block in product_grid[0].find_all('div', {'class': 'css-dkxsdo'}):
                for b in block.find_all('div', {'class': 'css-12egk0t'}):
                        brand = b.find('span', {'data-at', 'sku_item_brand'})
                        product = b.find('span', {'data-at': 'sku_item_name'}) 
                        price = b.find('span', {'data-at': 'sku_item_price_list'}) 
                        product_dict[product.text] = price.text 
        page += 1

for product in product_dict.keys():
    print('PRODUCT: {product}\nPRICE: {price}\n\n'.format(
        product = product, 
        price = product_dict[product]))
