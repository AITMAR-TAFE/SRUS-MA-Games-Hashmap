from app.player import Player
from app.player_list import PlayerList


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
        """ Add player """
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
        """ Retrieve player by key """
        index = self.get_index(key)
        player_list_at_index = self.hash_map[index]

        for player in player_list_at_index:
            if player.uid() == key:
                return player

        return f"Player with key '{key}' not found."

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

    player_test = player_map.get("player2")
    print("player2 is Bob")
    print("test get function:", player_test.name())