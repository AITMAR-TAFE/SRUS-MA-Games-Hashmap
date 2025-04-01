from app.player import Player
import random
import unittest


class TestPlayer(unittest.TestCase):
    def test_sort_players(self):
        players = [Player(unique_id='01',player_name="Alice", player_score=10), Player(unique_id='02',player_name="Bob", player_score=5), Player(unique_id='03',player_name = "Charlie", player_score=15)]
        # note: ensure initialization code is valid for **your** implementation

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(unique_id='02', player_name="Bob", player_score=5), Player(unique_id='01', player_name="Alice", player_score=10), Player(unique_id='03', player_name="Charlie", player_score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(unique_id='01',player_name="Alice", player_score=10)
        bob = Player(unique_id='02',player_name = "Bob", player_score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice > bob)

    def test_players_custom_sorting_algorithm(self):
        players = [Player(unique_id='01',player_name="Alice", player_score=10), Player(unique_id='02',player_name="Bob", player_score=5), Player(unique_id='03',player_name = "Charlie", player_score=15)]

        sorted_players = Player.sort(players)

        manually_sorted_players = [Player(unique_id='03', player_name="Charlie", player_score=15), Player(unique_id='01', player_name="Alice", player_score=10), Player(unique_id='02', player_name="Bob", player_score=5)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_custom_sorting_algorithm_at_scale(self):
        players = [Player(unique_id=f"{i:03}", player_name=f"Test player {i}", player_score=random.randint(0,1000)) for i in range(1000)]

        sorted_players = Player.sort(players)

        sorted_players_default = sorted(players, reverse=True)
        self.assertListEqual(sorted_players, sorted_players_default)

    def test_sorting_sorted_players(self):
        players = [Player(unique_id=f"{i:03}", player_name=f"Test player {i}", player_score=i) for i in range(1000, 0, -1)]

        sorted_players = Player.sort(players)

        self.assertListEqual(players, sorted_players)