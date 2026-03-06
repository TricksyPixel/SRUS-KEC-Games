class PlayerNode(object):

    __player = None
    __next = None
    __previous = None

    def __init__(self, player):
        self.__player = player
        self.__previous = None

        self.__next = None
    
    def __str__(self):
        return f'Current: {self.__player} \nPrevious: {self.__previous} \nNext: {self.__next}'