import requests
from bs4 import BeautifulSoup
url = 'https://www.enherb.jp/consept/blend/p-e130035-blend.html'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

print(soup.find_all('a'))
