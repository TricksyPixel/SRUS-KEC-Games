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
        
        self.player_list.insert_first(self.player_1.__uid)

        empty_list = self.player_list.is_empty()

        self.player_list.print_forward()
        
        self.assertFalse(empty_list, "Test Case 1: Error - List still empty after trying to add player.")
        self.assertEqual(self.player_list._first, self.player_1, "Test Case 1: Error - First node is not the player added.")

        

    # [ Test Case 2 ] - Test what happens when adding a new node to first list item on an already active list.
    def test_player_uid(self):
        first_node_replaced = False

        self.player_list.insert_first(self.player_2.__uid)
        self.player_list.insert_first(self.player_3.__uid)
        
        result = self.player_list.find(self.player_3.__uid)

        if self.player_list[0] == self.player_3.__uid:
            first_node_replaced = True
        
        self.player_list.print_forward()

        self.assertTrue(first_node_replaced, "Test Case 2: Error - First player not player_3.")

if __name__ == '__main__':
    unittest.main()