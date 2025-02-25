import unittest

from app.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player = Player("TestPlayerID","TestPlayerName")

    def test_player_name(self):
        self.assertEqual(self.test_player.name(), "TestPlayerName")

    def test_player_unique_id(self):
        self.assertEqual(self.test_player.uid(), "TestPlayerID")

