import os
import csv
from bs4 import BeautifulSoup
import requests
from collections import defaultdict


def file(path):


    url = 'https://www.rapidtables.com/math/symbols/Basic_Math_Symbols.html'
    os.chdir(path)
    with open('math.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['character', 'description', 'latex', 'unicode'])
    file = requests.get(url)
    soup = BeautifulSoup(file.text, 'html.parser')
    data = soup.find('div',{'id':'doc'})
    datatable = data.find('table')
    datatable = datatable.find('tbody').find_all('tr')
    k=0
    for i in range(0,len(datatable)):
        for j in range(0,4):    
            if j == 0:
                datatable[i].contents[j].find_all('a')
                temp = datatable[i].contents[j].find_all('a')
                temp = temp[0].text
                temp = temp.split('\n        ')
                temp = temp[1:]
                with open('math.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([temp])
                    k=k+1
            else:
                with open('math.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([''])

            k=k+1
            
path = input("Enter Path to Save math.csv: ")
file(path)
