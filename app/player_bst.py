from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def insert(self, player):
        if self.root is None:
            self.root = PlayerBNode(player)
        else:
            self._insert(player, self.root)

    def _insert(self, player, current_node):
        if player.name < current_node.player.name:
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                self._insert(player, current_node.left)
        elif player.name > current_node.player.name:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                self._insert(player, current_node.right)
        else:
            current_node._player = player

    def search(self, name):
        # steps = 0         For steps testing purposes
        node = self.root
        while node:
            # steps += 1
            if node is None or node.player.name == name:
                return node #, steps

            if name < node.player.name:
                node = node.left

            else:
                node = node.right
        #return None, steps

    def balanced_bst(self, sorted_list):
        self.root = None

        def build_recursively(my_list):
            if len(my_list) == 0:
                return
            middle_element = len(my_list) // 2
            player = my_list[middle_element]
            self.insert(player)  # use insert to add player properly
            build_recursively(my_list[:middle_element])
            build_recursively(my_list[middle_element + 1:])
        build_recursively(sorted_list)

    def create_sorted_list(self, node, in_order_list=None):
        if in_order_list is None:
            in_order_list = []

        if node:
            self.create_sorted_list(node.left, in_order_list)
            in_order_list.append(node.player)
            self.create_sorted_list(node.right, in_order_list)

        if node == self._root:
            return in_order_list

    def print_for_testing(self, node):
        if node:
            self.print_for_testing(node.left)
            print(node.player)
            self.print_for_testing(node.right)


# tree = PlayerBST()
#
# player1 = Player("ID1", "Alice", 100)
# player2 = Player("ID2", "Bob", 150)
# player3 = Player("ID3", "Charlie", 200)
# player4 = Player("ID4", "Fiona", 90)
# player5 = Player("ID5", "Elena", 180)
# player6 = Player("ID6", "Aadila", 120)  # Should be before Alice
#
# tree.insert(player4)
# tree.insert(player2)
# tree.insert(player5)
# tree.insert(player3)
# tree.insert(player1)
# tree.insert(player6)
#
# sorted_players = tree.create_sorted_list(tree.root)
# tree.balanced_bst(sorted_players)
#
# player, steps = tree.search("Bob")
# if player:
#     print(f"Player found: {player}")
#     print(f"Steps taken: {steps}")
# else:
#     print("Player not found")