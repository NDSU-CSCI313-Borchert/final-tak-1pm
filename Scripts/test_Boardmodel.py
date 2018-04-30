import unittest
from board_model import *


class test_BoardModel(unittest.TestCase):
    
####################################Set up tests###################################
    def test_board_model_can_be_created(self):
        board_model = BoardModel((0,0),"3x3")
        self.assertTrue(True)

    def test_board_model_has_coord_grid(self):
        board_model = BoardModel((0,0),"3x3")
        self.assertTrue(board_model.coord_grid)

    def test_board_model_has_marking_grid(self):
        board_model = BoardModel((0,0),"3x3")
        self.assertTrue(board_model.markGrid)

    def test_board_model_has_dimensions_3(self):
        board_model = BoardModel((0,0),"3x3")
        self.assertEqual(board_model.dimensions, 3)
    
    def test_board_model_has_dimensions_4(self):
        board_model = BoardModel((0,0),"4x4")
        self.assertEqual(board_model.dimensions, 4)

    def test_board_model_has_dimensions_5(self):
        board_model = BoardModel((0,0),"5x5")
        self.assertEqual(board_model.dimensions, 5)

    def test_board_model_coord_grid_has_correct_length_3(self):
        board_model = BoardModel((0,0),"3x3")
        self.assertEqual(len(board_model.coord_grid), (board_model.dimensions**2))

    def test_board_model_coord_grid_has_correct_length_4(self):
        board_model = BoardModel((0,0),"4x4")
        self.assertEqual(len(board_model.coord_grid), (board_model.dimensions**2))
    
    def test_board_model_coord_grid_has_correct_length_5(self):
        board_model = BoardModel((0,0),"5x5")
        self.assertEqual(len(board_model.coord_grid), (board_model.dimensions**2))

###################get square method tests################################################
    def test_board_model_get_square_returns_correct_coord_00(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(400, 200), "00")
            
    def test_board_model_get_square_returns_correct_coord_10(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(400, 400), "10")

    def test_board_model_get_square_returns_correct_coord_20(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(400, 500), "20")

    def test_board_model_get_square_returns_correct_coord_30(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(400, 700), "30")

    def test_board_model_get_square_returns_correct_coord_40(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(400, 800), "40")

    def test_board_model_get_square_returns_correct_coord_01(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(600, 200), "01")
    
    def test_board_model_get_square_returns_correct_coord_11(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(600, 400), "11")
    
    def test_board_model_get_square_returns_correct_coord_21(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(600, 500), "21")
    
    def test_board_model_get_square_returns_correct_coord_31(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(600, 700), "31")
    
    def test_board_model_get_square_returns_correct_coord_41(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(600, 800), "41")

    def test_board_model_get_square_returns_correct_coord_02(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(800, 200), "02")
    
    def test_board_model_get_square_returns_correct_coord_12(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(800, 400), "12")
    
    def test_board_model_get_square_returns_correct_coord_22(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(800, 500), "22")
    
    def test_board_model_get_square_returns_correct_coord_32(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(800, 700), "32")
    
    def test_board_model_get_square_returns_correct_coord_42(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(800, 800), "42")

    def test_board_model_get_square_returns_correct_coord_03(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(900, 200), "03")
    
    def test_board_model_get_square_returns_correct_coord_13(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(900, 400), "13")
    
    def test_board_model_get_square_returns_correct_coord_23(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(900, 500), "23")
    
    def test_board_model_get_square_returns_correct_coord_33(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(900, 700), "33")
    
    def test_board_model_get_square_returns_correct_coord_43(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(900, 800), "43")

    def test_board_model_get_square_returns_correct_coord_04(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(1000, 200), "04")
    
    def test_board_model_get_square_returns_correct_coord_14(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(1000, 400), "14")
    
    def test_board_model_get_square_returns_correct_coord_24(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(1000, 500), "24")
    
    def test_board_model_get_square_returns_correct_coord_34(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(1000, 700), "34")
    
    def test_board_model_get_square_returns_correct_coord_44(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_square(1000, 800), "44")


###################check victory method tests################################################

