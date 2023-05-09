from jsonLoader import getUsers, getSessions
import pandas as pd

class userStats:
    sessions = []

    def loadData(self):
        self.sessions = getSessions()
        self.sessions = pd.DataFrame.from_dict(self.sessions)

    def userTrackInteractions(self, user_id, track_id):
        return self.sessions.loc[(self.sessions['user_id'] == user_id) & (self.sessions['track_id'] == track_id), ['event_type']]
    
u = userStats()
u.loadData()
print(u.userTrackInteractions(101, "0qRR9d89hIS0MHRkQ0ejxX"))
