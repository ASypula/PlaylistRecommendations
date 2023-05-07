from jsonLoader import *
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

tracks = getTracks()

# Superstar
# Wannabe
# You and Me

df = pd.DataFrame.from_dict(tracks)
# print(df)

df2 = df.copy()
df2.drop(labels=("id"), axis=1, inplace=True)
df2.drop(labels=("name"), axis=1, inplace=True)
# df2.drop(labels=("id_artist"), axis=1, inplace=True)
df2.drop(labels=("release_date"), axis=1, inplace=True)
# dodać dekodowanie release_date do datatime, bo niektóre utwory maja 2 wersje z różną datą

one_hot_artist = pd.get_dummies(df2.id_artist, prefix="id_a")
df2.drop(labels=("id_artist"), axis=1, inplace=True)
df2 = df2.join(one_hot_artist)
# zamienić na one hot tagów


# print(df2.columns)

def recommend_most_popular(col,col_value,top_n=5):
    return df[df[col]>=col_value].sort_values(by='popularity',ascending = False).head(top_n)[['name',col,'popularity']]

# print(recommend_most_popular('valence', 0.9))


mapping = pd.Series(df.index,index = df['name'])
similarityMatrix = cosine_similarity(df2, df2)

def reccomend_similar(songName):
    songIndex = mapping[songName]
    similarityScore = list(enumerate(similarityMatrix[songIndex]))
    similarityScore = sorted(similarityScore, key=lambda x: x[1], reverse=True)
    similarityScore = similarityScore[1:15]
    indices = [i[0] for i in similarityScore]
    return (df['name'].iloc[indices])

print(reccomend_similar('Wannabe'))