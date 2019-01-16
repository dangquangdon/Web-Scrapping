#!/usr/bin/python3
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

# Get the url 
url = "https://www.gigantti.fi/catalog/puhelimet-ja-gps/fi_matkapuhelimet/matkapuhelimet"
# Get the browser
browser = webdriver.Chrome()

# Tell Selenium to get the URL
browser.get(url)

# Tell Selenium to scroll to the botom, wait 3 seconds for the data to load, then continue
page_len = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while (match == False):
    lastCount = page_len
    time.sleep(3)
    page_len = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == page_len:
        match = True

source_data = browser.page_source
with open("source_page.html","w") as f:
    f.write(source_data)

print("Done!")
f.close()

# soup = BeautifulSoup(source_data, "html.parser")
# print(type(soup))

# products = soup.findAll('div', {"class": "mini-product"})

# print(products[6])