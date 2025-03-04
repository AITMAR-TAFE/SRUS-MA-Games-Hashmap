import unittest

from app.player_list import PlayerList
from app.player import Player

class TestPlayerList(unittest.TestCase):
    def test_player_list_empty(self):
        test_player_list = PlayerList()
        self.assertEqual(test_player_list.is_empty(), True)

    def test_player_list(self):
        test_player_list = PlayerList([1,2,3])
        self.assertEqual(len(test_player_list),3)

    def test_player_list_head_and_tail(self):
        player_list = PlayerList()
        player_list.push('Player1')
        player_list.push('Player2')
        player_list.push('Player3')
        self.assertEqual(player_list._head._player, 'Player3')
        self.assertEqual(player_list._tail._player, 'Player1')
