from bs4 import BeautifulSoup
import random
import requests
import json
import re

url = 'https://www.vinorus.ru/ru-RU/about/contacts.aspx'
data = []
f = open('useragent.txt', 'r')
useragent = [line.strip() for line in f]
useragent = random.choice(useragent)
headers = {
    'User-Agent': useragent
}


r = requests.get(url, headers=headers).text



soup = BeautifulSoup (r, 'lxml')
peoples = soup.select('.col-sm-4.mb-4')



for p in peoples:
    name = str(p.find('b'))
    name = name.replace('<b>','').replace('</b>','')
    if name == 'None':
        continue
    else:
        position = p.br.next_sibling.replace(' \r','').replace('\r','')
        tel = p.br.next_sibling.next_sibling.next_sibling.replace('тел.: ','').replace(' \r','').replace('\r','')
        mail = p.br.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.replace('e-mail: ','').replace(' \r','').replace('\r','')
        data.append({
            'Имя': name,
            'Должность': position,
            'Телефон': tel,
            'Почта': mail
        })

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)
