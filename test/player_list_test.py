import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        
        # Create set of Players
        self.player_1 = Player("000001", "Bobba")
        self.player_2 = Player("123456", "JohnCena")
        self.player_3 = Player("020304", "Doolittle")
        self.player_4 = Player("999999", "Cloud")

        # Create the Player List ready for the Players to go into
        self.player_list = PlayerList()

    # [ Test Case 1 ] - Test what happens if a new node is added to an empty list.
    def test_add_new_node_to_empty_list(self):
        
        empty_list_result = self.player_list.is_empty()

        if empty_list_result:
            self.player_list.insert_first(self.player_1, self.player_1.__uid)
            self.player_list.insert_last(self.player_1, self.player_1.__uid)
            self.player_list.insert_first(self.player_1, self.player_1.__uid)

            final_list_result = self.player_list.is_empty()
        
        self.assertTrue(final_list_result == False, "Test Case 1: Error - List still empty after adding player.")

    # [ Test Case 2 ] - Test what happens if a new node is added to an active list.
    def test_player_uid(self):
        self.player_list.insert_first(self.player_2, self.player_2.__uid)
        self.player_list.insert_last(self.player_2, self.player_2.__uid)
        self.player_list.insert_first(self.player_2, self.player_2.__uid)
        
        empty_list_result = self.player_list.is_empty()

        if empty_list_result:
            # NOTE: Working here

            final_list_result = self.player_list.is_empty()
        
        self.assertTrue(final_list_result == False, "Test Case 1: Error - List still empty after adding player.")

if __name__ == '__main__':
    unittest.main()