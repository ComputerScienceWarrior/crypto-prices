from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com'
html = requests.get(url)
e = BeautifulSoup(html.content, 'html.parser')

tbody = e.find('tbody')

data = []

if tbody:
    rows = tbody.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        row_data = []
        for column in columns:
            text = column.get_text(strip=True)
            if text:
                row_data.append(text)
        if row_data:
            data.append(row_data)

for item in data:
    print(item)
