import pandas as pd
import random

random.seed(10)

class BasicModel:

    tracks_file = './IUM_Zad_03_01_v4/tracks.jsonl'

    def get_random_songs(self, nr: int) -> list:
        df_tracks = pd.read_json(self.tracks_file, lines=True)
        songs = []
        # generates a list of random integers without duplicates
        random_ids = random.sample(range(df_tracks.shape[0]), nr)
        for i in random_ids:
            songs.append(df_tracks.loc[i].at['id'])
        return songs

def get_random_playlist(nr):
    model = BasicModel()
    return model.get_random_songs(nr)