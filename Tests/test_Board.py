import unittest
from Scripts.board import *

class test_Board(unittest.TestCase):
    def test_Board_can_be_created(self):
        board = Board("5x5")
        self.assertTrue(True)

    if __name__ == '__main__':
        unittest.main()
