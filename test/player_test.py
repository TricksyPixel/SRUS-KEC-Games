import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    # [ Test Case 1 ] - Give the player a name.
    def test_player_name(self):
        player_created_with_username = False
        
        self.player.__name = "DefaultUsername"
        #self.player.__name = "SomeOtherName"
        
        # Check if __name of this instance is now "DefaultUsername"
        player_created_message = self.player.__str__()

        if "DefaultUsername" in player_created_message:
            player_created_with_username = True

        self.assertTrue(player_created_with_username, "Test Case 1: Error - Name: 'DefaultUsername' not contained in string.")

    # [ Test Case 2 ] - Give the player an ID.
    def test_player_uid(self):
        player_created_with_uid = False
        
        self.player.__uid = "999999"
        #self.player.__uid = "999991"
        
        # Check if __uid of this instance is now "999999"
        player_created_message = self.player.__str__()

        if "999999" in player_created_message:
            player_created_with_uid = True

        self.assertTrue(player_created_with_uid, "Test Case 2: Error - UID: '999999' not contained in string.")

if __name__ == '__main__':
    unittest.main()