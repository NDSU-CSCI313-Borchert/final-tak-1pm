import unittest

import sys
sys.path.insert(0, '/final-tak-1pm/Scripts/')

from board import *

class test_Board(unittest.TestCase):
    def test_board_can_be_created(self):
        board = Board("5x5")
        self.assertTrue(True)
