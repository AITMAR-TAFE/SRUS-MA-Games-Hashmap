from app.player_node import PlayerNode
from app.player import Player


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
            new_node.next_node = self._head
            self._head.prev_node = new_node
            self._head = new_node

            current_node = self._head
            while current_node.next_node is not None:
                current_node = current_node.next_node
                self._tail = current_node

        self._len += 1

    def push_tail(self, value):
        new_node = PlayerNode(value)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node

        else:
            self._tail.next_node = new_node
            new_node.prev_node = self._tail
            self._tail = new_node

    def delete_head(self):
        if self.is_empty():
            raise ValueError

        if self._head == self._tail:
            self._head = None
            self._tail = None

        else:
            self._head = self._head.next_node
            self._head.prev_node = None

        self._len -= 1

    def delete_tail(self):
        if self.is_empty():
            raise ValueError

        if self._tail == self._head:
            self._tail = None
            self._head = None

        else:
            self._tail = self._tail.prev_node
            self._tail.prev_node = None

        self._len -= 1

    def delete_key(self, value):
        if self.is_empty():
            raise ValueError

        current_node = self._head

        # option 1 - If the head of list matches value that needs to be deleted
        if current_node.key == value:
            self._head = self._head.next_node
            if self._head:
                self._head.prev_node = None
            else:
                self._tail = None
            return

        # option 2 - Head is not the value
        while current_node is not None:
            if current_node.key == value:
                prev_node = current_node.prev_node
                next_node = current_node.next_node

                if prev_node is not None:
                    prev_node.next_node = next_node

                if next_node is not None:
                    next_node.prev_node = prev_node

                return

            current_node = current_node.next_node

    def is_empty(self):
        if self._head is None:
            return True

    def display(self, forward: bool):
        if self.is_empty():
            raise ValueError

        current_node = self._head if forward else self._tail

        while current_node is not None:
            print(current_node.player)
            current_node = current_node.next_node if forward else current_node.prev_node


if __name__ == '__main__':
    players = PlayerList()
    players.push(Player(unique_id=1, player_name="Player1"))
    players.push(Player(unique_id=2, player_name="Player2"))
    players.push(Player(unique_id=3, player_name="Player3"))
    players.push(Player(unique_id=4, player_name="Player4"))
    players.push(Player(unique_id=5, player_name="Player5"))
    players.display(True)
    print("---------------")
    players.delete_key(4)
    players.display(True)

