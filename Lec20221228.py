import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
item = ['TV', '냉장고', '믹서', '선풍기', '전자렌지', '컴퓨터', '선풍기', '믹서', '믹서']
le.fit(item)
labels = le.transform(item)
labels
#데이터를 라벨 인코딩에서 주어진 모든 범주에 따라서 값을 지정하는 작업
from sklearn.preprocessing import OneHotEncoder

labels = labels.reshape(-1,1)

oh_encoder = OneHotEncoder()
oh_encoder.fit(labels)

oh_labels = oh_encoder.transform(labels)

oh_labels.toarray()

ages = [20, 22, 25, 27, 21]
bins = [18,25, 35, 75, 100]

cats = pd.cut(ages, bins)

cats.codes

cats.categories

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

pd.cut(ages, bins, labels=group_names)

an_ages = [18, 25, 42, 73]
an_cats = pd.cut(an_ages, bins, right=False)
an_cats

data = np.random.randn(1000)
cats = pd.qcut(data, 4)
cats
item

df = pd.DataFrame(item)
pd.get_dummies(df)

ts_me = pd.date_range(start='2019-01-01',
                      end = None,
                      periods=6,
                      freq = '3M',
                      tz = 'Asia/Seoul')

ts_me

pr_m = pd.period_range(start = '2019-01-01',
                       periods = 3,
                       freq='M')

#Vectorization

x = [{'city':'seoul', 'temp':10.0}, {'city':'Dubai', 'temp' : 33.5}, {'city':'LA','temp':20.0}]

x

from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer(sparse=False)

vec.fit_transform(x)

v=DictVectorizer()
X=v.fit_transform()
X

text = ['떴다 떴다 비행기 날아라 날아라',
        '높이 높이 날아라 우리 비행기',
        '내가 만든 비행기 날아라 날아라',
        '멀리 멀리 날아라 우리 비행기']

from sklearn.feature_extraction.text import CountVectorizer

vec2 = CountVectorizer()
t = vec2.fit_transform(text).toarray()

#TFIDF 전체문서에서 출현 비중이 높은단어에 낮은가중치
#출현비중이 낮은단어에 높은 가중치

from sklearn.feature_extraction.text import TfidfVectorizer
tfigf = TfidfVectorizer()

x2 = tfigf.fit_transform(text)
x2.toarray()

x3 = pd.DataFrame(x2.toarray(), columns= tfigf.get_feature_names_out())
x3









