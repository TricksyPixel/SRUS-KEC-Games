from app.player_list import PlayerList

key = None

class PlayerNode(object):
    def __init__(self, player, uid):
        __next = None
        __previous = None

        key =  uid

        self.__player = player
        self.__next = __next
        self.__previous = __previous

    def get_player(self):
        return self.__player
    
    def get_next_player(self):
        return self.__next

    def get_previous_player(self):
        return self.__previous
    
    def set_player(self, __player):
        self.__player = __player

    def set_next_player(self, __next):
        self.__next = __next

    def __str__(self):
        curr_player_msg = get_player(self)
        next_player_node_msg = get_next_player(self)
        prev_player_node_msg = get_previous_player(self)

        return (f'Current player: {curr_player_msg}\n'
                f'Next player node: {next_player_node_msg}\n'
                f'Prev player node: {prev_player_node_msg}')