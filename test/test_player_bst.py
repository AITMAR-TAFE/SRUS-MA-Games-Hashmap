import unittest
from app.player import Player
from app.player_bnode import PlayerBNode
from app.player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):

    def setUp(self):
        """Setup before each test"""
        self.bst = PlayerBST()
        self.player1 = Player("ID1", "Alice", 100)
        self.player2 = Player("ID2", "Bob", 150)
        self.player3 = Player("ID3", "Charlie", 200)
        self.player4 = Player("ID4", "Fiona", 90)
        self.player5 = Player("ID5", "Elena", 180)
        self.player6 = Player("ID6", "Aadila", 120)  # Should be before Alice
        self.player7 = Player("ID7", "Xavier", 300)

    def test_insert_single_node_sets_root(self):
        """Test insert method sets root node correctly"""
        self.bst.insert(self.player2)
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.player.name, "Bob")

    def test_insert_places_left_and_right_correctly(self):
        """Test insert method places players correctly in subtrees"""
        self.bst.insert(self.player2)
        self.bst.insert(self.player1)
        self.bst.insert(self.player4)

        self.assertEqual(self.bst.root.player.name, "Bob")
        self.assertEqual(self.bst.root.left.player.name, "Alice")
        self.assertEqual(self.bst.root.right.player.name, "Fiona")

    def test_insert_same_player_name(self):
        updated_player = Player("ID1", "Alice", 300)
        self.bst.insert(self.player1)
        self.bst.insert(updated_player)

        self.assertEqual(self.bst.root.player.name, "Alice")
        self.assertEqual(self.bst.root.player.score, 300)

    def test_search_root_is_none(self):
        empty_tree = PlayerBST()
        result = empty_tree.search("Alice")
        self.assertIsNone(result)

    def test_search_root_matches_name(self):
        self.bst.insert(self.player1)
        result = self.bst.search("Alice")
        self.assertEqual(result.player.name, "Alice")

    def test_search_works(self):
        self.bst.insert(self.player2)
        self.bst.insert(self.player1)
        self.bst.insert(self.player4)
        self.bst.insert(self.player5)
        self.bst.insert(self.player6)

        result = self.bst.search("Alice")
        self.assertEqual(result.player.name, "Alice")

        result = self.bst.search("Bob")
        self.assertEqual(result.player.name, "Bob")

        result = self.bst.search("David")
        self.assertIsNone(result)   # David is NOT in the tree, so result should be None

    def test_create_sorted_list(self):
        self.bst.insert(self.player2)
        self.bst.insert(self.player1)
        self.bst.insert(self.player4)
        self.bst.insert(self.player5)
        self.bst.insert(self.player6)

        result = self.bst.create_sorted_list(self.bst.root)
        correct_answer = [Player(unique_id='ID6', player_name='Aadila', player_score=120),
                          Player(unique_id='ID1', player_name='Alice', player_score=100),
                          Player(unique_id='ID2', player_name='Bob', player_score=150),
                          Player(unique_id='ID5', player_name='Elena', player_score=180),
                          Player(unique_id='ID4', player_name='Fiona', player_score=90)]
        self.assertEqual(correct_answer, result)

    def test_balanced_bst_structure(self):
        self.bst.insert(self.player2)
        self.bst.insert(self.player1)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)
        self.bst.insert(self.player5)
        self.bst.insert(self.player6)
        self.bst.insert(self.player7)
        sorted_list = self.bst.create_sorted_list(self.bst.root)
        self.bst.balanced_bst(sorted_list)

        # After balancing, the root should be the middle element: "Charlie"
        self.assertEqual(self.bst.root.player.name, "Charlie")
        self.assertEqual(self.bst.root.left.player.name, "Alice")
        self.assertEqual(self.bst.root.right.player.name, "Fiona")

