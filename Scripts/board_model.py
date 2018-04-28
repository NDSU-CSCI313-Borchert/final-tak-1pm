import pygame
import pprint
from board import *
from constants import *

class BoardModel():
    def __init__(self,x,y, dimensions):
        super().__init__()

        self.coord_grid = []
        self.dimensions = int(dimensions[0])

        for x in range(self.dimensions):
            for y in range(self.dimensions):
                self.coord_grid.append(((SCREEN_WIDTH/4)+(151*x),(SCREEN_HEIGHT/6+(151*y))))

        self.grid2 = []

        self.markGrid = [['' for i in range(5)] for j in range(5)]
        
        self.handstack = []
        
        self.stack_0_0_model = []
        self.stack_0_1_model = []
        self.stack_0_2_model = []
        self.stack_0_3_model = []
        self.stack_0_4_model = []
        self.stack_1_0_model = []
        self.stack_1_1_model = []
        self.stack_1_2_model = []
        self.stack_1_3_model = []
        self.stack_1_4_model = []
        self.stack_2_0_model = []
        self.stack_2_1_model = []
        self.stack_2_2_model = []
        self.stack_2_3_model = []
        self.stack_2_4_model = []
        self.stack_3_0_model = []
        self.stack_3_1_model = []
        self.stack_3_2_model = []
        self.stack_3_3_model = []
        self.stack_3_4_model = []
        self.stack_4_0_model = []
        self.stack_4_1_model = []
        self.stack_4_2_model = []
        self.stack_4_3_model = []
        self.stack_4_4_model = []

    def get_grid(self):
        return self.grid
    
    def get_square(self, x, y):
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
        if x > 374 and x < 526 and y > 166 and y < 317:
            return "00"
        elif x > 374 and x < 526 and y > 316 and y < 467:
            return "10"
        elif x > 374 and x < 526 and y > 466 and y < 617:
            return "20"
        elif x > 374 and x < 526 and y > 616 and y < 767:
            return "30"
        elif x > 374 and x < 526 and y > 766 and y < 917:
            return "40"
        
        elif x > 526 and x < 677 and y > 166 and y < 317:
            return "01"
        elif x > 526 and x < 677 and y > 316 and y < 467:
            return "11"
        elif x > 526 and x < 677 and y > 466 and y < 617:
            return "21"
        elif x > 526 and x < 677 and y > 616 and y < 767:
            return "31"
        elif x > 526 and x < 677 and y > 766 and y < 917:
            return "41"
                
        elif x > 677 and x < 826 and y > 166 and y < 317:
            return "02"
        elif x > 677 and x < 826 and y > 316 and y < 467:
            return "12"
        elif x > 677 and x < 826 and y > 466 and y < 617:
            return "22"
        elif x > 677 and x < 826 and y > 616 and y < 767:
            return "32"
        elif x > 677 and x < 826 and y > 766 and y < 917:
            return "42"
        
        elif x > 826 and x < 978 and y > 166 and y < 317:
            return "03"
        elif x > 826 and x < 978 and y > 316 and y < 467:
            return "13"
        elif x > 826 and x < 978 and y > 466 and y < 617:
            return "23"
        elif x > 826 and x < 978 and y > 616 and y < 767:
            return "33"
        elif x > 826 and x < 978 and y > 766 and y < 917:
            return "43"
        
        elif x > 977 and x < 1129 and y > 166 and y < 317:
            return "04"
        elif x > 977 and x < 1129 and y > 316 and y < 467:
            return "14"
        elif x > 977 and x < 1129 and y > 466 and y < 617:
            return "24"
        elif x > 977 and x < 1129 and y > 616 and y < 767:
            return "34"
        elif x > 977 and x < 1129 and y > 766 and y < 917:
            return "44"

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
#xposition, ypositon, then if it is player1 make it true


    def pickup(self, posx,posy):
        if posx > 374 and posx < 526 and posy > 166 and posy < 317:
            if self.markGrid[0][0]!=(''):
                self.handstack.append(self.markGrid[0][0])
                self.markGrid[0][0]=self.stack.pop()
            # The first column
        elif posx > 374 and posx < 526 and posy > 316 and posy < 467:
            if self.markGrid[1][0]!=(''):
                self.handstack.append(self.markGrid[1][0])
                self.markGrid[1][0] = self.stack2.pop()
        elif posx > 374 and posx < 526 and posy > 467 and posy < 619:
            if self.markGrid[2][0]!=(''):
                self.handstack.append(self.markGrid[2][0])
                self.markGrid[2][0] = self.stack3.pop()
        elif posx > 374 and posx < 526 and posy > 618 and posy < 771:
            if self.markGrid[3][0]!=(''):
                self.handstack.append(self.markGrid[3][0])
                self.markGrid[3][0] = self.stack4.pop()
        elif posx > 374 and posx < 526 and posy > 770 and posy < 921:
            if self.markGrid[4][0]!=(''):
                self.handstack.append(self.markGrid[4][0])
                self.markGrid[4][0] = self.stack5.pop()
            # The first row
        elif posx > 526 and posx < 677 and posy > 166 and posy < 317:
            if self.markGrid[0][1]!=(''):
                self.handstack.append(self.markGrid[0][1])
                self.markGrid[0][1] = self.stack6.pop()
            # The second column
        elif posx > 526 and posx < 677 and posy > 316 and posy < 468:
            if self.markGrid[1][1]!=(''):
                self.handstack.append(self.markGrid[1][1])
                self.markGrid[1][1] = self.stack7.pop()
        elif posx > 526 and posx < 677 and posy > 467 and posy < 619:
            if self.markGrid[2][1]!=(''):
                self.handstack.append(self.markGrid[2][1])
                self.markGrid[2][1] = self.stack8.pop()
        elif posx > 526 and posx < 677 and posy > 618 and posy < 771:
            if self.markGrid[3][1]!=(''):
                self.handstack.append(self.markGrid[3][1])
                self.markGrid[3][1] = self.stack9.pop()
        elif posx > 526 and posx < 677 and posy > 770 and posy < 921:
            if self.markGrid[4][1]!=(''):
                self.handstack.append(self.markGrid[4][1])
                self.markGrid[4][1] = self.stack10.pop()

            # Third Column
        elif posx > 677 and posx < 826 and posy > 166 and posy < 317:
            if self.markGrid[0][2]!=(''):
                self.handstack.append(self.markGrid[0][2])
                self.markGrid[0][2] = self.stack11.pop()
        elif posx > 677 and posx < 826 and posy > 316 and posy < 468:
            if self.markGrid[1][2]!=(''):
                self.handstack.append(self.markGrid[1][2])
                self.markGrid[1][2] = self.stack12.pop()
        elif posx > 677 and posx < 826 and posy > 467 and posy < 619:
            if self.markGrid[2][2]!=(''):
                self.handstack.append(self.markGrid[2][2])
                self.markGrid[2][2] = self.stack13.pop()
        elif posx > 677 and posx < 826 and posy > 618 and posy < 771:
            if self.markGrid[3][2]!=(''):
                self.handstack.append(self.markGrid[3][2])
                self.markGrid[3][2] = self.stack14.pop()
        elif posx > 677 and posx < 826 and posy > 770 and posy < 921:
            if self.markGrid[4][2]!=(''):
                self.handstack.append(self.markGrid[4][2])
                self.markGrid[4][2] = self.stack15.pop()
            # fourth coloumn
        elif posx > 826 and posx < 978 and posy > 166 and posy < 317:
            if self.markGrid[0][3]!=(''):
                self.handstack.append(self.markGrid[0][3])
                self.markGrid[0][3] = self.stack16.pop()
        elif posx > 826 and posx < 978 and posy > 316 and posy < 468:
            if self.markGrid[1][3]!=(''):
                self.handstack.append(self.markGrid[1][3])
                self.markGrid[1][3] = self.stack17.pop()
        elif posx > 826 and posx < 978 and posy > 467 and posy < 619:
            if self.markGrid[2][3]!=(''):
                self.handstack.append(self.markGrid[2][3])
                self.markGrid[2][3] = self.stack18.pop()
        elif posx > 826 and posx < 978 and posy > 618 and posy < 771:
            if self.markGrid[3][3]!=(''):
                self.handstack.append(self.markGrid[3][3])
                self.markGrid[3][3] = self.stack19.pop()
        elif posx > 826 and posx < 978 and posy > 770 and posy < 921:
            if self.markGrid[4][3]!=(''):
                self.handstack.append(self.markGrid[4][3])
                self.markGrid[4][3] = self.stack20.pop()
            # fifth coloumn
        elif posx > 977 and posx < 1129 and posy > 166 and posy < 317:
            if self.markGrid[0][4]!=(''):
                self.handstack.append(self.markGrid[0][4])
                self.markGrid[0][4] = self.stack21.pop()
        elif posx > 977 and posx < 1129 and posy > 316 and posy < 468:
            if self.markGrid[1][4]!=(''):
                self.handstack.append(self.markGrid[1][4])
            self.markGrid[1][4] = self.stack22.pop()
        elif posx > 977 and posx < 1129 and posy > 467 and posy < 619:
            if self.markGrid[2][4]!=(''):
                self.handstack.append(self.markGrid[2][4])
                self.markGrid[2][4] = self.stack23.pop()
        elif posx > 977 and posx < 1129 and posy > 618 and posy < 771:
            if self.markGrid[3][4]!=(''):
                self.handstack.append(self.markGrid[3][4])
                self.markGrid[3][4] = self.stack24.pop()
        elif posx > 977 and posx < 1129 and posy > 770 and posy < 921:
            if self.markGrid[4][4]!=(''):
                self.handstack.append(self.markGrid[4][4])
                self.markGrid[4][4] = self.stack25.pop()



    def flatten_stone(self,posx,posy,b):
        if b == True:
            mark = 'X'
        else:
            mark = 'Y'
        if posx > 374 and posx < 526 and posy > 166 and posy < 317:
            self.markGrid[0][0] = mark
            # The first column
        elif posx > 374 and posx < 526 and posy > 316 and posy < 467:
            self.markGrid[1][0] = mark
        elif posx > 374 and posx < 526 and posy > 467 and posy < 619:
            self.markGrid[2][0] = mark
        elif posx > 374 and posx < 526 and posy > 618 and posy < 771:
            self.markGrid[3][0] = mark
        elif posx > 374 and posx < 526 and posy > 770 and posy < 921:
            self.markGrid[4][0] = mark
            # The first row
        elif posx > 526 and posx < 677 and posy > 166 and posy < 317:
            self.markGrid[0][1] = mark
            # The second column
        elif posx > 526 and posx < 677 and posy > 316 and posy < 468:
            self.markGrid[1][1] = mark
        elif posx > 526 and posx < 677 and posy > 467 and posy < 619:
            self.markGrid[2][1] = mark
        elif posx > 526 and posx < 677 and posy > 618 and posy < 771:
            self.markGrid[3][1] = mark
        elif posx > 526 and posx < 677 and posy > 770 and posy < 921:
            self.markGrid[4][1] = mark

            # Third Column
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
            # fourth coloumn
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
            # fifth coloumn
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
            self.stack.append(self.markGrid[0][0])
            self.markGrid[0][0] = mark
        #The first column
        elif posx > 374 and posx < 526 and posy > 316 and posy < 467:
            self.stack2.append(self.markGrid[1][0])
            self.markGrid[1][0] = mark
        elif posx > 374 and posx < 526 and posy > 467 and posy < 619:
            self.stack3.append(self.markGrid[2][0])
            self.markGrid[2][0] = mark
        elif posx > 374 and posx < 526 and posy > 618 and posy < 771:
            self.stack4.append(self.markGrid[3][0])
            self.markGrid[3][0] = mark
        elif posx > 374 and posx < 526 and posy > 770 and posy < 921:
            self.stack5.append(self.markGrid[4][0])
            self.markGrid[4][0] = mark
        #The first row
        elif posx > 526 and posx < 677 and posy > 166 and posy < 317:
            self.stack6.append(self.markGrid[0][1])
            self.markGrid[0][1] = mark
        #The second column
        elif posx > 526 and posx < 677 and posy > 316 and posy < 468:
            self.stack7.append(self.markGrid[1][1])
            self.markGrid[1][1] = mark
        elif posx > 526 and posx < 677 and posy > 467 and posy < 619:
            self.stack8.append(self.markGrid[2][1])
            self.markGrid[2][1] = mark
        elif posx > 526 and posx < 677 and posy > 618 and posy < 771:
            self.stack9.append(self.markGrid[3][1])
            self.markGrid[3][1] = mark
        elif posx > 526 and posx < 677 and posy > 770 and posy < 921:
            self.stack10.append(self.markGrid[4][1])
            self.markGrid[4][1] = mark


        #Third Column
        elif posx > 677 and posx < 826 and posy > 166 and posy < 317:
            self.stack11.append(self.markGrid[0][2])
            self.markGrid[0][2] = mark
        elif posx > 677 and posx < 826 and posy > 316 and posy < 468:
            self.stack12.append(self.markGrid[1][2])
            self.markGrid[1][2] = mark
        elif posx > 677 and posx < 826 and posy > 467 and posy < 619:
            self.stack13.append(self.markGrid[2][2])
            self.markGrid[2][2] = mark
        elif posx > 677 and posx < 826 and posy > 618 and posy < 771:
            self.stack14.append(self.markGrid[3][2])
            self.markGrid[3][2] = mark
        elif posx > 677 and posx < 826 and posy > 770 and posy < 921:
            self.stack15.append(self.markGrid[4][2])
            self.markGrid[4][2] = mark
        #fourth coloumn
        elif posx > 826 and posx < 978 and posy > 166 and posy < 317:
            self.stack16.append(self.markGrid[0][3])
            self.markGrid[0][3] = mark
        elif posx > 826 and posx < 978 and posy > 316 and posy < 468:
            self.stack17.append(self.markGrid[1][3])
            self.markGrid[1][3] = mark
        elif posx > 826 and posx < 978 and posy > 467 and posy < 619:
            self.stack18.append(self.markGrid[2][3])
            self.markGrid[2][3] = mark
        elif posx > 826 and posx < 978 and posy > 618 and posy < 771:
            self.stack19.append(self.markGrid[3][3])
            self.markGrid[3][3] = mark
        elif posx > 826 and posx < 978 and posy > 770 and posy < 921:
            self.stack20.append(self.markGrid[4][3])
            self.markGrid[4][3] = mark
        #fifth coloumn
        elif posx > 977 and posx < 1129 and posy > 166 and posy < 317:
            self.stack21.append(self.markGrid[0][4])
            self.markGrid[0][4] = mark
        elif posx > 977 and posx < 1129 and posy > 316 and posy < 468:
            self.stack22.append(self.markGrid[1][4])
            self.markGrid[1][4] = mark
        elif posx > 977 and posx < 1129 and posy > 467 and posy < 619:
            self.stack23.append(self.markGrid[2][4])
            self.markGrid[2][4] = mark
        elif posx > 977 and posx < 1129 and posy > 618 and posy < 771:
            self.stack24.append(self.markGrid[3][4])
            self.markGrid[3][4] = mark
        elif posx > 977 and posx < 1129 and posy > 770 and posy < 921:
            self.stack25.append(self.markGrid[4][4])
            self.markGrid[4][4] = mark
        pprint.pprint(self.markGrid)

    #Feed this method an x and y coordinate for it to check if that spot is occupied
    def spot_occupied(self,posx,posy):

        if posx > 374 and posx < 526 and posy > 166 and posy < 317:
            if self.markGrid[0][0] ==('Z') :
                return True
        #The first column
        elif posx > 374 and posx < 526 and posy > 316 and posy < 467:
            if self.markGrid[1][0]==('Z') :
                return True
        elif posx > 374 and posx < 526 and posy > 467 and posy < 619:
            if self.markGrid[2][0]==('Z') :
                return True
        elif posx > 374 and posx < 526 and posy > 618 and posy < 771:
            if self.markGrid[3][0]==('Z') :
                return True
        elif posx > 374 and posx < 526 and posy > 770 and posy < 921:
            if self.markGrid[4][0]==('Z') :
                return True
        #The first row
        elif posx > 526 and posx < 677 and posy > 166 and posy < 317:
            if self.markGrid[0][1]==('Z') :
                return True
        #The second column
        elif posx > 526 and posx < 677 and posy > 316 and posy < 468:
            if self.markGrid[1][1]==('Z') :
                return True
        elif posx > 526 and posx < 677 and posy > 467 and posy < 619:
            if self.markGrid[2][1]==('Z') :
                return True
        elif posx > 526 and posx < 677 and posy > 618 and posy < 771:
            if self.markGrid[3][1]==('Z') :
                return True
        elif posx > 526 and posx < 677 and posy > 770 and posy < 921:
            if self.markGrid[4][1]==('Z') :
                return True


        #Third Column
        elif posx > 677 and posx < 826 and posy > 166 and posy < 317:
            if self.markGrid[0][2]==('Z') :
                return True
        elif posx > 677 and posx < 826 and posy > 316 and posy < 468:
            if self.markGrid[1][2]==('Z') :
                return True
        elif posx > 677 and posx < 826 and posy > 467 and posy < 619:
            if self.markGrid[2][2]==('Z') :
                return True
        elif posx > 677 and posx < 826 and posy > 618 and posy < 771:
            if self.markGrid[3][2]==('Z') :
                return True
        elif posx > 677 and posx < 826 and posy > 770 and posy < 921:
            if self.markGrid[4][2]==('Z') :
                return True
        #fourth coloumn
        elif posx > 826 and posx < 978 and posy > 166 and posy < 317:
            if self.markGrid[0][3]==('Z') :
                return True
        elif posx > 826 and posx < 978 and posy > 316 and posy < 468:
            if self.markGrid[1][3]==('Z') :
                return True
        elif posx > 826 and posx < 978 and posy > 467 and posy < 619:
            if self.markGrid[2][3]==('Z') :
                return True
        elif posx > 826 and posx < 978 and posy > 618 and posy < 771:
            if self.markGrid[3][3]==('Z') :
                return True
        elif posx > 826 and posx < 978 and posy > 770 and posy < 921:
            if self.markGrid[4][3]==('Z') :
                return True
        #fifth coloumn
        elif posx > 977 and posx < 1129 and posy > 166 and posy < 317:
            if self.markGrid[0][4]==('Z') :
                return True
        elif posx > 977 and posx < 1129 and posy > 316 and posy < 468:
            if self.markGrid[1][4]==('Z') :
                return True
        elif posx > 977 and posx < 1129 and posy > 467 and posy < 619:
            if self.markGrid[2][4]==('Z') :
                return True
        elif posx > 977 and posx < 1129 and posy > 618 and posy < 771:
            if self.markGrid[3][4]==('Z') :
                return True
        elif posx > 977 and posx < 1129 and posy > 770 and posy < 921:
            if self.markGrid[4][4]==('Z') :
                return True

