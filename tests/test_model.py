import unittest
import sys
sys.path.append('./')
import random
from app.recommender import Model
from experiment.basic_model import BasicModel
from experiment.utils import count_liked_genres

class TestModel(unittest.TestCase):

    user_ids_range = (101, 3100)
    songs_nr = 20
    model_A = Model()
    model_B = BasicModel()

    @classmethod
    def setUpClass(cls):
        cls.model_A.loadData()
        cls.model_A.prepareModel()
        print("Starting all the tests.")

    def test_sum(self):
        user_count = 3
        seed = 1
        random.seed(seed)
        ids = random.sample(range(self.user_ids_range[0], self.user_ids_range[1]+1), user_count)
        playlist_gen = self.model_A.createPlaylist(ids)
        playlist_basic = self.model_B.get_random_songs(self.songs)
        print(playlist_gen)
        print(playlist_basic)

    def test_sum_tuple(self):
        self.assertEqual(sum((2, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()