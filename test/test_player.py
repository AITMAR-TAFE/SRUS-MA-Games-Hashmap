from app.player import Player
import unittest


class TestPlayer(unittest.TestCase):
    def test_sort_players(self):
        players = [Player(unique_id='01',player_name="Alice", player_score=10), Player(unique_id='02',player_name = "Bob", player_score=5), Player(unique_id='03',player_name = "Charlie", player_score=15)]
        # note: ensure initialization code is valid for **your** implementation

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(unique_id='02', player_name="Bob", player_score=5), Player(unique_id='01', player_name="Alice", player_score=10), Player(unique_id='03', player_name="Charlie", player_score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)