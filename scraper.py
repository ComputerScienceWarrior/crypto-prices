from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com'
html = requests.get(url)
e = BeautifulSoup(html.content, 'html.parser')

tbody = e.find('tbody')

if tbody:
    rows = tbody.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        for column in columns:
            print(column.get_text())
