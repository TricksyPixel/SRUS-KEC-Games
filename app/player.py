class Player:
    def __init__(self, unique_id, player_name):
        # TODO: Within the file you just made, create a new class called Player.
        #  Add an initialiser (constructor) function __init__ that takes two arguments:
        #       - a unique id (a string) and a player name (also a string).
        # Have the initialiser create two private instance variables and assign the
        # provided values.

        self._uid = unique_id
        self._name = player_name

    def __str__(self):
