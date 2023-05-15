from model.model import Recommender
from model.usersStats import UserStats
import random
from itertools import zip_longest

class Model:
    def __init__(self) -> None:
        self.r = Recommender()
        self.us = UserStats(42)
        self.loadData()
        random.seed(42)
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
        print("got favourites")
        recommended = [self.r.reccomend_similar(s) for s in favourites]
        # print(recommended)
        rec = zip_longest(*recommended, fillvalue="?")
        rec = list(rec)
        # print(rec)
        rec = [num for sub in rec for num in sub]
        # print(rec)
        rec = list(filter(("?").__ne__, rec))
        # print(rec)

        playlist = favourites + rec
        playlist[:20]
        return playlist

        
# rec = Model()
# rec.loadData()
# print("loaded")
# rec.prepareModel()
# print("prepared")
# print(rec.createPlaylist([101, 3100, 3092] ))


if __name__ == "__main__":
    user_ids = [101, 3100, 3092]
    rec = Model()
    rec.loadData()
    print("loaded")
    print(rec.createPlaylist(user_ids))
