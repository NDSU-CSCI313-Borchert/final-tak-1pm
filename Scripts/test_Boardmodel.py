import unittest
from board_model import *


class test_BoardModel(unittest.TestCase):
    def test_board_model_can_be_created(self):
        board_model = BoardModel(0,0,"3x3")
        self.assertTrue(True)

    def test_board_model_has_coord_grid(self):
        board_model = BoardModel(0,0,"3x3")
        self.assertTrue(board_model.coord_grid)

    def test_board_model_has_marking_grid(self):
        board_model = BoardModel(0,0,"3x3")
        self.assertTrue(board_model.markGrid)

    def test_board_model_has_dimensions(self):
        board_model = BoardModel(0,0,"3x3")
        self.assertEqual(board_model.dimensions, 3)

    def test_board_model_coord_grid_has_correct_length(self):
        board_model = BoardModel(0,0,"3x3")
        self.assertEqual(len(board_model.coord_grid), 3)

    #def test_board_model_can_mark(self):
     #   board_model = BoardModel(0, 0)
      #  self.assertTrue(board_model.Mark_spot(400,200,True,False))

    #def test_board_model_can_win(self):
     #   board_model = BoardModel(0, 0)
      #  board_model.Mark_spot(400, 200, True, False)
       # board_model.Mark_spot(529, 200, True, False)
        #board_model.Mark_spot(679, 200, True, False)
    #    board_model.Mark_spot(828, 200, True, False)
     #   board_model.Mark_spot(980, 200, True, False)
     #   board_model.Check_victory()

   # def test_board_model_occupied(self):
    #    board_model = BoardModel(0, 0)
    #    board_model.Mark_spot(400, 200, True, False)
    #    board_model.spot_occupied(400,200)
    #    self.assertEqual(board_model.spot_occupied(400,200),True)