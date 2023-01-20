from datetime import datetime
import pandas as pd
from dateutil.parser import parse
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')


df['times'] = pd.to_datetime(df['Yr_Mo_Dy'])

def NoTimeMuchine(x):
    if x > datetime(2000,1,1):
        temp_year = x.year - 100
        temp_month = x.month
        temp_day = x.day
        return parse(str(temp_year)+'/'+str(temp_month)+'/'+str(temp_day))
    
    else:
        return x

df['CorrectTime'] = df['times'].apply(NoTimeMuchine)

df['CorrectTime'] = pd.to_datetime(df['CorrectTime'])

df

df.groupby(df.CorrectTime.dt.month).mean()

df.groupby(df.CorrectTime.dt.to_period('M')).mean()

df = pd.DataFrame({'key':['a','b','c'] * 4, 'value':np.arange(12)})

df.groupby('key').mean()

bill_tip = pd.read_csv('C:/Users/pgs66/Desktop/bill_tips.csv')

bill_tip.head()

bill_tip['pct'] = bill_tip['tip'] / bill_tip['total_bill']

bill_tip.groupby('day').agg({'pct' :['mean', 'std']})
bill_tip.groupby('smoker').agg({'pct' :['mean', 'std']})

bill_tip.groupby(['day', 'smoker']).agg({'pct' :['mean', 'std']})

bill_tip.groupby(['day', 'smoker']).agg({'pct' :['count','min','max'],'total_bill' : ['count','min','max']})

groped = bill_tip.groupby(['day', 'smoker'])

groped.agg({'tip':'max', 'size':'sum'})

groped.agg({'pct':['min','max','mean','std'], 'size':'sum'})

groped.agg('mean')

bill_tip.groupby(['day','smoker'], as_index=False).agg('mean')

import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig = plt.figure(figsize=(15,5))

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

sns.regplot(x='age', y='fare', data=titanic, ax=ax1)
sns.regplot(x='age', y='fare', data=titanic, ax=ax2)
plt.show()

from matplotlib import font_manager, rc

df = pd.read_excel('C:/Users/pgs66/Desktop/시도별 전출입 인구수.xlsx')

df.head()

font_path = ('C:/Users/pgs66/Desktop/malgun.ttf')
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

sr_one = df.loc['경기도']





