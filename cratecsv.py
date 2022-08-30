
import csv
from bs4 import BeautifulSoup as bs
import requests
url = 'https://www.rapidtables.com/math/symbols/Basic_Math_Symbols.html'
html = requests.get(url).content
soup = bs(html, 'lxml')
table = soup.find('table', {'class':'dtable'})
headers = [h.text.strip() for h in table.find('thead').find_all('th')]
rows = [[td.text.strip() for td in tr.find_all('td')]
            for tr in table.find('tbody').find_all('tr')]
with open('math_symbols.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(row for row in rows if row)

