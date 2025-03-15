import random
import time


class Player:
    def __init__(self, player_name):
        self.unique_id = self.generate_unique_id()
        self.player_name = player_name

    def generate_unique_id(self):
        """Ref: https://medium.com/@nagendra.kumar1508/generating-unique-ids-using-python-a-practical-guide-97ed7729071d"""
        timestamp = str(int((time.time() * 0.000001)))
        random_number = str(random.randint(100, 999))
        unique_id = f"{timestamp}_{random_number}"
        return unique_id

    def __str__(self):
        return f"Player ID: {self.unique_id}, Name: {self.player_name}"

    def uid(self):
        return self.unique_id

    def name(self):
        return self.player_name
