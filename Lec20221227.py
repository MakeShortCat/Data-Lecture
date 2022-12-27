import re

re.search('python', '10 python')

#findall : 인수 문자열에서 패턴을 만족하는 모든 문자열을 추출

re.findall('[a-z]+', 'python 3 verson programing')

#compile : 인수 패턴을 컴파일하여 정규식 객체를 변환한다

re.search(r'[A-Z]', 'a=123 : B = 456')
p = re.compile(r'[A-Z]')
p.search('a = 123 : B = 456')

p = re.compile(r'([^_A-Za-z]\w*)\s*=\s(\d+)')
m= p.search('a = 123')
m.groups()

p = re.compile(r'[^\w\s]+')
m= p.search('a = 123')
m.group()
import pandas as pd
url ='https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv', encoding='euc-kr')
df
df['일자'].value_counts()

import folium
seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12)
seoul_map.save('./s.html')

df = pd.read_excel('C:/Users/pgs66/Desktop/seoul_univ.xlsx', engine='openpyxl')
df

df.columns = ['name', 'lat', 'long']

df.head()

seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12 , tiles='Stamen Terrain')

for name, lat, lng in zip(df.name, df.lat, df.long):
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)

seoul_map.save('./s.html')

df = pd.read_excel('C:/Users/pgs66/Desktop/popul.xlsx', index_col='구분', engine='openpyxl')

df.columns = df.columns.map(str)

import json

geo_path = 'C:/Users/pgs66/Desktop/경기도행정구역경계.json'

try:
    geo_data = json.load(open(geo_path, encoding = 'utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))

year = '2017'
g_map = folium.Map(location=[37.5502, 126.982],zoom_start=12 , tiles='Stamen Terrain')

folium.Choropleth(geo_data=geo_data, data=df[year], columns=[df.index, df[year]],
                  fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
                  key_on='feature.properties.name').add_to(g_map)
g_map.save('./g.html')
df.head()

import seaborn as sns

df = sns.load_dataset('titanic')
df.head()

df.info()

df.isnull().sum()

df.dropna(axis=1, thresh=500).columns
df.columns

len(df.age)
len(df.dropna(subset = ['age'], how='any', axis = 0))

mean_age = df['age'].mean(axis=0)
df['age'].fillna(mean_age, inplace=True)
print(df['age'].head(10))

most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq)

df['embark_town'].fillna(most_freq, inplace =True)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['legned.loc'] = 'upper center'

#자료초기화

y= pd.Series([1,4,2,4, np.nan, np.nan, 7,5,4, np.nan, np.nan, 1,2])
x= np.arange(0, len(y))

#차트 생성
fig, ax = plt.subplots(nrows=1, ncols=4, figsize = (25,3))
ax[0].plot(x, y.fillna(0), color = 'red', label='updated')
ax[0].plot(x, y, label='original')
ax[0].set_title('zero')

ax[1].plot(x, y.fillna(y.mean()), color = 'red', label='updated')
ax[1].plot(x, y, label='original')
ax[1].set_title('zero')

ax[2].plot(x, y.fillna(1), color = 'red', label='updated')
ax[2].plot(x, y, label='original')
ax[2].set_title('zero')

ax[3].plot(x, y.interpolate(), color = 'red', label='updated')
ax[4].plot(x, y, label='original')
ax[5].set_title('zero')

df = pd.DataFrame({'c1':['a','a','b','a','b'],
                   'c2':[1,1,1,2,2],
                   'c3':[1,2,2,2,2]})





