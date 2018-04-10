import pygame
from board import *
from constants import *

class BoardModel():
    def __init__(self,x,y):
        super().__init__()
        # self.grid = [[((SCREEN_WIDTH/4)+(151*i),(SCREEN_HEIGHT/6+(151*j))) for i in range(5)] for j in range(5)]
        # print('\n'.join([''.join(['{0}'.format(item) for item in row]) for row in self.grid]))

        self.grid = []
        for x in range(5):
            for y in range(5):
                self.grid.append(((SCREEN_WIDTH/4)+(151*x),(SCREEN_HEIGHT/6+(151*y))))

        print(self.grid)

    def get_grid(self):
        return self.grid

    def check_victory(self, board):
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

    def mark_spot(self,pos,b):
        if b==True:
            mark='X'
        else:
            mark ='Y'