import pandas as pd

SONGS_TOTAL=20

def get_song_names(ids: list, file: str='./IUM_Zad_03_01_v4/tracks.jsonl') -> list:
    df_tracks = pd.read_json(file, lines=True)
    songs = []
    i=0
    while len(ids) > len(songs):
        if df_tracks.loc[i].at["id"] in ids:
            songs.append(df_tracks.loc[i].at["name"])
        i+=1
    return songs

def parse_data(data):
    try:
        users = data["users"]
        count = data.get("count", SONGS_TOTAL)
        if not isinstance(users, list):
            raise Exception("Incorrect parameters, a list of users should be provided.")
        return users, count
    except KeyError as e:
        msg = "Invalid request, field \"users\" is missing."
        #TODO: better error handling/displaying
        print(msg)
