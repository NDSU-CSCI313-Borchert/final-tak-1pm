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
        self.grid2 = []

    def get_grid(self):
        return self.grid




    def Check_victory(self, board):

        for x in range(0, 4):
            if board[x][0] == ('X'):
                current_spot = board[x][0]
                self.grid2 = current_spot
                break
                #I need a little help with logic, am i able to use current spot to check the spot next to it like current_spot[x][y+1]
        if board[x + 1][0] == ('X'):
            current_spot = board[x+1][0]
            self.grid2[2] = current_spot
            if board[x + 2][0] == ('X'):
                current_spot = board[x + 2][0]
                self.grid2[3] = current_spot

            if board[x + 1][1] == ('X'):
                    current_spot = board[x + 1][1]
                    self.grid2[3] = current_spot


        if board[x][0+1] == ('X'):
            current_spot = board[x][0+1]
            self.grid2[2] = current_spot


        if board[x - 1][0] == ('X'):
            current_spot= board[x-1][0]
            self.grid2[3] = current_spot




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
            if board[0][y] == ('Y') and board[1][y] == ('Y') and board[2][y] == ('Y') and board[3][y] == ('Y') and \
                    board[4][y] == ('Y'):
                return True

        return False

    def Mark_spot(self, posx, posy, b):
        if b == True:
            mark = 'X'
        else:
            mark = 'Y'
        if posx > 374 and posx < 526 and posy > 166 and posy < 317:
            self.grid[0][0] = mark
        #The first column
        if posx > 374 and posx < 526 and posy > 316 and posy < 467:
            self.grid[1][0] = mark
        if posx > 374 and posx < 526 and posy > 467 and posy < 619:
            self.grid[2][0] = mark
        if posx > 374 and posx < 526 and posy > 618 and posy < 771:
            self.grid[3][0] = mark
        if posx > 374 and posx < 526 and posy > 770 and posy < 921:
            self.grid[4][0] = mark
        #The first row
        if posx > 526 and posx < 677 and posy > 166 and posy < 317:
            self.grid[0][1] = mark
        #The second column
        if posx > 526 and posx < 677 and posy > 316 and posy < 468:
            self.grid[1][1] = mark
        if posx > 526 and posx < 677 and posy > 467 and posy < 619:
            self.grid[2][1] = mark
        if posx > 526 and posx < 677 and posy > 618 and posy < 771:
            self.grid[3][1] = mark
        if posx > 526 and posx < 677 and posy > 770 and posy < 921:
            self.grid[4][1] = mark


        #Third Column
        if posx > 677 and posx < 826 and posy > 166 and posy < 317:
            self.grid[0][2] = mark
        if posx > 677 and posx < 826 and posy > 316 and posy < 468:
            self.grid[1][2] = mark
        if posx > 677 and posx < 826 and posy > 467 and posy < 619:
            self.grid[2][2] = mark
        if posx > 677 and posx < 826 and posy > 618 and posy < 771:
            self.grid[3][2] = mark
        if posx > 677 and posx < 826 and posy > 770 and posy < 921:
            self.grid[4][2] = mark
        #fourth coloumn
        if posx > 826 and posx < 978 and posy > 166 and posy < 317:
            self.grid[0][3] = mark
        if posx > 826 and posx < 978 and posy > 316 and posy < 468:
            self.grid[1][2] = mark
        if posx > 826 and posx < 978 and posy > 467 and posy < 619:
            self.grid[2][2] = mark
        if posx > 826 and posx < 978 and posy > 618 and posy < 771:
            self.grid[3][2] = mark
        if posx > 826 and posx < 978 and posy > 770 and posy < 921:
            self.grid[4][2] = mark
        #fifth coloumn
        if posx > 977 and posx < 1129 and posy > 166 and posy < 317:
            self.grid[0][4] = mark
        if posx > 977 and posx < 1129 and posy > 316 and posy < 468:
            self.grid[1][2] = mark
        if posx > 977 and posx < 1129 and posy > 467 and posy < 619:
            self.grid[2][2] = mark
        if posx > 977 and posx < 1129 and posy > 618 and posy < 771:
            self.grid[3][2] = mark
        if posx > 977 and posx < 1129 and posy > 770 and posy < 921:
            self.grid[4][2] = mark