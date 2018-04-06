import unittest
from player import *

class test_Player(unittest.TestCase):
    def test_player_can_be_created(self):
        player = Player()
        self.assertTrue(True)

    def test_player_has_correct_stones(self):
        player = Player()
        self.assertEqual(player.stones, 21)

    def test_player_has_correct_capstones(self):
        player = Player()
        self.assertEqual(player.capstones, 1)
