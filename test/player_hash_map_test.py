import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_hash_map import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        """Setup before each test"""
        self.player_map = PlayerHashMap()
        self.player_map.put("player1", "Alice")
        self.player_map.put("player2", "Bob")
        self.player_map.put("player3", "Charlie")
        self.player_map.put("player4", "David")
        self.player_map.put("player5", "Eva")

    def test_get_index(self):
        """Test get_index method to ensure proper index calculation"""
        index_player1 = self.player_map.get_index("player1")
        index_player2 = self.player_map.get_index("player2")

        self.assertIsInstance(index_player1, int)
        self.assertIsInstance(index_player2, int)
        self.assertNotEqual(index_player1, index_player2)

    def test_put_new_player(self):
        """Test adding a new player"""
        self.player_map.put("player6", "Frank")
        index = self.player_map.get_index("player6")
        player_list = self.player_map.hash_map[index]

        player_found = False
        for player in player_list:
            if player.uid() == "player6" and player.name() == "Frank":
                player_found = True
                break
        self.assertTrue(player_found)

    def test_collision_handling(self):
        """Test handling of a hash collision (same index for two different players)"""
        self.player_map.put("player19", "Paul")

        index_player19 = self.player_map.get_index("player19")
        index_player3 = self.player_map.get_index("player3")
        self.assertEqual(index_player19, index_player3, "Collision not detected!")

        player_list = self.player_map.hash_map[index_player19]
        player_names = [player.name() for player in player_list]
        self.assertIn("Paul", player_names, "Player 19 not found!")
        self.assertIn("Charlie", player_names, "Player 3 not found!")