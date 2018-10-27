import requests
from bs4 import BeautifulSoup


url = 'https://www.enherb.jp/consept/blend/p-e130035-blend.html'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
contents_list = soup.find('div', class_='contents_list')

for content in contents_list.find_all('a'):
  link = content['href']
  new_link_content = requests.get(link)
  new_content = BeautifulSoup(new_link_content.text, 'html.parser')
  stuff = new_content.find(text='英名') 
  print(stuff.parent.parent.next_sibling.text)

