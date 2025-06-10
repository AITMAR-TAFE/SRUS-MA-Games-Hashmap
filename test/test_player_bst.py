import unittest
from app.player import Player
from app.player_bnode import PlayerBNode
from app.player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):

    def setUp(self):
        self.bst = PlayerBST()
        self.player1 = Player("ID1", "Alice", 100)
        self.player2 = Player("ID2", "Bob", 150)
        self.player3 = Player("ID3", "Charlie", 200)
        self.player4 = Player("ID4", "Fiona", 90)
        self.player5 = Player("ID5", "Elena", 180)
        self.player6 = Player("ID6", "Aadila", 120)
        self.player7 = Player("ID7", "Xavier", 300)

    def insert_players(self, players):
        for player in players:
            self.bst.insert(player)

    def players_group_1(self):
        return [self.player2, self.player1, self.player4]

    def players_group_2(self):
        return [self.player2, self.player1, self.player4, self.player5, self.player6]

    def players_group_all(self):
        return [self.player2, self.player1, self.player3, self.player4, self.player5, self.player6, self.player7]

    def test_insert_single_node_sets_root_to_that_node(self):
        self.bst.insert(self.player2)
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.player.name, "Bob")

    def test_insert_multiple_nodes_places_left_and_right_subtrees_correctly(self):
        self.insert_players(self.players_group_1())
        self.assertEqual(self.bst.root.player.name, "Bob")
        self.assertEqual(self.bst.root.left.player.name, "Alice")
        self.assertEqual(self.bst.root.right.player.name, "Fiona")

    def test_insert_existing_player_name_updates_score(self):
        updated_player = Player("ID1", "Alice", 300)
        self.bst.insert(self.player1)
        self.bst.insert(updated_player)
        self.assertEqual(self.bst.root.player.name, "Alice")
        self.assertEqual(self.bst.root.player.score, 300)

    def test_search_returns_none_when_tree_is_empty(self):
        empty_tree = PlayerBST()
        result = empty_tree.search("Alice")
        self.assertIsNone(result)

    def test_search_returns_node_when_root_matches_name(self):
        self.bst.insert(self.player1)
        result = self.bst.search("Alice")
        self.assertEqual(result.player.name, "Alice")

    def test_search_returns_correct_nodes_for_existing_players_and_none_for_nonexistent(self):
        self.insert_players(self.players_group_2())
        result = self.bst.search("Alice")
        self.assertEqual(result.player.name, "Alice")

        result = self.bst.search("Bob")
        self.assertEqual(result.player.name, "Bob")

        result = self.bst.search("David")
        self.assertIsNone(result)

    def test_create_sorted_list_returns_players_in_alphabetical_order_by_name(self):
        self.insert_players(self.players_group_2())
        result = self.bst.create_sorted_list(self.bst.root)

        correct_answer = [
            Player(unique_id='ID6', player_name='Aadila', player_score=120),
            Player(unique_id='ID1', player_name='Alice', player_score=100),
            Player(unique_id='ID2', player_name='Bob', player_score=150),
            Player(unique_id='ID5', player_name='Elena', player_score=180),
            Player(unique_id='ID4', player_name='Fiona', player_score=90),
        ]
        self.assertEqual(correct_answer, result)

    def test_balanced_bst_rebalances_tree_correctly_with_middle_element_as_root(self):
        self.insert_players(self.players_group_all())
        sorted_list = self.bst.create_sorted_list(self.bst.root)
        self.bst.balanced_bst(sorted_list)

        self.assertEqual(self.bst.root.player.name, "Charlie")
        self.assertEqual(self.bst.root.left.player.name, "Alice")
        self.assertEqual(self.bst.root.right.player.name, "Fiona")