#def test_board_model_can_win(self):
#   board_model = BoardModel(0, 0)
#  board_model.Mark_spot(400, 200, True, False)
# board_model.Mark_spot(529, 200, True, False)
#board_model.Mark_spot(679, 200, True, False)
#    board_model.Mark_spot(828, 200, True, False)
#   board_model.Mark_spot(980, 200, True, False)
#   board_model.Check_victory()

###################grid operations method tests################################################

#def test_board_model_can_mark(self):
#   board_model = BoardModel(0, 0)
#  self.assertTrue(board_model.Mark_spot(400,200,True,False))

# def test_board_model_occupied(self):
#    board_model = BoardModel(0, 0)
#    board_model.Mark_spot(400, 200, True, False)
#    board_model.spot_occupied(400,200)
#    self.assertEqual(board_model.spot_occupied(400,200),True)


    """
        Grid reference
        __________________________
        | 00 | 01 | 02 | 03 | 04 |
        --------------------------
        | 10 | 11 | 12 | 13 | 14 |
        --------------------------
        | 20 | 21 | 22 | 23 | 24 |
        --------------------------
        | 30 | 31 | 32 | 33 | 34 |
        --------------------------
        | 40 | 41 | 42 | 43 | 44 |
        --------------------------
    """
    def test_board_model_get_adjacent_square_returns_correct_grids_00(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("00"), ["01","10"])

    def test_board_model_get_adjacent_square_returns_correct_grids_10(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("10"), ["00","11","20"])

    def test_board_model_get_adjacent_square_returns_correct_grids_20(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("20"), ["10","21","30"])

    def test_board_model_get_adjacent_square_returns_correct_grids_30(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("30"), ["20","31","40"])

    def test_board_model_get_adjacent_square_returns_correct_grids_40(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("40"), ["30","41"])

    def test_board_model_get_adjacent_square_returns_correct_grids_01(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("01"), ["02","11","00"])

    def test_board_model_get_adjacent_square_returns_correct_grids_11(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("11"), ["01","12","21","10"])

    def test_board_model_get_adjacent_square_returns_correct_grids_21(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("21"), ["11","22","31","20"])

    def test_board_model_get_adjacent_square_returns_correct_grids_31(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("31"), ["21","32","41","30"])

    def test_board_model_get_adjacent_square_returns_correct_grids_41(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("41"), ["31","42","40"])

    def test_board_model_get_adjacent_square_returns_correct_grids_02(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("02"), ["03","12","01"])

    def test_board_model_get_adjacent_square_returns_correct_grids_12(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("12"), ["02","13","22","11"])

    def test_board_model_get_adjacent_square_returns_correct_grids_22(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("22"), ["12","23","32","21"])

    def test_board_model_get_adjacent_square_returns_correct_grids_32(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("32"), ["22","33","42","31"])

    def test_board_model_get_adjacent_square_returns_correct_grids_42(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("42"), ["32","43","41"])

    def test_board_model_get_adjacent_square_returns_correct_grids_03(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("03"), ["04","13","02"])

    def test_board_model_get_adjacent_square_returns_correct_grids_13(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("13"), ["03","14","23","12"])

    def test_board_model_get_adjacent_square_returns_correct_grids_23(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("23"), ["13","24","33","22"])

    def test_board_model_get_adjacent_square_returns_correct_grids_33(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("33"), ["23","34","43","32"])

    def test_board_model_get_adjacent_square_returns_correct_grids_43(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("43"), ["33","44","42"])

    def test_board_model_get_adjacent_square_returns_correct_grids_04(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("04"), ["14","03"])

    def test_board_model_get_adjacent_square_returns_correct_grids_14(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("14"), ["04","24","13"])

    def test_board_model_get_adjacent_square_returns_correct_grids_24(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("24"), ["14","34","23"])

    def test_board_model_get_adjacent_square_returns_correct_grids_34(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("34"), ["24","44","33"])

    def test_board_model_get_adjacent_square_returns_correct_grids_44(self):
        board_model = BoardModel((0, 0), "5x5")
        self.assertEqual(board_model.get_adjacent_squares("44"), ["34","43"])





































