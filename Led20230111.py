import pandas as pd
import numpy as np
from datetime import datetime
import prophet


now = datetime.now()
datetime(2023, 1, 11).strftime('%m-%d')
now

now.year, now.month, now.day

delta = datetime(2022, 7, 1) - datetime(2023, 1, 11)

abs(delta)

from datetime import timedelta

start = datetime(2022, 7, 1)
start + timedelta(12)

start - 2 *timedelta(12)

start.strftime('%Y-%m-%d')

value = '2011-01-03'

datetime.strptime(value, '%Y-%m-%d')

from dateutil.parser import parse
datetime(2001,)
parse('2023-01-03')>datetime(2001,1,1)

parse('Jan 31, 1997 10:45 PM')

date_strs = ['2011-07-06 12:00:00', '2011-08-06 12:00:00']

results = pd.to_datetime(date_strs)

results

idx = pd.to_datetime(date_strs + [None])

idx[2]

pd.isnull(idx)

dates = [datetime(2011,1,2), datetime(2011,1,5),
         datetime(2011,1,7), datetime(2011,1,8),
         datetime(2011,1,10), datetime(2011,1,12)]

ts = pd.Series(np.random.randn(6), index=dates)

ts

ts + ts[::2]

stamp = ts.index[2]

stamp

ts[stamp]


ts['1/10/2011']

ts['20110110']

longer_ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods=1000))

longer_ts['2002-05':'2002-06']

longer_ts.truncate(after='1/9/2022')

dates = pd.date_range('1/1/2000', periods = 100, freq='W-Wed')

long_df = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=['colorado', 'taxas' ,'ney york', 'ohio'])

long_df.loc['5-2001']

dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000','1/2/2000','1/2/2000','1/3/2000','1/3/2000',])

dup_ts = pd.Series(np.arange(6), dates)

dup_ts

grouped = dup_ts.groupby(level=0)

grouped.mean()

ts

ts.resample('D')

index = pd.date_range('2012-04-01', '2012-06-01')

index

pd.date_range('2012-04-01', periods=20)

pd.date_range(end = '2012-04-01', periods=20)

pd.date_range('2000-01-01', '2000-12-01', freq='BM')

pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True)

pd.date_range('2000-01-01', '2000-01-07 23:59', freq='3h')

pd.date_range('2012-04-01', periods=20, freq='1h30min')


ts
ts.shift(1)

ts  - ts.shift(1)

ts / ts.shift(1) -1

rng = pd.date_range('2000-01-01', periods=100, freq='D')

ts = pd.Series(np.random.randn(len(rng)), index=rng)

ts.resample('M').mean()

rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.arange(12), index=rng)
ts
ts.resample('5min').sum()

ts.resample('5min', closed='left').sum() #0부터 4까지 시작값을 왼쪽 값으로 한다

ts.resample('5min', closed='right').sum() #0부터 5까지 마지막값인 오른쪽 값을 계산에 포함한다

ts.resample('5min', closed='right', label='right').sum() #0부터 5까지 마지막값인 오른쪽 값을 계산에 포함한다

ts.resample('5min', closed='right',
            label='right', loffset='+1s').sum()

## 리샘플링: 시계열의 빈도를 변환하는 과정

frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range('1/1/2000', periods=2,
                                         freq='W-WED'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])

frame.resample('D')

df_daily = frame.resample('D').asfreq()
df_daily

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')


df['times'] = pd.to_datetime(df['Yr_Mo_Dy'])

df['times']
df.times.dt.year.unique()

df.loc[3, 'times'].year

parse('2022-01-01')


datetime.strptime(value, '%Y-%m-%d')

df['times']


def NoTimeMuchine(x):
    if x > datetime(2000,1,1):
        temp_year = x.year - 100
        temp_month = x.month
        temp_day = x.day
        return parse(str(temp_year)+'/'+str(temp_month)+'/'+str(temp_day))
    
    else:
        return x

df['CorrectTime'] = df['times'].apply(NoTimeMuchine)

df

