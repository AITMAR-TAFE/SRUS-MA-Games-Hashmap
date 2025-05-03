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

    def print_for_testing(self, node):
        if node:
            self.print_for_testing(node.left)
            print(node.player)
            self.print_for_testing(node.right)


# player1 = Player("A1", "Alice", 100)
# player2 = Player("B2", "Bob", 150)
# player3 = Player("C3", "Charlie", 120)
# player4 = Player("A1", "Alice", 200)
#
# player_bst = PlayerBST()
# player_bst.insert(player1)
# player_bst.insert(player2)
# player_bst.insert(player3)
# player_bst.insert(player4)
#
# print("--TESTING--")
# player_bst.print_for_testing(player_bst.root)