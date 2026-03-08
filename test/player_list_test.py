import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        
        # Create the Player List ready for the Players to go into
        self.player_list = PlayerList()

    # [ Test Case 1 ] - Test what happens if a new node is added to the first node of an empty list.
    def test_insert_first_node_to_empty_list(self):
        
        self.player_1 = Player("000001", "Bobba")
        
        self.player_list.insert_first(self.player_1.__uid)

        empty_list = self.player_list.is_empty()
        
        self.assertFalse(empty_list, "Test Case 1: Error - List still empty after trying to add player.")
        self.assertEqual(self.player_list._first, self.player_1.__uid, "Test Case 1: Error - First node is not the player added.")

    # [ Test Case 2 ] - Test what happens when adding a new node to first list item on an already active list.
    def test_insert_two_to_first_node(self):
        
        self.player_2 = Player("123456", "JohnCena")
        self.player_3 = Player("020304", "Doolittle")

        first_node_replaced = False

        self.player_list.insert_first(self.player_2.__uid)
        self.player_list.insert_first(self.player_3.__uid)
        
        if self.player_list[0] == self.player_3.__uid:
            first_node_replaced = True
        
        self.assertTrue(first_node_replaced, "Test Case 2: Error - First player not player_3.")

    #[ Test Case 3 ] Test for inserting to last node of list.
    def test_insert_to_last_node(self):
        
        self.player_4 = Player("999999", "Cloud")
        self.player_5 = Player("101010", "DavidBowie")
        self.player_6 = Player("600600", "TheManWhoSoldTheWorld")

        last_node_replaced = False

        self.player_list.insert_last(self.player_4.__uid)
        self.player_list.insert_last(self.player_5.__uid)
        self.player_list.insert_last(self.player_6.__uid)
        
        if self.player_list[2] == self.player_6.__uid:
            last_node_replaced = True
        
        self.assertTrue(last_node_replaced, "Test Case 3: Error - Last player not player_6.")

if __name__ == '__main__':
    unittest.main()