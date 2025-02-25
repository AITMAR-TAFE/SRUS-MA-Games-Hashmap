class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next_node = None
        self._prev_node = None

    @property
    def player(self):
        return self._player

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        self._next_node = value

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, value):
        self._prev_node = value

    @property
    def key(self):
        return self._player.uid()

    def __str__(self):
        return f"PlayerNode(uid={self.key}, player_name={self._player.name()})"
