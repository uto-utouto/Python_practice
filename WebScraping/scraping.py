#requestsモジュールをインポート
import requests
#BeautifulSoupモジュールをインポート
from bs4 import BeautifulSoup
#seleniumのwebdriverモジュールをインポート
#from selenium import webdriver
from time import sleep

#driver = webdriver.Chrome('C:\Users\kfg_admin\Documents\練習\WebScraping\chromedriver_win32\chromedriver.exe')

url = "https://news.yahoo.co.jp"
response = requests.get(url)

# print(response.text[:500])

# print(requests.headers)

soup = BeautifulSoup(response.content,"html.parser")

print(soup.select("h1"))

print(soup.select("p"))