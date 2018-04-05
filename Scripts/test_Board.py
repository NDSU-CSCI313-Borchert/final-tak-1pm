
from board import *

def test_board_can_be_created():
    board = Board("5x5")
    board.rect.x =120
    board.rect.y =120
    assert test_board_can_be_created(True) == True