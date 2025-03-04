from app.player_node import PlayerNode


class PlayerList(object):
    def __init__(self, values=None):
        self._head = None
        self._tail = None
        self._len = 0
        if values is not None:
            for item in values:
                self.push(item)

    def __len__(self):
        return self._len

    def push(self, value):
        new_node = PlayerNode(value)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node

        else:
            new_node.next_player = self._head
            self._head.prev_node = new_node
            self._head = new_node

            current_node = self._head
            while current_node.next_node is not None:
                current_node = current_node.next_node
                self._tail = current_node

        self._len += 1

    def is_empty(self):
        if self._head is None:
            return True
