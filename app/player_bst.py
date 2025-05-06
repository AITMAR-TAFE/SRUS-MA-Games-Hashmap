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
            node = self.root

            while True:
                if player.name < node.player.name:
                    if node.left is None:
                        node.left = PlayerBNode(player)
                        break
                    else:
                        node = node.left
                elif player.name > node.player.name:
                    if node.right is None:
                        node.right = PlayerBNode(player)
                        break
                    else:
                        node = node.right
                else:
                    node._player = player
                    break

    def search(self, name):
        node = self.root
        while node:
            if node is None or node.player.name == name:
                return node

            if name < node.player.name:
                node = node.left

            else:
                node = node.right

    def balanced_bst(self, sorted_list):
        def build_recursively(my_list):
            if len(my_list) == 0: #If the list is empty
                return None
            middle_element = len(my_list) // 2
            node = PlayerBNode(my_list[middle_element])
            node.left = build_recursively(my_list[:middle_element])
            node.right = build_recursively(my_list[middle_element + 1:])
            print("The middle:", node," The left:", node.left, " The right:", node.right)
            return node

        self.root = build_recursively(sorted_list)

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


tree = PlayerBST()

player1 = Player("ID1", "Alice", 100)
player2 = Player("ID2", "Bob", 150)
player3 = Player("ID3", "Charlie", 200)
player4 = Player("ID4", "Fiona", 90)
player5 = Player("ID5", "Elena", 180)
player6 = Player("ID6", "Aadila", 120)  # Should be before Alice
player7 = Player("ID7", "Xavier", 300)

tree.insert(player4)
tree.insert(player2)
tree.insert(player5)
tree.insert(player3)
tree.insert(player1)
tree.insert(player6)
tree.insert(player7)

sorted_players = tree.create_sorted_list(tree.root)
tree.balanced_bst(sorted_players)