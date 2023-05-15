import itertools
import pandas as pd

def eval_matching_genre(user_genres: list, song_genres: list) -> int:
    # Evaluates if genres liked by given user match the genres in the song
    # For exactly same genre returns 1
    # For partially matching e.g. 'funk pop' and 'american pop' returns 0.5
    fully_matched =  set(user_genres).intersection(set(song_genres))
    if len(fully_matched) > 0:
        return 1
    user_parts = list(itertools.chain.from_iterable([x.split() for x in user_genres]))
    song_parts = list(itertools.chain.from_iterable([x.split() for x in song_genres]))
    partial_match = set(user_parts).intersection(set(song_parts))
    if len(partial_match) > 0:
        return 0.5
    else:
        return 0

def count_liked_genres_per_user(user_genres, songs_genres):
    user_sum = 0
    for song_genres in songs_genres:
        user_sum+=eval_matching_genre(user_genres, song_genres)
    return user_sum

def get_users_genres(user_ids, users_file='./IUM_Zad_03_01_v4/users.jsonl'):
    df_users = pd.read_json(users_file, lines=True)
    users_genres = []
    for user_id in user_ids:
        x = ((df_users.loc[df_users['user_id'] == user_id]).iloc[0])['favourite_genres']
        users_genres.append(x)
    return users_genres

def get_songs_genres(song_ids, songs_file='./IUM_Zad_03_01_v4/tracks.jsonl', artists_file='./IUM_Zad_03_01_v4/artists.jsonl'):
    df_songs = pd.read_json(songs_file, lines=True)
    df_artists = pd.read_json(artists_file, lines=True)
    songs_genres = []
    for song_id in song_ids:
        artist_id = ((df_songs.loc[df_songs['id'] == song_id]).iloc[0])['id_artist']
        x = ((df_artists.loc[df_artists['id'] == artist_id]).iloc[0])['genres']
        songs_genres.append(x)
    return songs_genres

def count_liked_genres(user_ids, song_ids):
    total = 0
    users_genres = get_users_genres(user_ids)
    songs_genres = get_songs_genres(song_ids)
    for u_genres in users_genres:
        total += count_liked_genres_per_user(u_genres, songs_genres)
    return total

# Test
# user_ids = [101, 104, 134]
# song_ids = ['4YjjNHtEsTX6Af4mCTupT5', '0F7FA14euOIX8KcbEturGH']
# print(count_liked_genres(user_ids, song_ids))
