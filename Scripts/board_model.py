import pygame
import pprint
from board import *
from constants import *

class BoardModel():
    def __init__(self,x,y):
        super().__init__()

        self.coord_grid = []
        for x in range(5):
            for y in range(5):
                self.coord_grid.append(((SCREEN_WIDTH/4)+(151*x),(SCREEN_HEIGHT/6+(151*y))))

        self.grid2 = []

        self.markGrid = [['' for i in range(5)] for j in range(5)]

    def get_grid(self):
        return self.grid




    def Check_victoryX(self):
        h_victory = False
        v_victory = False
        my_list =[]
        my_listy =[]

        # Vertical check
        for y in range(0,5):
            if self.markGrid[0][y]==('X'):
                if self.markGrid[1][y] == 'X' and self.markGrid[2][y] == 'X' and self.markGrid[3][y] == 'X' and self.markGrid[4][y] == 'X':
                    v_victory = True
                    break

        # Horizontal check
        for x in range(0,5):
            if self.markGrid[x][0] == 'X':
                if self.markGrid[x][1] == 'X' and self.markGrid[x][2] == 'X' and self.markGrid[x][3] == 'X' and self.markGrid[x][4] == 'X':
                    h_victory = True
                    break

        if v_victory or h_victory:
            return True
        else:
            return False


    def Check_victoryY(self):
        h_victory = False
        v_victory = False
        my_list = []
        my_listy = []

        # Vertical check
        for y in range(0, 5):
            if self.markGrid[0][y] == ('Y'):
                if self.markGrid[1][y]  == 'Y' and self.markGrid[2][y]  == 'Y' and self.markGrid[3][y] == 'Y' and self.markGrid[4][y] == 'Y':
                    v_victory = True
                    break

        # Horizontal check
        for x in range(0, 5):
            if self.markGrid[x][0] == 'Y':
                if self.markGrid[x][1] == 'Y' and self.markGrid[x][2] == 'Y' and self.markGrid[x][3] == 'Y' and self.markGrid[x][4] == 'Y':
                    h_victory = True
                    break

        if v_victory or h_victory:
            return True
        else:
            return False

    # pos x from the mouse, position y from the mouse, a boolean stating weather or not it is player1, then if the stone is a standing stone.
    def Mark_spot(self, posx, posy, b,standingStone):
        if b == True:
            mark = 'X'
        else:
            mark = 'Y'
        if standingStone == True:
            mark = 'Z'
        if posx > 374 and posx < 526 and posy > 166 and posy < 317:
            self.markGrid[0][0] = mark
        #The first column
        elif posx > 374 and posx < 526 and posy > 316 and posy < 467:
            self.markGrid[1][0] = mark
        elif posx > 374 and posx < 526 and posy > 467 and posy < 619:
            self.markGrid[2][0] = mark
        elif posx > 374 and posx < 526 and posy > 618 and posy < 771:
            self.markGrid[3][0] = mark
        elif posx > 374 and posx < 526 and posy > 770 and posy < 921:
            self.markGrid[4][0] = mark
        #The first row
        elif posx > 526 and posx < 677 and posy > 166 and posy < 317:
            self.markGrid[0][1] = mark
        #The second column
        elif posx > 526 and posx < 677 and posy > 316 and posy < 468:
            self.markGrid[1][1] = mark
        elif posx > 526 and posx < 677 and posy > 467 and posy < 619:
            self.markGrid[2][1] = mark
        elif posx > 526 and posx < 677 and posy > 618 and posy < 771:
            self.markGrid[3][1] = mark
        elif posx > 526 and posx < 677 and posy > 770 and posy < 921:
            self.markGrid[4][1] = mark


        #Third Column
        elif posx > 677 and posx < 826 and posy > 166 and posy < 317:
            self.markGrid[0][2] = mark
        elif posx > 677 and posx < 826 and posy > 316 and posy < 468:
            self.markGrid[1][2] = mark
        elif posx > 677 and posx < 826 and posy > 467 and posy < 619:
            self.markGrid[2][2] = mark
        elif posx > 677 and posx < 826 and posy > 618 and posy < 771:
            self.markGrid[3][2] = mark
        elif posx > 677 and posx < 826 and posy > 770 and posy < 921:
            self.markGrid[4][2] = mark
        #fourth coloumn
        elif posx > 826 and posx < 978 and posy > 166 and posy < 317:
            self.markGrid[0][3] = mark
        elif posx > 826 and posx < 978 and posy > 316 and posy < 468:
            self.markGrid[1][3] = mark
        elif posx > 826 and posx < 978 and posy > 467 and posy < 619:
            self.markGrid[2][3] = mark
        elif posx > 826 and posx < 978 and posy > 618 and posy < 771:
            self.markGrid[3][3] = mark
        elif posx > 826 and posx < 978 and posy > 770 and posy < 921:
            self.markGrid[4][3] = mark
        #fifth coloumn
        elif posx > 977 and posx < 1129 and posy > 166 and posy < 317:
            self.markGrid[0][4] = mark
        elif posx > 977 and posx < 1129 and posy > 316 and posy < 468:
            self.markGrid[1][4] = mark
        elif posx > 977 and posx < 1129 and posy > 467 and posy < 619:
            self.markGrid[2][4] = mark
        elif posx > 977 and posx < 1129 and posy > 618 and posy < 771:
            self.markGrid[3][4] = mark
        elif posx > 977 and posx < 1129 and posy > 770 and posy < 921:
            self.markGrid[4][4] = mark
        pprint.pprint(self.markGrid)

    #Feed this method an x and y coordinate for it to check if that spot is occupied
    def spot_occupied(self,posx,posy):

        if posx > 374 and posx < 526 and posy > 166 and posy < 317:
            if self.markGrid[0][0] !=('') :
                return True
        #The first column
        elif posx > 374 and posx < 526 and posy > 316 and posy < 467:
            if self.markGrid[1][0]!=('') :
                return True
        elif posx > 374 and posx < 526 and posy > 467 and posy < 619:
            if self.markGrid[2][0]!=('') :
                return True
        elif posx > 374 and posx < 526 and posy > 618 and posy < 771:
            if self.markGrid[3][0]!=('') :
                return True
        elif posx > 374 and posx < 526 and posy > 770 and posy < 921:
            if self.markGrid[4][0]!=('') :
                return True
        #The first row
        elif posx > 526 and posx < 677 and posy > 166 and posy < 317:
            if self.markGrid[0][1]!=('') :
                return True
        #The second column
        elif posx > 526 and posx < 677 and posy > 316 and posy < 468:
            if self.markGrid[1][1]!=('') :
                return True
        elif posx > 526 and posx < 677 and posy > 467 and posy < 619:
            if self.markGrid[2][1]!=('') :
                return True
        elif posx > 526 and posx < 677 and posy > 618 and posy < 771:
            if self.markGrid[3][1]!=('') :
                return True
        elif posx > 526 and posx < 677 and posy > 770 and posy < 921:
            if self.markGrid[4][1]!=('') :
                return True


        #Third Column
        elif posx > 677 and posx < 826 and posy > 166 and posy < 317:
            if self.markGrid[0][2]!=('') :
                return True
        elif posx > 677 and posx < 826 and posy > 316 and posy < 468:
            if self.markGrid[1][2]!=('') :
                return True
        elif posx > 677 and posx < 826 and posy > 467 and posy < 619:
            if self.markGrid[2][2]!=('') :
                return True
        elif posx > 677 and posx < 826 and posy > 618 and posy < 771:
            if self.markGrid[3][2]!=('') :
                return True
        elif posx > 677 and posx < 826 and posy > 770 and posy < 921:
            if self.markGrid[4][2]!=('') :
                return True
        #fourth coloumn
        elif posx > 826 and posx < 978 and posy > 166 and posy < 317:
            if self.markGrid[0][3]!=('') :
                return True
        elif posx > 826 and posx < 978 and posy > 316 and posy < 468:
            if self.markGrid[1][3]!=('') :
                return True
        elif posx > 826 and posx < 978 and posy > 467 and posy < 619:
            if self.markGrid[2][3]!=('') :
                return True
        elif posx > 826 and posx < 978 and posy > 618 and posy < 771:
            if self.markGrid[3][3]!=('') :
                return True
        elif posx > 826 and posx < 978 and posy > 770 and posy < 921:
            if self.markGrid[4][3]!=('') :
                return True
        #fifth coloumn
        elif posx > 977 and posx < 1129 and posy > 166 and posy < 317:
            if self.markGrid[0][4]!=('') :
                return True
        elif posx > 977 and posx < 1129 and posy > 316 and posy < 468:
            if self.markGrid[1][4]!=('') :
                return True
        elif posx > 977 and posx < 1129 and posy > 467 and posy < 619:
            if self.markGrid[2][4]!=('') :
                return True
        elif posx > 977 and posx < 1129 and posy > 618 and posy < 771:
            if self.markGrid[3][4]!=('') :
                return True
        elif posx > 977 and posx < 1129 and posy > 770 and posy < 921:
            if self.markGrid[4][4]!=('') :
                return True

