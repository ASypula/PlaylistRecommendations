import sys
sys.path.append('./')
import random
from app.recommender import Model
from basic_model import BasicModel
from utils import count_liked_genres

#random.seed(1)
SONGS = 20

def generate_playlist_results(model_gen, model_basic, user_ids):
    playlist_gen = model_gen.createPlaylist(user_ids)
    playlist_basic = model_basic.get_random_songs(SONGS)
    count_gen = count_liked_genres(user_ids, playlist_gen)
    count_basic = count_liked_genres(user_ids, playlist_basic)
    return count_gen, count_basic

def run(nr_tests=2, users_count=[3]):
    # nr_tests - number of tests to take for each given nr of users
    # users_count - list with the numbers of users for playlist on each iteration e.g. [3, 6, 9]
    user_ids_range = (101, 3100)
    results_gen, results_basic = [], []
    model_A = Model()
    model_A.loadData()
    model_A.prepareModel()
    model_B = BasicModel()
    for nr in users_count:
        for _ in range(nr_tests):
            random_ids = random.sample(range(user_ids_range[0], user_ids_range[1]+1), nr)
            result_A, result_B = generate_playlist_results(model_A, model_B, random_ids)
            result_A = result_A/nr/SONGS
            result_B = result_B/nr/SONGS
            results_gen.append(result_A)
            results_basic.append(result_B)
    return (results_gen, results_basic)

def experiment_AB():
    results_gen, results_basic = run()
    with open("test_results.txt", '+a') as f:
        f.write(f"Results from model: {results_gen}")
        f.write(f"Results from random: {results_basic}")

if __name__=="__main__":
    experiment_AB()