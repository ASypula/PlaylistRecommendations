# import sys
# sys.path.append('./')
from model.jsonLoader import getArtists, getTracks
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import re


class Recommender:
    tracks =[]
    artists = []
    mapping = []
    tracks2 = []

    def __init__(self, searchPattern='id') -> None:
        self.sp = searchPattern

    def loadData(self):
        self.tracks = getTracks()
        self.artists = getArtists()
        self.tracks = pd.DataFrame.from_dict(self.tracks)
        self.artists = pd.DataFrame.from_dict(self.artists)
        self.mapping = pd.Series(self.tracks.index,index = self.tracks[self.sp])

    def initVector(self):
        self.tracks2 = self.tracks.copy()
        self.tracks2.drop(labels=("id"), axis=1, inplace=True)
        self.tracks2.drop(labels=("name"), axis=1, inplace=True)


    def recommend_most_popular(self,col,col_value,top_n=5):
        return self.tracks[self.tracks[col]>=col_value].sort_values(by='popularity',ascending = False).head(top_n)[['name',col,'popularity']]


    def dropRedundant(self):
        self.tracks2.drop(labels=("loudness"), axis=1, inplace=True)
        self.tracks2.drop(labels=("acousticness"), axis=1, inplace=True)
        self.tracks2.drop(labels=("valence"), axis=1, inplace=True)

    def applyDateParser(self,dateString):
        regs = r"[0-9]{4}-[0-9\-]*"
        if (re.match(regs, dateString)):
            return int(dateString[:4])
        else:
            return int(dateString)


    def parseDates(self):
        self.tracks2['release_date'] = self.tracks2['release_date'].apply(self.applyDateParser)

    def dropDates(self):
        self.tracks2.drop(labels=("release_date"), axis=1, inplace=True)


    def dropArtists(self):
        self.tracks2.drop(labels=("id_artist"), axis=1, inplace=True)
        

    def applyGenres(self,id_artist):
        # df.loc[df['column_name'] == some_value]
        genres = self.artists.loc[self.artists['id'] == id_artist]
        genres = genres.iloc[0]['genres']
        genres = ",".join(genres).lower()
        return genres

    def countEncodeGenres(self):
        self.tracks2.rename(columns= {"id_artist":"genres"}, inplace=True)
        self.tracks2["genres"] = self.tracks2["genres"].apply(self.applyGenres)
        vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','), token_pattern=None)
        X = vectorizer.fit_transform(self.tracks2['genres'])
        X.toarray()
        genrestags = vectorizer.get_feature_names_out()
        countVectorGenres = pd.DataFrame(X.toarray(),columns=genrestags)
        # print(countVectorGenres.head())

        self.tracks2.drop(labels=("genres"), axis=1, inplace=True)
        self.tracks2 = self.tracks2.join(countVectorGenres)

    def oneHotArtists(self):
        one_hot_artist = pd.get_dummies(self.tracks2.id_artist, prefix="id_a", dtype=float)
        self.tracks2.drop(labels=("id_artist"), axis=1, inplace=True)
        self.tracks2 = self.tracks2.join(one_hot_artist)

    def similarityMatrix(self):
        self.similarityMatrix = cosine_similarity(self.tracks2, self.tracks2)

    def recommend_similar(self,songName, nrofRecc=10):
        songIndex = self.mapping[songName]
        similarityScore = list(enumerate(self.similarityMatrix[songIndex]))
        similarityScore = sorted(similarityScore, key=lambda x: x[1], reverse=True)
        similarityScore = similarityScore[1:nrofRecc + 1]
        indices = [i[0] for i in similarityScore]
        return (self.tracks[self.sp].iloc[indices])

# r = Recommender()
# r.loadData()
# r.initVector()
# r.dropRedundant()
# r.parseDates()
# r.countEncodeGenres()
# # r.dropArtists()

# print(r.recommend_similar('You and Me'))