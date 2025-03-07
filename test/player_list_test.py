import unittest

from app.player_list import PlayerList
from app.player import Player


class TestPlayerList(unittest.TestCase):
    def test_player_list_empty(self):
        test_player_list = PlayerList()
        self.assertEqual(test_player_list.is_empty(), True)

    def test_player_list(self):
        test_player_list = PlayerList()
        test_player_list.push(Player(unique_id=1, player_name="Player1"))
        test_player_list.push(Player(unique_id=2, player_name="Player2"))
        test_player_list.push(Player(unique_id=3, player_name="Player3"))
        self.assertEqual(len(test_player_list), 3)

    def test_player_list_head_and_tail(self):
        player_list = PlayerList()
        player_list.push(Player(unique_id=1, player_name="Player1"))
        player_list.push(Player(unique_id=2, player_name="Player2"))
        player_list.push(Player(unique_id=3, player_name="Player3"))
        self.assertEqual(player_list._head._player.name(), 'Player3')
        self.assertEqual(player_list._tail._player.name(), 'Player1')

    def test_player_list_push_tail(self):
        player_list = PlayerList()
        player_list.push(Player(unique_id=1, player_name="Player1"))
        player_list.push(Player(unique_id=2, player_name="Player2"))
        player_list.push(Player(unique_id=3, player_name="Player3"))
        player_list.push_tail(Player(unique_id=4, player_name="PlayerPUSH"))
        player_list.push(Player(unique_id=5, player_name="Player4"))
        self.assertEqual(player_list._tail._player.name(), 'PlayerPUSH')
        self.assertEqual(player_list._head._player.name(), 'Player4')

    def test_player_list_delete_head(self):
        player_list = PlayerList()
        player_list.push(Player(unique_id=1, player_name="Player1"))
        player_list.push(Player(unique_id=2, player_name="Player2"))
        player_list.push(Player(unique_id=3, player_name="Player3"))
        player_list.delete_head()
        self.assertEqual(player_list._head._player.name(), 'Player2')

    def test_player_list_delete_tail(self):
        player_list = PlayerList()
        player_list.push(Player(unique_id=1, player_name="Player1"))
        player_list.push(Player(unique_id=2, player_name="Player2"))
        player_list.push(Player(unique_id=3, player_name="Player3"))
        player_list.delete_tail()
        self.assertEqual(player_list._tail._player.name(), 'Player2')