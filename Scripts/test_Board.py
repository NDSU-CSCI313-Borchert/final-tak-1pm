import unittest

from board import *

class test_Board(unittest.TestCase):
    def test_board_can_be_created(self):
        board = Board("5x5_Board")
        self.assertTrue(True)
