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

    def test_player_has_correct_stones_after_removing_stone(self):
        player = Player()
        player.removeStone()
        self.assertEqual(player.stones, 20)

    def test_player_has_correct_capstones_after_removing_capstone(self):
        player = Player()
        player.removeCapstone()
        self.assertEqual(player.capstones, 0)
