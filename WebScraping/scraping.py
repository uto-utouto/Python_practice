import requests
import requests
from bs4 import BeautifulSoup


url = "https://news.yahoo.co.jp"
response = requests.get(url)

# print(response.text[:500])

# print(requests.headers)

soup = BeautifulSoup(response.content,"html.parser")

print(soup.select("h1"))

print(soup.select("p"))