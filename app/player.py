class Player:
    def __init__(self, unique_id, player_name):
        self.unique_id = unique_id
        self.player_name = player_name

    def __str__(self):
        return f"Player ID: {self.unique_id}, Name: {self.player_name}"

    def uid(self):
        return self.unique_id

    def name(self):
        return self.player_name


