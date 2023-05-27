import sys
sys.path.append('./')
import random
from app.recommender import Model
from basic_model import BasicModel
from utils import count_liked_genres
import logging

logger = logging.Logger(__name__)

SONGS = 20

def generate_playlist_results(model_gen, model_basic, user_ids):
    playlist_gen = model_gen.createPlaylist(user_ids)
    logger.debug(f"Songs ids from model playlist: {playlist_gen}")
    playlist_basic = model_basic.get_random_songs(SONGS)
    logger.debug(f"Songs ids from random playlist: {playlist_basic}")
    count_gen = count_liked_genres(user_ids, playlist_gen)
    count_basic = count_liked_genres(user_ids, playlist_basic)
    return count_gen, count_basic

def run(nr_tests, users_count):
    # nr_tests - number of tests to take for each given nr of users
    # users_count - list with the numbers of users for playlist on each iteration e.g. [3, 6, 9]
    user_ids_range = (101, 3100)
    results_gen, results_basic = [], []
    model_A = Model()
    model_A.loadData()
    model_A.prepareModel()
    model_B = BasicModel()
    for nr in users_count:
        for i in range(nr_tests):
            logger.info(f"Starting test nr {i} for {nr} users")
            random_ids = random.sample(range(user_ids_range[0], user_ids_range[1]+1), nr)
            logger.info(f"Chosen user ids for the test: {random_ids}")
            result_A, result_B = generate_playlist_results(model_A, model_B, random_ids)
            result_A = result_A/nr/SONGS
            result_B = result_B/nr/SONGS
            logger.info(f"Result for custom model in {i} iteration {nr} users {result_A}")
            logger.info(f"Result for random model in {i} iteration {nr} users {result_B}")
            results_gen.append(result_A)
            results_basic.append(result_B)
    return (results_gen, results_basic)

def experiment_AB(nr_tests=20, users_count=[3, 6, 9]):
    filename = "test_results.txt"
    results_gen, results_basic = run(nr_tests, users_count)
    logger.info(f"Experiment finished, saving results to file: {filename}")
    with open(filename, '+a') as f:
        f.write(f"Results from model: {results_gen}")
        f.write(f"Results from random: {results_basic}")
    logger.info("Results saved")

if __name__=="__main__":
    if len(sys.argv) > 2:
        nr_tests = int(sys.argv[1])
        users_count = [int(x) for x in sys.argv[2:]]
        experiment_AB(nr_tests, users_count)
    else:
        experiment_AB()
