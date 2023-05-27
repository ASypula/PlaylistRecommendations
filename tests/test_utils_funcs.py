import unittest
import sys
sys.path.append('./')
import random
from app.utils import get_song_names, parse_data
from experiment.utils import get_users_genres

class TestModel(unittest.TestCase):

    user_ids_range = (101, 3100)
    songs = 20

    def test_song_names_2(self):
        song_ids = ['1CgmY8fVN7kstVDZmsdM5k', '0Yld4eVEV6rBvpijVU2s6l']
        song_names = get_song_names(song_ids)
        expected_songs = ['P.Y.T. (Pretty Young Thing)', 'Naina']
        self.assertListEqual(expected_songs, song_names)

    def test_song_names_20(self):
        song_ids = ['0bSZTzZALj8fVdpKvP6xiG', '2ehkJlAysINP3czoqaklyT', '6YffUZJ2R06kyxyK6onezL', '2ggqfj97qyiORmXoVFzP5j', '6M0IsaUX4GNyto4niSegfI', '3jPGemJdr95abo520vyvVk', '2jxfsaODfcVQhKMZPuYK2j', '6DyywdbmTzlmXBzG9ym7Rt', '3B5UbSndRz907IZhhmUfLi', '4sUlsy0tPv9n5nqrqeA0lE', '40h65HAR8COEoqkMwUUQHu', '3UDmHZcBTQp8Iu8droNtUl', '694vvR5o19xHPhhJ5QdLN7', '77o1HdXHm1hLd7Ebe9ygd0', '3NcJu9876GBJuNU6vJOrbb', '6BnRwKaF2bRuA3bbrPjBJg', '7Ie9W94M7OjPoZVV216Xus', '7J4ldEKgygxQrKo0y9msdH', '0w7lKfhxW190u1ckXi45E9', '6C88rHxXBlpcgtBY3HAF0E']
        song_names = get_song_names(song_ids)
        expected_songs = ['Ring of Fire', 'I Want a Little Sugar In My Bowl', 'Peaceful Easy Feeling - 2013 Remaster', 'Revolution - Remastered 2009', 'Brighton Rock - Remastered 2011', 'Magic Man', 'Sober', 'Not Afraid', 'Le Onde', 'No Option', 'Count on Me', 'Sin Saber Por Qué', 'Esta Noche', 'No Te Vayas', 'Andromeda', 'Paris', 'THAT BITCH', 'Quem Pegou, Pegou - Ao Vivo', 'Rain', 'NO HALO']
        self.assertListEqual(expected_songs, song_names)

    def test_get_users_genres1(self):
        user_ids = [101]
        genres = get_users_genres(user_ids)
        expected_genres = [['dance pop', 'latin', 'hard rock']]
        self.assertListEqual(expected_genres, genres)

    def test_get_users_genres3(self):
        user_ids = [101, 102, 103]
        genres = get_users_genres(user_ids)
        expected_genres = [['dance pop', 'latin', 'hard rock'], ['reggaeton', 'latin arena pop', 'modern rock'], ['rap', 'art rock', 'rock']]
        self.assertListEqual(expected_genres, genres)

    def test_random_ids(self):
        user_count = 8
        random.seed(1)
        ids = random.sample(range(self.user_ids_range[0], self.user_ids_range[1]+1), user_count)
        expected_ids = [651, 2432, 359, 1145, 583, 2130, 1942, 2035]
        self.assertListEqual(expected_ids, ids)

    def test_parse_data(self):
        expected_users = [1, 2, 3]
        response = {"users": expected_users, "count": 20}
        users = parse_data(response)
        self.assertEqual(expected_users, users)

if __name__ == '__main__':
    unittest.main()