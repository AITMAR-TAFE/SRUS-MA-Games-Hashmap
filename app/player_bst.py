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

    def print_for_testing(self, node):
        if node:
            self.print_for_testing(node.left)
            print(node.player)
            self.print_for_testing(node.right)
