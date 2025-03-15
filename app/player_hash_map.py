from player import Player
from player_list import PlayerList


class PlayerHashMap:
    def __init__(self):
        self.size = 11
        self.hash_map = self.create_table()

    def create_table(self):
        return [PlayerList() for _ in range(self.size)]

    def get_index(self, name):
        """??? Kinda double hashing again ???"""
        hash_value = 0
        for char in name:
            hash_value += ord(char)
        return hash_value

    def put(self, name):
        player= Player(name)
        key = player.uid()
        hash_tabel_id = self.get_index(key)
        linked_list_id = hash_tabel_id % self.size
        bucket = self.hash_map[linked_list_id]
        bucket.push(player)


    def get(self, key):
        return

    def remove(self, key):
        return

    def size(self):
        return

    def display(self, forward=True):
        """Displays the entire hash map with players in each bucket."""
        for i, player_list in enumerate(self.hash_map):
            print(f"Bucket {i}: ", end="")
            try:
                player_list.display(forward)
            except ValueError:
                print("Empty")

if __name__ == '__main__':
    player_map = PlayerHashMap()
    player1 = Player("Alice")
    player2 = Player("Bob")
    player3 = Player("Jessica")
    player4 = Player("Alice")
    player5 = Player("Alice")

    player_map.put(player1.name())
    player_map.put(player2.name())
    player_map.put(player3.name())
    player_map.put(player4.name())
    player_map.put(player5.name())

    print("Printing the whole player map:")
    player_map.display()