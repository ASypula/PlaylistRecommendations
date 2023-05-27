import unittest
import sys
sys.path.append('./')
import random
from app.recommender import Model
from experiment.basic_model import BasicModel

class TestModel(unittest.TestCase):

    user_ids_range = (101, 3100)
    songs = 20
    model_A = Model()
    model_B = BasicModel()

    @classmethod
    def setUpClass(cls):
        cls.model_A.loadData()
        cls.model_A.prepareModel()

    def test_3_users_seed1(self):
        user_count = 3
        seed = 1
        random.seed(seed)
        ids = random.sample(range(self.user_ids_range[0], self.user_ids_range[1]+1), user_count)
        expected_model_playlist = ['3t5WtBD4OweaMvlPlN1Czv', '4tGqkpkHNxSovRoJrajH4n', '2nO1DYEg1X5GHi8SSuNJQj', '4sVqufkRucC6hzUBzxKmdd', '01CYr3t0hedD915PmI5l4D', '41Az1BCotlAUt7Ud8k6H2Y', '0wJtvjLu9S7FJoCrtwMmS4', '6F5RvdxWcLOJW7LAGuc24r', '208bYsadJ56km31IENM2qS', '42HaJ7QlInzQ5vHKWb5Ixa', '51LmI5GE3tHKISLNZMjDPC', '7rbWpbXVwY2DFrZpWYPtVj', '7xrwGUa11hnnxXWeTIzcHf', '3JjZq20Kv6UphyyirAaY9A', '6nxQdXa1uAL0rY72wPZu89', '2SCyoYh5CgyJyCvpve3AVQ', '14LtANuaslKWyYbktUrHBU', '4LZqNiZHiQvGLlt0RkXtqt', '2Aon31CR3MV3Kt3vczK9Xf', '2cm5JHPVzXyrWPtIZZi1Gh']
        expected_basic_playlist = ['3FK0U3qJYP3E24Vx5QSBWz', '3kZADzbBCSKzWyjKDwOIEb', '54suAFhsGjOKBhrUedu0pm', '4bLfRfX6fSvMDaLEFnMvB4', '5BAmltzhQpFXtBddPN4sUf', '3Pzh926pXggbMe2ZpXyMV7', '2UqzzArv2T0NnHSTIUa13V', '17rf2oZYDVymJeYI9ftDXc', '5v1osKVFv3rXWb1VJDO9pW', '7D93pJcwymzaZx8WgBo2zG', '0bSZTzZALj8fVdpKvP6xiG', '2ehkJlAysINP3czoqaklyT', '6YffUZJ2R06kyxyK6onezL', '2ggqfj97qyiORmXoVFzP5j', '6M0IsaUX4GNyto4niSegfI', '3jPGemJdr95abo520vyvVk', '2jxfsaODfcVQhKMZPuYK2j', '6DyywdbmTzlmXBzG9ym7Rt', '3B5UbSndRz907IZhhmUfLi', '4sUlsy0tPv9n5nqrqeA0lE']
        playlist_gen = self.model_A.createPlaylist(ids)
        playlist_basic = self.model_B.get_random_songs(self.songs)
        self.assertEqual(len(playlist_gen), 20)
        self.assertListEqual(expected_model_playlist, playlist_gen)
        self.assertListEqual(expected_basic_playlist, playlist_basic)

    def test_3_users_seed2(self):
        user_count = 3
        seed = 2
        random.seed(seed)
        ids = random.sample(range(self.user_ids_range[0], self.user_ids_range[1]+1), user_count)
        expected_model_playlist = ['79s5XnCN4TJKTVMSmOx8Ep', '064NEtcV4JQqGxAtfqvRfI', '2LMloFiV7DHpBhITOaBSam', '4yugZvBYaoREkJKtbG08Qr', '67D9O4Oau629qirRXtTWCS', '0OM9ri37LIbPc9hffwsyb1', '1yjY7rpaAQvKwpdUliHx0d', '1CgmY8fVN7kstVDZmsdM5k', '0Yld4eVEV6rBvpijVU2s6l', '5TU6HG6Ltm7ZYr3r5dZjsA', '5zGJT3TTShcNHeJeDrjPvs', '1gzXHWAGYKbaHubERNp0Ox', '0AUyNF6iFxMNQsNx2nhtrw', '3OS4XXm4S42pnESQmtN9MG', '2xeVMreitVgtGQvEL5KD9s', '0utlOiJy2weVl9WTkcEWHy', '4fzyvSu73BhGvi96p2zwjL', '4Htt3QaBWdLggq88rJI5MU', '0hyImI8JaWONOrzKH7kJsC', '0KXpgyL7L8xIpotzpWoUOo']
        expected_basic_playlist = ['1Jw8h20nLaqTxIAznSbxfS', '3rn07BEDuQLxbpKsStMido', '4lrC9aBnzlG9U5DDoHMnyt', '7FCdJdGEOBCHqZAYRoZAWV', '38EI0NudWZT1qFuhEafIHh', '0DrFTaAX2srXPkuag35djb', '5Ale7Htu2SdvOcBwlEdGhZ', '3vLH6polscUOyQuZB9VjCC', '1XjHRolIXL2M1EEOUsGGR4', '2agBDIr9MYDUducQPC1sFU', '3LCEPpWeFpp6EONBsL2qbk', '2zWxPpMXAY4RTxxFnU3Vx7', '417MeJ40upxxf3aNlr5Xbi', '1Slwb6dOYkBlWal1PGtnNg', '5PdymUcagmspn9bSXYDHoi', '1CyKvPk8UOj3kvc0KRVDZn', '3FrQ1OJwWcusCyP5NS2bnD', '1EKiQ1InQXuodp4M1idrng', '1BwBeG8Pae6uHp3w29AHvi', '2cYAd7BJIOj4Y0pU5Pyesc']
        playlist_gen = self.model_A.createPlaylist(ids)
        playlist_basic = self.model_B.get_random_songs(self.songs)
        self.assertEqual(len(playlist_gen), 20)
        self.assertListEqual(expected_model_playlist, playlist_gen)
        self.assertListEqual(expected_basic_playlist, playlist_basic)

    def test_5_users_seed1(self):
        user_count = 5
        seed = 1
        random.seed(seed)
        ids = random.sample(range(self.user_ids_range[0], self.user_ids_range[1]+1), user_count)
        expected_model_playlist = ['6FKU84JHM1lbiy5Dx0Dyqd', '0Ky9DFq4xtsIZQiI0d2fnG', '78YknDXAOrz0E9ves11vnK', '19W5OTEcQI3ZoRW1HERMyy', '3JfHYZKy5JmE5Fv4gDTCiz', '3NgCzSW98SsqBdpYcnm4kv', '5OFi9CIyD6s1oENyHapK2W', '5ZqNz8GXWpkb95f7aVxTA0', '5Aa33rAPkp7f7l1aVqsHO8', '5QTdOvIF2ehBMZpSIIGzIo', '3ljr9ATeLs2BY9gNp7vm62', '7ytES33eLYS9WaZLKqWfYM', '18LgeYUnaMuirDr0Ljz1pL', '3o8QzWsiiqTUVgBZfHgF58', '5Fim1gaXBgsiFfsQAfQSDS', '1clTca5X3tpBjNgfpsd3wu', '1BMhbPsW66IXqksKC8jrCf', '3fZQ34JaZ1DPbB3U9CUnlg', '1MKZaAEx8RrzoQjHhVuvgs', '1hqrYSqvNc9x3BETX1cZhk']
        expected_basic_playlist = ['3Pzh926pXggbMe2ZpXyMV7', '2UqzzArv2T0NnHSTIUa13V', '17rf2oZYDVymJeYI9ftDXc', '5v1osKVFv3rXWb1VJDO9pW', '7D93pJcwymzaZx8WgBo2zG', '0bSZTzZALj8fVdpKvP6xiG', '2ehkJlAysINP3czoqaklyT', '6YffUZJ2R06kyxyK6onezL', '2ggqfj97qyiORmXoVFzP5j', '6M0IsaUX4GNyto4niSegfI', '3jPGemJdr95abo520vyvVk', '2jxfsaODfcVQhKMZPuYK2j', '6DyywdbmTzlmXBzG9ym7Rt', '3B5UbSndRz907IZhhmUfLi', '4sUlsy0tPv9n5nqrqeA0lE', '40h65HAR8COEoqkMwUUQHu', '3UDmHZcBTQp8Iu8droNtUl', '694vvR5o19xHPhhJ5QdLN7', '77o1HdXHm1hLd7Ebe9ygd0', '3NcJu9876GBJuNU6vJOrbb']
        playlist_gen = self.model_A.createPlaylist(ids)
        playlist_basic = self.model_B.get_random_songs(self.songs)
        self.assertEqual(len(playlist_gen), 20)
        self.assertListEqual(expected_model_playlist, playlist_gen)
        self.assertListEqual(expected_basic_playlist, playlist_basic)

    def test_5_users_seed2(self):
        user_count = 5
        seed = 2
        random.seed(seed)
        ids = random.sample(range(self.user_ids_range[0], self.user_ids_range[1]+1), user_count)
        expected_model_playlist = ['7mjSHL2Eb0kAwiKbvNNyD9', '0RCpze7hmowZIGUJs9Dm7w', '2QhURnm7mQDxBb5jWkbDug', '6dJ2mSRaKE9ctYw9qWNGWQ', '2GiJYvgVaD2HtM8GqD9EgQ', '00Mb3DuaIH1kjrwOku9CGU', '0ESIjVxnDnCDaTPo6sStHm', '1QjsRvdLEvUmKgCWh9cvd5', '3q3hLt6ACOJg0hvA5lYmj5', '0GO8y8jQk1PkHzS31d699N', '6mADjHs6FXdroPzEGW6KVJ', '52BJrldggFQyTiW8XrILhO', '4255amV4enzl28KAn16rUO', '4Ai0ANRDYwx6mCD4Uty1WS', '5vdp5UmvTsnMEMESIF2Ym7', '3h3pOvw6hjOvZxRUseB7h9', '3bWGaqVeYKMlLss40mPgNn', '2glGP8kEfACgJdZ86kWxhN', '2d5vz9uU5Jan1rX8mkxw2w', '76hfruVvmfQbw0eYn1nmeC']
        expected_basic_playlist = ['0DrFTaAX2srXPkuag35djb', '5Ale7Htu2SdvOcBwlEdGhZ', '3vLH6polscUOyQuZB9VjCC', '1XjHRolIXL2M1EEOUsGGR4', '2agBDIr9MYDUducQPC1sFU', '3LCEPpWeFpp6EONBsL2qbk', '2zWxPpMXAY4RTxxFnU3Vx7', '417MeJ40upxxf3aNlr5Xbi', '1Slwb6dOYkBlWal1PGtnNg', '5PdymUcagmspn9bSXYDHoi', '1CyKvPk8UOj3kvc0KRVDZn', '3FrQ1OJwWcusCyP5NS2bnD', '1EKiQ1InQXuodp4M1idrng', '1BwBeG8Pae6uHp3w29AHvi', '2cYAd7BJIOj4Y0pU5Pyesc', '2SpEHTbUuebeLkgs9QB7Ue', '5bQ9rtAfOUbPmuxjPK8zDp', '4FyhUbVIVFEEOHfdTiFmbf', '7Lwj4BttdzmwGIL5pigaMV', '6IqbQelrOB6nTORNj4q2Ma']
        playlist_gen = self.model_A.createPlaylist(ids)
        playlist_basic = self.model_B.get_random_songs(self.songs)
        self.assertEqual(len(playlist_gen), 20)
        self.assertListEqual(expected_model_playlist, playlist_gen)
        self.assertListEqual(expected_basic_playlist, playlist_basic)

    def test_8_users_seed1(self):
        user_count = 8
        seed = 1
        random.seed(seed)
        ids = random.sample(range(self.user_ids_range[0], self.user_ids_range[1]+1), user_count)
        expected_model_playlist = ['2oENJa1T33GJ0w8dC167G4', '2ythurkTtSiyfK7GprJoFW', '5WfSHn8qVk1W3GJJQpETC1', '4uQ7wYsuL0DryknoDc11Hk', '0cKk8BKEi7zXbdrYdyqBP5', '5KV9bNW1Ta4Z4PdHgu84TA', '0jllH0usRFD4LJkJnGK9Lf', '61KpQadow081I2AsbeLcsb', '13MF2TYuyfITClL1R2ei6e', '7pamxApUs3CE8t7tKmUJ6Z', '46h7yzNgZQNuyn5BwBHQeS', '1ibeKVCiXORhvUpMmtsQWq', '4ve2uzqdwnHr20G5YgMMqr', '0M1pfDTZGWC7cBuEx3FwwT', '3MkdA6vwF0ifRl86yzTlJW', '0NWPxcsf5vdjdiFUI8NgkP', '3skn2lauGk7Dx6bVIt5DVj', '2juRA8DhQePry4eb2LMUMM', '0ZFqB9g2FujbmMSrjqsL3j', '0EJu1RBtxzldMG2peczuPv']
        expected_basic_playlist = ['0bSZTzZALj8fVdpKvP6xiG', '2ehkJlAysINP3czoqaklyT', '6YffUZJ2R06kyxyK6onezL', '2ggqfj97qyiORmXoVFzP5j', '6M0IsaUX4GNyto4niSegfI', '3jPGemJdr95abo520vyvVk', '2jxfsaODfcVQhKMZPuYK2j', '6DyywdbmTzlmXBzG9ym7Rt', '3B5UbSndRz907IZhhmUfLi', '4sUlsy0tPv9n5nqrqeA0lE', '40h65HAR8COEoqkMwUUQHu', '3UDmHZcBTQp8Iu8droNtUl', '694vvR5o19xHPhhJ5QdLN7', '77o1HdXHm1hLd7Ebe9ygd0', '3NcJu9876GBJuNU6vJOrbb', '6BnRwKaF2bRuA3bbrPjBJg', '7Ie9W94M7OjPoZVV216Xus', '7J4ldEKgygxQrKo0y9msdH', '0w7lKfhxW190u1ckXi45E9', '6C88rHxXBlpcgtBY3HAF0E']
        playlist_gen = self.model_A.createPlaylist(ids)
        playlist_basic = self.model_B.get_random_songs(self.songs)
        self.assertEqual(len(playlist_gen), 20)
        self.assertListEqual(expected_model_playlist, playlist_gen)
        self.assertListEqual(expected_basic_playlist, playlist_basic)

    def test_8_users_seed2(self):
        user_count = 8
        seed = 2
        random.seed(seed)
        ids = random.sample(range(self.user_ids_range[0], self.user_ids_range[1]+1), user_count)
        expected_model_playlist = ['67WTwafOMgegV6ABnBQxcE', '696DnlkuDOXcMAnKlTgXXK', '3ZuVfQriS93y6ofwbIf7lp', '0IGXkVRn0uCsgn4FvIfpgB', '6DjKJgwe9c90Bd2iya0fre', '0xsvATseavMaJjO13iHTkF', '4sUoWHVnJl8z3t4zdqf6xB', '4mCf3vQf7z0Yseo0RxAi3V', '6t6oULCRS6hnI7rm0h5gwl', '7GLWWrk1YlkPYqJK3ynIA0', '0GrHWVTDsaWcD4nrCGr7VE', '6nswV1Lz3OZkaiCJfmVUOa', '32bJv8V2Xgi5mtxdPcsi8B', '1HjENSMpxb14fBU27GrAKu', '4tkSJRlbhuVxYjvuIQaMcj', '2BgEsaKNfHUdlh97KmvFyo', '11EX5yhxr9Ihl3IN1asrfK', '2LawezPeJhN4AWuSB0GtAU', '3AgY5gLURlcdYBVGv1RVm7', '7aULhZT2q6ckDPPwUvgfFg']
        expected_basic_playlist = ['1Slwb6dOYkBlWal1PGtnNg', '5PdymUcagmspn9bSXYDHoi', '1CyKvPk8UOj3kvc0KRVDZn', '3FrQ1OJwWcusCyP5NS2bnD', '1EKiQ1InQXuodp4M1idrng', '1BwBeG8Pae6uHp3w29AHvi', '2cYAd7BJIOj4Y0pU5Pyesc', '2SpEHTbUuebeLkgs9QB7Ue', '5bQ9rtAfOUbPmuxjPK8zDp', '4FyhUbVIVFEEOHfdTiFmbf', '7Lwj4BttdzmwGIL5pigaMV', '6IqbQelrOB6nTORNj4q2Ma', '3sjxyR6C8OjKPnGYpsthzH', '7BfIsls4rRVAUhj16hHgM9', '6BL4PpswVjH9BAajbIbpmZ', '6Ahg1hncxUdK0ICqU03BCu', '003vvx7Niy0yvhvHt4a68B', '5pyVqlqThcxI7tPDjHIzPh', '0LtOwyZoSNZKJWHqjzADpW', '4Zy3y23RJDQEohBZFu94v1']
        playlist_gen = self.model_A.createPlaylist(ids)
        playlist_basic = self.model_B.get_random_songs(self.songs)
        self.assertEqual(len(playlist_gen), 20)
        self.assertListEqual(expected_model_playlist, playlist_gen)
        self.assertListEqual(expected_basic_playlist, playlist_basic)

if __name__ == '__main__':
    unittest.main()