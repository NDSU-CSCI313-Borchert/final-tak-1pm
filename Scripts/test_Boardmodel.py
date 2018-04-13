import unittest
from board_model import *


class test_BoardModel(unittest.TestCase):
    def test_board_model_can_be_created(self):
        board_model = BoardModel(0,0)
        self.assertTrue(True)

    def test_board_model_has_coord_grid(self):
        board_model = BoardModel(0,0)
        self.assertTrue(board_model.coord_grid)

    def test_board_model_has_marking_grid(self):
        board_model = BoardModel(0,0)
        self.assertTrue(board_model.markGrid)