

class Player:
    def __init__(self, unique_id: str, player_name: str):
        self._unique_id = unique_id
        self._player_name = player_name

    def __str__(self):
        return f"Player ID: {self.uid}, Name: {self.name}"

    def uid(self):
        return self._unique_id

    @classmethod
    def hash(cls, key: str) -> int:
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value

    def name(self):
        return self._player_name

