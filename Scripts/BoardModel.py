import pygame
from board import *

class BoardModel():
    def __init__(self,x):
        super().__init__()
        self.grid = []
        for row in range(x):
            self.grid.append([])
            for column in range(x):
                self.grid[row].append(0)
    def get_grid(self):
        return self.grid
    def Check_victory(self, board):
        for x in range(0, 4):
            if board[x][0] == ('X') and board[x][1] == ('X') and board[x][2] == ('X') and board[x][3] == ('X') and \
                    board[x][4] == ('X'):
                return True
            if board[x][0] == ('Y') and board[x][1] == ('Y') and board[x][2] == ('Y') and board[x][3] == ('Y') and \
                    board[x][4] == ('Y'):
                return True
        for y in range(0, 4):
            if board[0][y] == ('X') and board[1][y] == ('X') and board[2][y] == ('X') and board[3][y] == ('X') and \
                    board[4][y] == ('X'):
                return True
            if board[0][y] == ('Y') and board[1][y] == ('Y') and board[2][y] == ('Y') and board[3][y] == ('Y') and board[4][y] == ('Y'):
                return True

        return False
    def Mark_spot(self,posx,posy,b):
        if b==True:
            mark='X'
        else:
            mark ='Y'
        if posx> 374 and posx< 526 and posy> 166 and posy< 317:
            self.grid[0][0] = mark
        if posx> 526 and posx< 677 and posy> 166 and posy< 317:
            self.grid[0][0] = mark
