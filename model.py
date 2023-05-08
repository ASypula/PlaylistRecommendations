from jsonLoader import *
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import re

tracks = getTracks()
artists = getArtists()

# Superstar
# Wannabe
# You and Me

tracks = pd.DataFrame.from_dict(tracks)
artists = pd.DataFrame.from_dict(artists)

def recommend_most_popular(col,col_value,top_n=5):
    return tracks[tracks[col]>=col_value].sort_values(by='popularity',ascending = False).head(top_n)[['name',col,'popularity']]

# print(recommend_most_popular('valence', 0.9))

mapping = pd.Series(tracks.index,index = tracks['name'])
# print(tracks)

tracks2 = tracks.copy()
tracks2.drop(labels=("id"), axis=1, inplace=True)
tracks2.drop(labels=("name"), axis=1, inplace=True)
# dodać dekodowanie release_date do datatime, bo niektóre utwory maja 2 wersje z różną datą

def applyDateParser(dateString):
    regs = r"[0-9]{4}-[0-9\-]*"
    if (re.match(regs, dateString)):
        return int(dateString[:4])
    else:
        return int(dateString)


def parseDates():
    tracks2['release_date'] = tracks2['release_date'].apply(applyDateParser)

def dropDates():
    tracks2.drop(labels=("release_date"), axis=1, inplace=True)


def dropArtists():
    tracks2.drop(labels=("id_artist"), axis=1, inplace=True)
    

def applyGenres(id_artist):
    # df.loc[df['column_name'] == some_value]
    genres = artists.loc[artists['id'] == id_artist]
    genres = genres.iloc[0]['genres']
    genres = ",".join(genres).lower()
    return genres

def countEncodeGenres(tracks2):
    tracks2.rename(columns= {"id_artist":"genres"}, inplace=True)
    tracks2["genres"] = tracks2["genres"].apply(applyGenres)
    vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','))
    X = vectorizer.fit_transform(tracks2['genres'])
    X.toarray()
    genrestags = vectorizer.get_feature_names_out()
    countVectorGenres = pd.DataFrame(X.toarray(),columns=genrestags)
    # print(countVectorGenres.head())

    tracks2.drop(labels=("genres"), axis=1, inplace=True)
    tracks2 = tracks2.join(countVectorGenres)

def oneHotArtists():
    one_hot_artist = pd.get_dummies(tracks2.id_artist, prefix="id_a", dtype=float)
    tracks2.drop(labels=("id_artist"), axis=1, inplace=True)
    tracks2 = tracks2.join(one_hot_artist)






parseDates()
countEncodeGenres(tracks2)
# dropArtists()
similarityMatrix = cosine_similarity(tracks2, tracks2)

def reccomend_similar(songName):
    songIndex = mapping[songName]
    similarityScore = list(enumerate(similarityMatrix[songIndex]))
    similarityScore = sorted(similarityScore, key=lambda x: x[1], reverse=True)
    similarityScore = similarityScore[1:15]
    indices = [i[0] for i in similarityScore]
    return (tracks['name'].iloc[indices])

print(reccomend_similar('Wannabe'))