import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 99, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}

dict_data = {'c0' : [1,2,3],
             'c1' : [4,5,6],
             'c2' : [7,8,9],
             'c3' : [10,11,12],
             'c4' : [13,14,15]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

ndf = df.reset_index()
print(ndf)

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = 'https://www.chicagomag.com/chicago-magazine/january-2023/our-30-favorite-things-to-eat-right-now/'

hdr = {'User-Agent' : 'Mozilla/5.0'}
req = Request(url, headers=hdr)
page = urlopen(req)

print(page)

soup = BeautifulSoup(page, 'html.parser')

soup.find_all('div', "article-body")

tmp = soup.find_all('div', "article-body")[0]

food_list = []
for item in tmp.find_all('h2'):
    food_list.append(item.text)
    
restaurant_list = []
for item in tmp.find_all('h3'):
    restaurant_list.append(item.text[3:].strip('\xa0'))
    
restaurant_list

money_list = []
address_list = []
for item in tmp.find_all('p'):
    sample_text = item.get_text()
    idx_of_dollar =sample_text.index('$')
    money = sample_text[idx_of_dollar:].split(' ')[0]
    dummy_address = sample_text[idx_of_dollar + len(money)+1:]
    if dummy_address.split(' ')[0]  == 'for':
        dummy_address = dummy_address[dummy_address.index('. ')+2:]
        money_list.append(money)
        address_list.append(dummy_address)


