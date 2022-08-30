from bs4 import BeautifulSoup
import requests
import csv

with open('/Users/hungrycodie/Desktop/file.csv', 'w', newline='') as output:
    csv_writer = csv.writer(output)
    csv_writer.writerow(['Symbol', 'Definition', 'Example'])


with open(path, 'w+', newline='') as output:
    csv_writer = csv.writer(output)
    csv_writer.writerows


url = 'https://www.rapidtables.com/math/symbols/Basic_Math_Symbols.html'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

table = soup.find('table', {'class': 'dtable'})

tbody = table.find('tbody')

print(table)