import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Sets up a new stack instance for each test
        self.player = Player('123456', 'TricksyPixel')

    # Test Case 1: Test player created with username TricksyPixel, ID 123456 .
    def test_player_creation(self):
        # Return the object as a readable string
        player_object_str = self.player.__str__()

        print(f'Test case 1: Test player created with username TricksyPixel, ID 123456\n{player_object_str}\n')
        self.assertTrue(player_object_str, "Created a player object successfully.")

    # Test Case 2: Test modifying uid and player_name
    def test_change_details(self):
        self.player._name = "SpongeBob"
        self.player._uid = "999999"

        player_object_str = self.player.__str__()

        print(f'Test case 2: Modify player ID and Name\n{player_object_str}\n')
        self.assertTrue(player_object_str, 'Player ID: 999999 \nPlayer Username: SpongeBob')

if __name__ == '__main__':
    unittest.main()