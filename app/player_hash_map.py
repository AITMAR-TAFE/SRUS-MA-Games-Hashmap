from player import Player
from player_list import PlayerList


class PlayerHashMap:
    def __init__(self):
        self.size = 11
        self.hash_map = self.create_table()

    def create_table(self):
        return [PlayerList() for _ in range(self.size)]

    def get_index(self, name):
        hash_value = 0
        for char in name:
            hash_value += ord(char)
        return hash_value

    def put(self, key, name):
        hash_tabel_id = self.get_index(name)
        linked_list_id = hash_tabel_id % self.size
        bucket = self.hash_map[linked_list_id]
        bucket.push(Player(key, name))


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
    player1 = Player("123", "Alice")
    player2 = Player("234", "Bob")
    player3 = Player("345", "Jessica")
    player4 = Player("234", "Alice")
    player5 = Player("345", "Alice")

    player_map.put(player1.uid(), player1.name())
    player_map.put(player2.uid(), player2.name())
    player_map.put(player3.uid(), player3.name())
    player_map.put(player4.uid(), player4.name())
    player_map.put(player5.uid(), player5.name())

    print("Printing the whole player map:")
    player_map.display()