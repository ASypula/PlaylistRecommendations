from app.model import Recommender
from app.usersStats import UserStats
import random
from itertools import zip_longest

SONG_NR=20

class Model:
    def __init__(self) -> None:
        self.r = Recommender()
        self.us = UserStats(42)
        self.loadData()
        self.pl = 20

    def loadData(self):
        self.r.loadData()
        self.us.loadData()

    def prepareModel(self):
        self.r.initVector()
        self.r.dropRedundant()
        self.r.parseDates()
        self.r.dropArtists()
        self.r.computeSimiliarityMatrix()


    def createPlaylist(self, users: list):
        nrofUsers = len(users)
        if nrofUsers < 3 or nrofUsers > 10:
            return []
        random.shuffle(users)
        favourites = [self.us.userLikedSongs(u, 1)[0] for u in users]
        recommended = [self.r.reccomend_similar(s) for s in favourites]
        rec = zip_longest(*recommended, fillvalue="?")
        rec = list(rec)
        rec = [num for sub in rec for num in sub]
        rec = list(filter(("?").__ne__, rec))

        playlist = favourites + rec
        # playlist[:SONG_NR]
        return playlist[:SONG_NR]

if __name__ == "__main__":
    user_ids = [101, 310, 309]
    rec = Model()
    rec.loadData()
    print("loaded")
    print(rec.createPlaylist(user_ids))
