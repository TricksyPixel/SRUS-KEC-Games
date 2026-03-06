from app.player_node import PlayerNode
from app.player import Player

class PlayerList(object):
    def __init__(self):
        self.__first = None
    
    def is_empty(self):
        return self.__first is None

    def find(self, key):
        current = self.__first
        
        while current and current.__player != key:
            current = current.next
        
        return current
    
    def insert_first(self, key):
        new_player_node = PlayerNode(key)
        new_player_node.next = self.__first
        self.__first = new_player_node

    def delete(self, key):
        current = self.__first
        previous = self.__first
        while current and current.__player != key:
            previous = current
            current = current.next

        if current is not None:
            if current == self.__first:
                self.__first = self.__first.next
            else:
                previous.next = current.next

        return current
    
    def delete_first(self):
        temporary_node = self.__first
        if self.__first is not None:
            self.__first = self.__first.next

        return temporary_node
    