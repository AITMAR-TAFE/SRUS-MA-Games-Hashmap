import unittest

from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def test_player_list_empty(self):
        test_player_list = PlayerList()
        self.assertEqual(test_player_list.is_empty(), True)

    def test_player_list(self):
        test_player_list = PlayerList([1,2,3])
        self.assertEqual(len(test_player_list),3)