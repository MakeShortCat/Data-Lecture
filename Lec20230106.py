import seaborn as sns
import pandas as pd
import numpy as np

titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived': 'age']
df

df = pd.read_excel('C:/Users/pgs66/Desktop/주가데이터.xlsx')

df['연월일'] = df['연월일'].astype('str')
dates =df['연월일'].str.split('-')
print(dates.head())

df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)

movies = pd.read_table('C:/Users/pgs66/Desktop/movies.txt', sep='::',header=None,
                    names=['movie_id', 'title', 'genres'], encoding = "ISO-8859-1")

all_genres = []

df1['genres']  = df1['genres'].str.split('|')

for i in df1['genres']:
    all_genres.extend(i.split('|'))

df1['genres'] = all_genres
    
(df1['genres'])

genres = pd.unique(all_genres)


zero_metrix = np.zeros((len(df1['genres']), len(genres)))

zero_metrix

df_movies = pd.DataFrame(zero_metrix, columns=genres)

df_movies.columns.get_indexer(movies.genres.str.split('|')[3])

for i, gen in enumerate(movies.genres):
    print(i, gen)
    
df_movies.iloc[3823, [2,9]]

for i, gen in enumerate(movies.genres):
    df_movies.iloc[i, df_movies.columns.get_indexer(gen.split('|'))] = 1
    
    
    