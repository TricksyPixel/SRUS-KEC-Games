class Player:
    def __init__(self, unique_id="000000", player_name="unknown"):

        self.__uid = unique_id
        self.__name = player_name

    def __str__(self):
        return f'Player ID: {self.__uid} \nPlayer Username: {self.__name}'