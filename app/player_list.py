from app.player_node import PlayerNode

class PlayerList(object):
    def __init__(self):
        self.__first = None
        self.__last = None
    
    def is_empty(self):
        return self.__first is None

    def find(self, key):
        current = self.__first
        
        while current and current.__player != key:
            current = current.__next
        
        return current
    
    def insert_first(self, key):
        new_player_node = PlayerNode(key)
        if self.__first is None:
            self.__last = new_player_node
            
        new_player_node.next = self.__first
        self.__first = new_player_node
    
    def insert_last(self, key):
        new_player_node = PlayerNode(key)
        if self.__first is None:
            self.__first = new_player_node
        else:
            self.__last.__next = new_player_node

            self.__last = new_player_node

    def delete(self, key):
        current = self.__first
        previous = self.__first
        while current and current.__player != key:
            previous = current
            current = current.__next

        if current is not None:
            if current == self.__first:
                self.__first = self.__first.__next
            else:
                previous.next = current.__next

        return current
    
    def delete_first(self):
        temporary_node = self.__first
        if self.__first is not None:
            self.__first = self.__first.__next

        return temporary_node
    
    def display(self, forwards = True):
        if forwards:
            # Prints list forwards
            print("List first to last: ")
            current = self.__first
            while current is not None:
                print(current)
            current = current.__next
        else:
            # Prints list backwards
            print("List last to first: ")
            current = self.__last
            while current:
                temp = current.__next
                current.__previous = temp
                current = current.__previous
        
            temp = self.__last
            self.__last = self.__first
            self.__first = temp