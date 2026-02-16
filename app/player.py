class Player:
    def __init__(self, unique_id, player_name):

        self._uid = unique_id
        self._name = player_name

    def __str__(self):
        return f'Player ID: {self._uid} \nPlayer Username: {self._name}'