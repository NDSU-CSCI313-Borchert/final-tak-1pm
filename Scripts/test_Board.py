import unittest

from board import *

class test_Board(unittest.TestCase):
    def test_board_can_be_created(self):
        size = "5x5"
        design = "Brown"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
