from player import Player
from player_list import PlayerList

class PlayerHashMap:
    def __init__(self):
        self.size = 10
        self.hash_map = self.create_table()

    def create_table(self):
        return [[] for _ in range(self.size)]

    def put(self, key, name):
        position = key % self.size
        for k, n in self.hash_map[position]:
            if k == key:
                print(f"Key {key} already exists. No insertion.")
                return
        self.hash_map[position].append((key, name))
        print(f"Inserted '{key}' with value '{name}' at position {position}.")

    def get(self, key):
        return

    def remove(self, key):
        return

    def size(self):
        return

if __name__ == '__main__':
    player_map = PlayerHashMap()
    player1 = Player("123", "Alice")
    player2 = Player("456", "Bob")
