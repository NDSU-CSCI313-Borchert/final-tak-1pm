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
        self.assertEqual(len(board_model.coord_grid), (board_model.dimensions**2))

    def test_board_model_get_square_returns_correct_coord_00(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(400, 200), "00")
            
    def test_board_model_get_square_returns_correct_coord_10(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(400, 400), "10")

    def test_board_model_get_square_returns_correct_coord_20(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(400, 500), "20")

    def test_board_model_get_square_returns_correct_coord_30(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(400, 700), "30")

    def test_board_model_get_square_returns_correct_coord_40(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(400, 800), "40")

    def test_board_model_get_square_returns_correct_coord_01(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(600, 200), "01")
    
    def test_board_model_get_square_returns_correct_coord_11(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(600, 400), "11")
    
    def test_board_model_get_square_returns_correct_coord_21(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(600, 500), "21")
    
    def test_board_model_get_square_returns_correct_coord_31(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(600, 700), "31")
    
    def test_board_model_get_square_returns_correct_coord_41(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(600, 800), "41")

    def test_board_model_get_square_returns_correct_coord_02(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(800, 200), "02")
    
    def test_board_model_get_square_returns_correct_coord_12(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(800, 400), "12")
    
    def test_board_model_get_square_returns_correct_coord_22(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(800, 500), "22")
    
    def test_board_model_get_square_returns_correct_coord_32(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(800, 700), "32")
    
    def test_board_model_get_square_returns_correct_coord_42(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(800, 800), "42")

    def test_board_model_get_square_returns_correct_coord_03(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(900, 200), "03")
    
    def test_board_model_get_square_returns_correct_coord_13(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(900, 400), "13")
    
    def test_board_model_get_square_returns_correct_coord_23(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(900, 500), "23")
    
    def test_board_model_get_square_returns_correct_coord_33(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(900, 700), "33")
    
    def test_board_model_get_square_returns_correct_coord_43(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(900, 800), "43")

    def test_board_model_get_square_returns_correct_coord_04(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(1000, 200), "04")
    
    def test_board_model_get_square_returns_correct_coord_14(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(1000, 400), "14")
    
    def test_board_model_get_square_returns_correct_coord_24(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(1000, 500), "24")
    
    def test_board_model_get_square_returns_correct_coord_34(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(1000, 700), "34")
    
    def test_board_model_get_square_returns_correct_coord_44(self):
        board_model = BoardModel(0, 0, "5x5")
        self.assertEqual(board_model.get_square(1000, 800), "44")

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
