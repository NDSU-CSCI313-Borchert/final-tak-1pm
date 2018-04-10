import unittest
from stone import *

class test_Stone(unittest.TestCase):
    def test_stone_brown_can_be_created(self):
        stone = Stone("brown_stone", "brown_wall")
        self.assertTrue(True)

    def test_stone_beige_can_be_created(self):
        stone = Stone("beige_stone", "beige_wall")
        self.assertTrue(True)

    def test_stone_brown_can_be_turned_into_wall(self):
        stone = Stone("brown_stone", "brown_wall")
        stone.flipStone()
        self.assertTrue(True)

    def test_stone_beige_can_be_turned_into_wall(self):
        stone = Stone("beige_stone", "beige_wall")
        stone.flipStone()
        self.assertTrue(True)

    def test_wall_brown_can_be_turned_back_into_flat_stone(self):
        stone = Stone("brown_stone", "brown_wall")
        stone.flipStone()
        stone.flipStone()
        self.assertTrue(True)

    def test_wall_beige_can_be_turned_back_into_flat_stone(self):
        stone = Stone("beige_stone", "beige_wall")
        stone.flipStone()
        stone.flipStone()
        self.assertTrue(True)

    def test_stone_brown_flat_name_is_correct(self):
        stone = Stone("brown_stone", "brown_wall")
        self.assertEqual(stone.name, "flat")

    def test_stone_beige_flat_name_is_correct(self):
        stone = Stone("beige_stone", "beige_wall")
        self.assertEqual(stone.name, "flat")

    def test_stone_brown_wall_name_is_correct(self):
        stone = Stone("brown_stone", "brown_wall")
        stone.flipStone()
        self.assertEqual(stone.name, "wall")

    def test_stone_beige_wall_name_is_correct(self):
        stone = Stone("beige_stone", "beige_wall")
        stone.flipStone()
        self.assertEqual(stone.name, "wall")














