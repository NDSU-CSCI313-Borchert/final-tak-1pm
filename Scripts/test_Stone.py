import unittest
from stone import *

class test_Stone(unittest.TestCase):
    def test_stone_brown_can_be_created(self):
        stone = Stone("brown_stone")
        self.assertTrue(True)

    def test_stone_beige_can_be_created(self):
        stone = Stone("beige_stone")
        self.assertTrue(True)

