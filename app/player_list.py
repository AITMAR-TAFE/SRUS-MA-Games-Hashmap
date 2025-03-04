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
            # self._tail.prev_node = None

        self._len -= 1


    def is_empty(self):
        if self._head is None:
            return True

# if __name__ == '__main__':
#     players = PlayerList()
#     players.push('Player1')
#     players.push('Player2')
#     players.push('Player3')
#     players.push('Player4')
#     print(f"Before delete head: Head: {players._head._player}, Tail: {players._tail._player}")
#     players.delete_head()
#     print(f"After delete head: Head: {players._head._player}, Tail: {players._tail._player}")
#     print("----")
#     print(f"Before delete tail: Head: {players._head._player}, Tail: {players._tail._player}")
#     players.delete_tail()
#     print(f"After delete tail: Head: {players._head._player}, Tail: {players._tail._player}")

