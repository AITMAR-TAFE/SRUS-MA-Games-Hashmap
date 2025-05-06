

class Player:
    def __init__(self, unique_id: str, player_name: str, player_score: int):
        self._unique_id = unique_id
        self._player_name = player_name
        self._player_score = player_score

    def __str__(self):
        return f"Player ID: {self.uid}, Name: {self.name}, Score: {self.score}"

    def __repr__(self):
        return f"Player(unique_id='{self._unique_id}', player_name='{self._player_name}', player_score={self._player_score})"

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def __hash__(self):
        return hash((self._unique_id, self._player_name, self._player_score))

    @property
    def uid(self):
        return self._unique_id

    @classmethod
    def hash(cls, key: str, size: int) -> int:
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % size

    @property
    def name(self):
        return self._player_name

    @property
    def score(self):
        return self._player_score

    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("Invalid score: must be a positive number.")

        self._player_score = value

    @classmethod
    def sort(cls, players: list) -> list:
        if len(players) <= 1:
            return players

        middle = len(players) // 2
        pivot = players[middle]
        left = []
        right = []
        middle = []

        for x in players:
            if x == pivot:
                middle.append(x)
            elif x > pivot:
                left.append(x)
            else:
                right.append(x)
        return cls.sort(left) + middle + cls.sort(right)

