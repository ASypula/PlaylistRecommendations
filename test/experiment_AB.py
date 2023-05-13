from recommender import get_playlist
from basic_model import get_random_playlist
from utils import count_liked_genres

def run():
    user_ids = [101, 103, 106]
    count = 20
    playlist_gen = get_playlist(user_ids)
    playlist_random = get_random_playlist(20)
    score_gen = count_liked_genres(user_ids, playlist_gen)
    score_random = count_liked_genres(user_ids, playlist_random)
