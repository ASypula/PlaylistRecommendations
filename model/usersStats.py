from model.jsonLoader import getUsers, getSessions
import pandas as pd
import numpy as np

class UserStats:
    sessions = []
    def __init__(self, seed) -> None:
        np.random.seed(seed)

    def loadData(self):
        self.sessions = getSessions()
        self.sessions = pd.DataFrame.from_dict(self.sessions)

    def userTrackInteractions(self, user_id, track_id):
        return self.sessions.loc[(self.sessions['user_id'] == user_id) & (self.sessions['track_id'] == track_id), ['event_type']]

    def userLikedSongs(self, user_id, songs=10):
        liked = self.sessions.loc[(self.sessions['user_id'] == user_id) & (self.sessions['event_type'] == 'like'), ['track_id']]
        ll = len(liked.index)
        if ll < songs: songs = ll
        return liked.sample(songs)['track_id'].values.tolist()


    
# u = UserStats(42)
# u.loadData()
# # print(u.userTrackInteractions(101, "0qRR9d89hIS0MHRkQ0ejxX"))
# print(u.userLikedSongs(3100))
