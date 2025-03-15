from player import Player
from player_list import PlayerList


class PlayerHashMap:
    def __init__(self):
        self.size = 11
        self.hash_map = self.create_table()

    def create_table(self):
        return [PlayerList() for _ in range(self.size)]

    def get_index(self, key: str) -> int:
        """Calculate index from characters in key, return int"""
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def put(self, key: str, name: str):
        index = self.get_index(key)
        player_list = self.hash_map[index]

        # If player already exists, update name not uid
        for player in player_list:
            if player.uid() == key:
                player.name = name
                print("Player name changed")
                return

        new_player = Player(key, name)
        player_list.push(new_player)


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
    player_map.put("player1", "Alice")
    player_map.put("player2", "Bob")
    player_map.put("player3", "Jessica")
    player_map.put("player4", "Alice")
    player_map.put("player5", "Alice")
    player_map.put("player6", "Charlie")
    player_map.put("player7", "David")
    player_map.put("player8", "Eva")
    player_map.put("player9", "Frank")
    player_map.put("player10", "Grace")
    player_map.put("player11", "Hannah")
    player_map.put("player12", "Ivy")
    player_map.put("player13", "Jack")
    player_map.put("player14", "Karen")
    player_map.put("player15", "Leo")
    player_map.put("player16", "Mia")
    player_map.put("player17", "Nina")
    player_map.put("player18", "Oliver")
    player_map.put("player19", "Paul")
    player_map.put("player20", "Quinn")
    player_map.put("player21", "Riley")
    player_map.put("player22", "Sophia")
    player_map.put("player23", "Tyler")
    player_map.put("player24", "Uma")
    player_map.put("player25", "Victor")

    print("Printing the whole player map:")
    player_map.display()