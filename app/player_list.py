from app.player_node import PlayerNode
from app.player import Player


class PlayerList(object):
    """Initializes an empty PlayerList or creates it with given values."""
    def __init__(self, values=None):
        self._head = None
        self._tail = None
        self._len = 0
        if values is not None:
            for item in values:
                self.push(item)

    def __len__(self):
        """Returns the length of the player list."""
        return self._len

    def __iter__(self):
        """Make the PlayerList iterable."""
        current_node = self._head
        while current_node:
            yield current_node.player  # Yield the player object at each node
            current_node = current_node.next_node

    def push(self, value):
        """Add a player to the front of the list."""
        new_node = PlayerNode(value)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            self._len += 1
            return


        # Insert at the front of the list
        new_node.next_node = self._head
        self._head.prev_node = new_node
        self._head = new_node

        current_node = self._head
        while current_node.next_node is not None:
            current_node = current_node.next_node
            self._tail = current_node
        self._len += 1

    def push_tail(self, value):
        """Add a player to the end of the list."""
        new_node = PlayerNode(value)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            return

        # Insert at the end of the list
        self._tail.next_node = new_node
        new_node.prev_node = self._tail
        self._tail = new_node
        self._len += 1

    def delete_head(self):
        """Remove the latest added player of the list."""
        if self.is_empty():
            raise ValueError("The list is already empty")

        if self._head == self._tail:
            self._head = None
            self._tail = None

        else:
            self._head = self._head.next_node
            self._head.prev_node = None

        self._len -= 1

    def delete_tail(self):
        """Remove the first added player of the list."""
        if self.is_empty():
            raise ValueError("The list is already empty")

        if self._tail == self._head:
            self._tail = None
            self._head = None

        else:
            self._tail = self._tail.prev_node
            self._tail.next_node = None

        self._len -= 1

    def delete_key(self, value):
        """Deletes the node with the given key value."""
        if self.is_empty():
            raise ValueError("The list is empty")

        current_node = self._head

        # If the head of list matches value that needs to be deleted
        if current_node.key == value:
            self._head = self._head.next_node
            if self._head:
                self._head.prev_node = None
            else:
                self._tail = None  # If the list becomes empty then update the tail also
            self._len -= 1
            return

        # Is head is not the value, find the node to delete in the list
        while current_node is not None:
            if current_node.key == value:
                prev_node = current_node.prev_node
                next_node = current_node.next_node

                if prev_node is not None:
                    prev_node.next_node = next_node

                if next_node is not None:
                    next_node.prev_node = prev_node

                self._len -= 1
                return

            current_node = current_node.next_node
        raise ValueError(f"Key {value} not found")

    def is_empty(self):
        """Returns True if the list is empty, otherwise False."""
        return self._head is None

    def display(self, forward: bool):
        """Displays all players in the list in either forward or reverse order."""
        if self.is_empty():
            raise ValueError("The list is empty")

        current_node = self._head if forward else self._tail

        while current_node is not None:
            print(current_node.player)
            current_node = current_node.next_node if forward else current_node.prev_node


if __name__ == '__main__':
    players = PlayerList()
    players.push(Player("player1", player_name="Player1"))
    players.push(Player("player2", player_name="Player2"))
    players.push(Player("player3", player_name="Player3"))
    players.push(Player("player4", player_name="Player4"))
    players.push(Player("player5", player_name="PUSH HEAD"))

    print("After Push:")
    print("Length:", len(players))
    players.display(True)
    print("---------------")

    players.delete_head()
    print("After Delete Head:")
    print("Length:", len(players))
    players.display(True)
    print("---------------")

    players.push_tail(Player("player6", player_name="PUSH TAIL"))
    print("After Push Tail:")
    print("Length:", len(players))
    players.display(True)
    print("---------------")

    players.delete_tail()
    print("After Delete Tail:")
    print("Length:", len(players))
    players.display(True)
    print("---------------")

    players.delete_key(3)
    print("After Delete Key (ID 3):")
    print("Length:", len(players))
    players.display(True)

