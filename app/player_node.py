class PlayerNode(object):
    def __init__(self, __player=None, __next=None, __previous=None):
        self.__player = __player
        self.__next = __next
        self.__previous = __previous

    def get_player(self):
        return self.__player
    
    def get_next_player(self):
        return self.__next
    
    def get_previous_player(self):
        return self.__previous_player
    
    def set_player(self, __player, __):
        