import unittest
from io import StringIO
import sys

from app.player_list import PlayerList
from app.player import Player


class Capturing(list):
    """
    Context manager to capture printed output during tests.
    Reference https://gist.github.com/russhughes/5afb0dca6e6b73d5c10d707334b06615
    """
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()
        self._current_string = sys.stdout
        return self

    def __exit__(self, *args):
        self.extend(self._current_string.getvalue().splitlines())
        del self._current_string
        sys.stdout = self._stdout


class TestPlayerList(unittest.TestCase):

    def setUp(self):
        """Set up a test player list with sample players."""
        self.player_list = PlayerList()
        players = [
            Player("player1", "Alice"),
            Player("player2", "Bob"),
            Player("player3", "Charlie"),
            Player("player4", "David"),
            Player("player5", "Eva")
        ]
        for player in players:
            self.player_list.push(player)

    def test_player_list_empty(self):
        """Test if a new list is empty."""
        empty_list = PlayerList()
        self.assertTrue(empty_list.is_empty())

    def test_player_list(self):
        """Test the length of the player list."""
        self.assertEqual(len(self.player_list), 5)

    def test_player_list_head_and_tail(self):
        """Test if head and tail are set correctly after initialization."""
        self.assertEqual(self.player_list._head._player.name(), 'Eva')
        self.assertEqual(self.player_list._tail._player.name(), 'Alice')

    def test_player_list_push_tail(self):
        """Test the push_tail method to add a player to the end of the list."""
        self.player_list.push_tail(Player("player6", "PlayerPUSH"))
        self.assertEqual(self.player_list._tail._player.name(), 'PlayerPUSH')
        self.assertEqual(self.player_list._head._player.name(), 'Eva')
        self.assertEqual(len(self.player_list), 6)

    def test_player_list_delete_head(self):
        """Test deleting the head player from the list."""
        self.player_list.delete_head()
        self.assertEqual(self.player_list._head._player.name(), 'David')
        self.assertEqual(len(self.player_list), 4)

    def test_player_list_delete_tail(self):
        """Test deleting the tail player from the list."""
        self.player_list.delete_tail()
        self.assertEqual(self.player_list._tail._player.name(), 'Bob')
        self.assertEqual(len(self.player_list), 4)

    def test_player_list_delete_key(self):
        """Test deleting a player by unique key."""
        self.player_list.delete_key("player4")
        self.assertEqual(self.player_list._head._player.name(), "Eva")
        self.assertEqual(self.player_list._tail._player.name(), "Alice")
        self.assertEqual(self.player_list._head.next_node._player.name(), "Charlie")
        self.assertEqual(len(self.player_list), 4)

    def test_player_list_display(self):
        """Test displaying the player list."""
        with Capturing() as output:
            self.player_list.display(True)

        expected_output = [
            "Player ID: player5, Name: Eva",
            "Player ID: player4, Name: David",
            "Player ID: player3, Name: Charlie",
            "Player ID: player2, Name: Bob",
            "Player ID: player1, Name: Alice"
        ]

        self.assertEqual(output, expected_output)
