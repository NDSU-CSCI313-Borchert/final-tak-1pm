import unittest

from board import *

class test_Board(unittest.TestCase):
    def test_5x5_brown_board_can_be_created(self):
        size = "5x5"
        design = "Brown"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_4x4_brown_board_can_be_created(self):
        size = "4x4"
        design = "Brown"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_3x3_brown_board_can_be_created(self):
        size = "3x3"
        design = "Brown"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
     def test_5x5_space_board_can_be_created(self):
        size = "5x5"
        design = "Space"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_4x4_space_board_can_be_created(self):
        size = "4x4"
        design = "Space"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_3x3_space_board_can_be_created(self):
        size = "3x3"
        design = "Space"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_5x5_yellow_board_can_be_created(self):
        size = "5x5"
        design = "Yellow"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_4x4_yellow_board_can_be_created(self):
        size = "4x4"
        design = "Yellow"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_3x3_yellow_board_can_be_created(self):
        size = "3x3"
        design = "Yellow"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_5x5_summer_board_can_be_created(self):
        size = "5x5"
        design = "Summerbreeze"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_4x4_summer_board_can_be_created(self):
        size = "4x4"
        design = "Summerbreeze"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
        
    def test_3x3_summer_board_can_be_created(self):
        size = "3x3"
        design = "Summerbreeze"
        board_type = str(size) + str(design)
        board = Board(board_type)
        self.assertTrue(True)
