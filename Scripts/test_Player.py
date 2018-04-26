import unittest
from player import *

class test_Player(unittest.TestCase):
    def test_player_can_be_created(self):
        player = Player(21, 1)
        self.assertTrue(True)

    def test_player_has_correct_stones(self):
        player = Player(21, 1)
        self.assertEqual(player.stones, 21)

    def test_player_has_correct_capstones(self):
        player = Player(21, 1)
        self.assertEqual(player.capstones, 1)

    def test_player_has_correct_stones_after_removing_stone(self):
        player = Player(21, 1)
        player.removeStone()
        self.assertEqual(player.stones, 20)

    def test_player_has_correct_capstones_after_removing_capstone(self):
        player = Player(21, 1)
        player.removeCapstone()
        self.assertEqual(player.capstones, 0)
