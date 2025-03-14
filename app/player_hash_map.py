from player import Player
from player_list import PlayerList

class PlayerHashMap:
    def __init__(self):
        self.size = 10
        self.hash_map = self.create_table()

    def create_table(self):
        return [[] for _ in range(self.size)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return int(key.uid()) % self.size
        else:
            return hash(key) % self.size

    def put(self, key, name):
        position = self.get_index(key)
        print(key, name)

        for k, n in self.hash_map[position]:
            if k == key:
                print(f"Key {key} already exists. No insertion.")
                return
        player_list.append((key, name))
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
    player2 = Player("234", "Bob")
    player3 = Player("345", "Jessica")

    player_map.put(player1.uid(), player1.name())
    player_map.put(player2.uid(), player2.name())
    player_map.put(player3.uid(), player3.name())

    print("Printing the whole player map:")
    for index, player_list in enumerate(player_map.hash_map):
        if player_list:  # Only print non-empty lists
            print(f"Index {index}: {player_list}")