class PlayerNode(object):
    def __init__(self, player):
        self.__player = player
        self.__next_player_node = None
        self.__previous_player_node = None