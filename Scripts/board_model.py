import pygame
import pprint
from board import *
from constants import *

class BoardModel():
    def __init__(self, pos, dimensions):
        super().__init__()

        self.coord_grid = []
        self.dimensions = int(dimensions[0])

        self.pos = pos

        for x in range(self.dimensions):
            for y in range(self.dimensions):
                self.coord_grid.append(((pos[0])+(151*x),(pos[1]+(151*y))))

        self.grid2 = []

        self.markGrid = [['' for i in range(5)] for j in range(5)]
        self.capstoneSpots = [['' for i in range (self.dimensions)] for j in range (self.dimensions)]
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

        else:
            return ""

    def get_adjacent_squares(self, current_position):
        
        position = current_position
        
        #returns clockwise array of adjacent grid spaces
        if position == "00":
            return ["01", "10"]
        elif position == "10":
            return ["00", "11", "20"]
        elif position == "20":
            return ["10", "21", "30"]
        elif position == "30":
            return ["20", "31", "40"]
        elif position == "40":
            return ["30", "41"]

        elif position == "01":
            return ["02","11","00"]
        elif position == "11":
            return ["01","12","21", "10"]
        elif position == "21":
            return ["11","22","31", "20"]
        elif position == "31":
            return ["21","32","41", "30"]
        elif position == "41":
            return ["31","42","40"]
        
        elif position == "02":
            return ["03","12","01"]
        elif position == "12":
            return ["02","13","22", "11"]
        elif position == "22":
            return ["12","23","32", "21"]
        elif position == "32":
            return ["22","33","42", "31"]
        elif position == "42":
            return ["32","43","41"]

        elif position == "03":
            return ["04","13","02"]
        elif position == "13":
            return ["03","14","23", "12"]
        elif position == "23":
            return ["13","24","33", "22"]
        elif position == "33":
            return ["23","34","43", "32"]
        elif position == "43":
            return ["33","44","42"]
        
        elif position == "04":
            return ["14", "03"]
        elif position == "14":
            return ["04", "24", "13"]
        elif position == "24":
            return ["14", "34", "23"]
        elif position == "34":
            return ["24", "44", "33"]
        elif position == "44":
            return ["34", "43"]

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

# if the spot is not equal to empty, append what is in that spot to the handstack, and make the mark on the board,
    #be what the old piece was
    def pickup(self, posx,posy):
        
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
        
        position = self.get_square(posx, posy)
        
        if position == "00":
            if self.markGrid[0][0]!=(''):
                self.handstack.append(self.markGrid[0][0])
                self.markGrid[0][0]=self.stack.pop()
        elif position == "10":
            if self.markGrid[1][0]!=(''):
                self.handstack.append(self.markGrid[1][0])
                self.markGrid[1][0] = self.stack2.pop()
        elif position == "20":
            if self.markGrid[2][0]!=(''):
                self.handstack.append(self.markGrid[2][0])
                self.markGrid[2][0] = self.stack3.pop()
        elif position == "30":
            if self.markGrid[3][0]!=(''):
                self.handstack.append(self.markGrid[3][0])
                self.markGrid[3][0] = self.stack4.pop()
        elif position == "40":
            if self.markGrid[4][0]!=(''):
                self.handstack.append(self.markGrid[4][0])
                self.markGrid[4][0] = self.stack5.pop()

        elif position == "01":
            if self.markGrid[0][1]!=(''):
                self.handstack.append(self.markGrid[0][1])
                self.markGrid[0][1] = self.stack6.pop()
        elif position == "11":
            if self.markGrid[1][1]!=(''):
                self.handstack.append(self.markGrid[1][1])
                self.markGrid[1][1] = self.stack7.pop()
        elif position == "21":
            if self.markGrid[2][1]!=(''):
                self.handstack.append(self.markGrid[2][1])
                self.markGrid[2][1] = self.stack8.pop()
        elif position == "31":
            if self.markGrid[3][1]!=(''):
                self.handstack.append(self.markGrid[3][1])
                self.markGrid[3][1] = self.stack9.pop()
        elif position == "41":
            if self.markGrid[4][1]!=(''):
                self.handstack.append(self.markGrid[4][1])
                self.markGrid[4][1] = self.stack10.pop()

        elif position == "02":
            if self.markGrid[0][2]!=(''):
                self.handstack.append(self.markGrid[0][2])
                self.markGrid[0][2] = self.stack11.pop()
        elif position == "12":
            if self.markGrid[1][2]!=(''):
                self.handstack.append(self.markGrid[1][2])
                self.markGrid[1][2] = self.stack12.pop()
        elif position == "22":
            if self.markGrid[2][2]!=(''):
                self.handstack.append(self.markGrid[2][2])
                self.markGrid[2][2] = self.stack13.pop()
        elif position == "32":
            if self.markGrid[3][2]!=(''):
                self.handstack.append(self.markGrid[3][2])
                self.markGrid[3][2] = self.stack14.pop()
        elif position == "42":
            if self.markGrid[4][2]!=(''):
                self.handstack.append(self.markGrid[4][2])
                self.markGrid[4][2] = self.stack15.pop()

        elif position == "03":
            if self.markGrid[0][3]!=(''):
                self.handstack.append(self.markGrid[0][3])
                self.markGrid[0][3] = self.stack16.pop()
        elif position == "13":
            if self.markGrid[1][3]!=(''):
                self.handstack.append(self.markGrid[1][3])
                self.markGrid[1][3] = self.stack17.pop()
        elif position == "23":
            if self.markGrid[2][3]!=(''):
                self.handstack.append(self.markGrid[2][3])
                self.markGrid[2][3] = self.stack18.pop()
        elif position == "33":
            if self.markGrid[3][3]!=(''):
                self.handstack.append(self.markGrid[3][3])
                self.markGrid[3][3] = self.stack19.pop()
        elif position == "43":
            if self.markGrid[4][3]!=(''):
                self.handstack.append(self.markGrid[4][3])
                self.markGrid[4][3] = self.stack20.pop()

        elif position == "04":
            if self.markGrid[0][4]!=(''):
                self.handstack.append(self.markGrid[0][4])
                self.markGrid[0][4] = self.stack21.pop()
        elif position == "14":
            if self.markGrid[1][4]!=(''):
                self.handstack.append(self.markGrid[1][4])
            self.markGrid[1][4] = self.stack22.pop()
        elif position == "24":
            if self.markGrid[2][4]!=(''):
                self.handstack.append(self.markGrid[2][4])
                self.markGrid[2][4] = self.stack23.pop()
        elif position == "34":
            if self.markGrid[3][4]!=(''):
                self.handstack.append(self.markGrid[3][4])
                self.markGrid[3][4] = self.stack24.pop()
        elif position == "44":
            if self.markGrid[4][4]!=(''):
                self.handstack.append(self.markGrid[4][4])
                self.markGrid[4][4] = self.stack25.pop()

    def putdown(self,posx,posy):
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

        position = self.get_square(posx, posy)

        if position == "00":
            self.markGrid[0][0]=self.handstack.pop()

        elif position == "10":
            self.markGrid[1][0] = self.handstack.pop()
        elif position == "20":
            self.markGrid[2][0] = self.handstack.pop()
        elif position == "30":
            self.markGrid[3][0] = self.handstack.pop()
        elif position == "40":
            self.markGrid[4][0] = self.handstack.pop()

        elif position == "01":
            self.markGrid[0][1] = self.handstack.pop()
        elif position == "11":
            self.markGrid[1][1] = self.handstack.pop()
        elif position == "21":
            self.markGrid[2][1] = self.handstack.pop()
        elif position == "31":
            self.markGrid[3][1] = self.handstack.pop()
        elif position == "41":
            self.markGrid[4][1] = self.handstack.pop()

        elif position == "02":
            self.markGrid[0][2] = self.handstack.pop()
        elif position == "12":
            self.markGrid[1][2] = self.handstack.pop()
        elif position == "22":
            self.markGrid[2][2] = self.handstack.pop()
        elif position == "32":
            self.markGrid[3][2] = self.handstack.pop()
        elif position == "42":
            self.markGrid[4][2] = self.handstack.pop()

        elif position == "03":
            self.markGrid[0][3] = self.handstack.pop()
        elif position == "13":
            self.markGrid[1][3] = self.handstack.pop()
        elif position == "23":
            self.markGrid[2][3] = self.handstack.pop()
        elif position == "33":
            self.markGrid[3][3] = self.handstack.pop()
        elif position == "43":
            self.markGrid[4][3] = self.handstack.pop()

        elif position == "04":
            self.markGrid[0][4] = self.handstack.pop()
        elif position == "14":
            self.markGrid[1][4] = self.handstack.pop()
        elif position == "24":
            self.markGrid[2][4] = self.handstack.pop()
        elif position == "34":
            self.markGrid[3][4] = self.handstack.pop()
        elif position == "44":
            self.markGrid[4][4] = self.handstack.pop()

    def get_item_in_block(self,posx,posy):
        position = self.get_square(posx, posy)

        if position == "00":
            return self.markGrid[0][0]

        elif position == "10":
            return self.markGrid[1][0]
        elif position == "20":
            return self.markGrid[2][0]
        elif position == "30":
            return self.markGrid[3][0]
        elif position == "40":
            return self.markGrid[4][0]

        elif position == "01":
            return self.markGrid[0][1]
        elif position == "11":
            return self.markGrid[1][1]
        elif position == "21":
            return self.markGrid[2][1]
        elif position == "31":
            return self.markGrid[3][1]
        elif position == "41":
            return self.markGrid[4][1]

        elif position == "02":
            return self.markGrid[0][2]
        elif position == "12":
            return self.markGrid[1][2]
        elif position == "22":
            return self.markGrid[2][2]
        elif position == "32":
            return self.markGrid[3][2]
        elif position == "42":
            return self.markGrid[4][2]

        elif position == "03":
            return self.markGrid[0][3]
        elif position == "13":
            return self.markGrid[1][3]
        elif position == "23":
            return self.markGrid[2][3]
        elif position == "33":
            return self.markGrid[3][3]
        elif position == "43":
            return self.markGrid[4][3]

        elif position == "04":
            return self.markGrid[0][4]
        elif position == "14":
            return self.markGrid[1][4]
        elif position == "24":
            return self.markGrid[2][4]
        elif position == "34":
            return self.markGrid[3][4]
        elif position == "44":
            return self.markGrid[4][4]
    def flatten_stone(self,posx,posy,b):
        
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
        
        position = self.get_square(posx, posy)
        
        if b == True:
            mark = 'X'
        else:
            mark = 'Y'
        
        if position == "00":
            self.markGrid[0][0] = mark
        elif position == "10":
            self.markGrid[1][0] = mark
        elif position == "20":
            self.markGrid[2][0] = mark
        elif position == "30":
            self.markGrid[3][0] = mark
        elif position == "40":
            self.markGrid[4][0] = mark

        elif position == "01":
            self.markGrid[0][1] = mark
        elif position == "11":
            self.markGrid[1][1] = mark
        elif position == "21":
            self.markGrid[2][1] = mark
        elif position == "31":
            self.markGrid[3][1] = mark
        elif position == "41":
            self.markGrid[4][1] = mark

        elif position == "02":
            self.markGrid[0][2] = mark
        elif position == "12":
            self.markGrid[1][2] = mark
        elif position == "22":
            self.markGrid[2][2] = mark
        elif position == "32":
            self.markGrid[3][2] = mark
        elif position == "42":
            self.markGrid[4][2] = mark

        elif position == "03":
            self.markGrid[0][3] = mark
        elif position == "13":
            self.markGrid[1][3] = mark
        elif position == "23":
            self.markGrid[2][3] = mark
        elif position == "33":
            self.markGrid[3][3] = mark
        elif position == "43":
            self.markGrid[4][3] = mark

        elif position == "04":
            self.markGrid[0][4] = mark
        elif position == "14":
            self.markGrid[1][4] = mark
        elif position == "24":
            self.markGrid[2][4] = mark
        elif position == "34":
            self.markGrid[3][4] = mark
        elif position == "44":
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
        position = self.get_square(posx, posy)
        
        if b == True:
            mark = 'X'
        else:
            mark = 'Y'
        if standingStone == True:
            mark = 'Z'
        
        if position == "00":
            self.stack_0_0_model.append(self.markGrid[0][0])
            self.markGrid[0][0] = mark
        elif position == "10":
            self.stack_1_0_model.append(self.markGrid[1][0])
            self.markGrid[1][0] = mark
        elif position == "20":
            self.stack_2_0_model.append(self.markGrid[2][0])
            self.markGrid[2][0] = mark
        elif position == "30":
            self.stack_3_0_model.append(self.markGrid[3][0])
            self.markGrid[3][0] = mark
        elif position == "40":
            self.stack_4_0_model.append(self.markGrid[4][0])
            self.markGrid[4][0] = mark

        elif position == "01":
            self.stack_0_1_model.append(self.markGrid[0][1])
            self.markGrid[0][1] = mark
        elif position == "11":
            self.stack_1_1_model.append(self.markGrid[1][1])
            self.markGrid[1][1] = mark
        elif position == "21":
            self.stack_2_1_model.append(self.markGrid[2][1])
            self.markGrid[2][1] = mark
        elif position == "31":
            self.stack_3_1_model.append(self.markGrid[3][1])
            self.markGrid[3][1] = mark
        elif position == "41":
            self.stack_4_1_model.append(self.markGrid[4][1])
            self.markGrid[4][1] = mark

        elif position == "02":
            self.stack_0_2_model.append(self.markGrid[0][2])
            self.markGrid[0][2] = mark
        elif position == "12":
            self.stack_1_2_model.append(self.markGrid[1][2])
            self.markGrid[1][2] = mark
        elif position == "22":
            self.stack_2_2_model.append(self.markGrid[2][2])
            self.markGrid[2][2] = mark
        elif position == "32":
            self.stack_3_2_model.append(self.markGrid[3][2])
            self.markGrid[3][2] = mark
        elif position == "42":
            self.stack_4_2_model.append(self.markGrid[4][2])
            self.markGrid[4][2] = mark

        elif position == "03":
            self.stack_0_3_model.append(self.markGrid[0][3])
            self.markGrid[0][3] = mark
        elif position == "13":
            self.stack_1_3_model.append(self.markGrid[1][3])
            self.markGrid[1][3] = mark
        elif position == "23":
            self.stack_2_3_model.append(self.markGrid[2][3])
            self.markGrid[2][3] = mark
        elif position == "33":
            self.stack_3_3_model.append(self.markGrid[3][3])
            self.markGrid[3][3] = mark
        elif position == "43":
            self.stack_4_3_model.append(self.markGrid[4][3])
            self.markGrid[4][3] = mark

        elif position == "04":
            self.stack_0_4_model.append(self.markGrid[0][4])
            self.markGrid[0][4] = mark
        elif position == "14":
            self.stack_1_4_model.append(self.markGrid[1][4])
            self.markGrid[1][4] = mark
        elif position == "24":
            self.stack_2_4_model.append(self.markGrid[2][4])
            self.markGrid[2][4] = mark
        elif position == "34":
            self.stack_3_4_model.append(self.markGrid[3][4])
            self.markGrid[3][4] = mark
        elif position == "44":
            self.stack_4_4_model.append(self.markGrid[4][4])
            self.markGrid[4][4] = mark
    #print.print(self.markGrid)
    #Trying something new I suppose, whenever a capstone is placed there is a second matrix where the info is stored to help fro when being picked up
    def mark_grid2(self,posx,posy,piece, color):
        b = False
        position = self.get_square(posx, posy)
        if piece =="flat" and color =="brown":
            mark ='X'
        elif piece =="flat" and color =="beige":
            mark ='Y'
        elif piece =="wall":
            mark ='Z'
        elif piece =="capstone" and color =="brown":
            mark='X'
            b=True
        if position == "00":
            self.stack_0_0_model.append(self.markGrid[0][0])
            self.markGrid[0][0] = mark
            if b ==True:
                self.capstoneSpots[0][0] = mark
        elif position == "10":
            self.stack_1_0_model.append(self.markGrid[1][0])
            self.markGrid[1][0] = mark
            if b ==True:
                self.capstoneSpots[1][0] = mark
        elif position == "20":
            self.stack_2_0_model.append(self.markGrid[2][0])
            self.markGrid[2][0] = mark
            if b ==True:
                self.capstoneSpots[2][0] = mark
        elif position == "30":
            self.stack_3_0_model.append(self.markGrid[3][0])
            self.markGrid[3][0] = mark
            if b ==True:
                self.capstoneSpots[3][0] = mark
        elif position == "40":
            self.stack_4_0_model.append(self.markGrid[4][0])
            self.markGrid[4][0] = mark
            if b ==True:
                self.capstoneSpots[4][0] = mark

        elif position == "01":
            self.stack_0_1_model.append(self.markGrid[0][1])
            self.markGrid[0][1] = mark
            if b ==True:
                self.capstoneSpots[0][1] = mark
        elif position == "11":
            self.stack_1_1_model.append(self.markGrid[1][1])
            self.markGrid[1][1] = mark
            if b ==True:
                self.capstoneSpots[1][1] = mark
        elif position == "21":
            self.stack_2_1_model.append(self.markGrid[2][1])
            self.markGrid[2][1] = mark
            if b ==True:
                self.capstoneSpots[2][1] = mark
        elif position == "31":
            self.stack_3_1_model.append(self.markGrid[3][1])
            self.markGrid[3][1] = mark
            if b ==True:
                self.capstoneSpots[3][1] = mark
        elif position == "41":
            self.stack_4_1_model.append(self.markGrid[4][1])
            self.markGrid[4][1] = mark
            if b ==True:
                self.capstoneSpots[4][1] = mark

        elif position == "02":
            self.stack_0_2_model.append(self.markGrid[0][2])
            self.markGrid[0][2] = mark
            if b ==True:
                self.capstoneSpots[0][2] = mark
        elif position == "12":
            self.stack_1_2_model.append(self.markGrid[1][2])
            self.markGrid[1][2] = mark
            if b ==True:
                self.capstoneSpots[1][2] = mark
        elif position == "22":
            self.stack_2_2_model.append(self.markGrid[2][2])
            self.markGrid[2][2] = mark
            if b ==True:
                self.capstoneSpots[2][2] = mark
        elif position == "32":
            self.stack_3_2_model.append(self.markGrid[3][2])
            self.markGrid[3][2] = mark
            if b ==True:
                self.capstoneSpots[3][2] = mark
        elif position == "42":
            self.stack_4_2_model.append(self.markGrid[4][2])
            self.markGrid[4][2] = mark
            if b ==True:
                self.capstoneSpots[4][2] = mark

        elif position == "03":
            self.stack_0_3_model.append(self.markGrid[0][3])
            self.markGrid[0][3] = mark
            if b ==True:
                self.capstoneSpots[0][3] = mark
        elif position == "13":
            self.stack_1_3_model.append(self.markGrid[1][3])
            self.markGrid[1][3] = mark
            if b ==True:
                self.capstoneSpots[1][3] = mark
        elif position == "23":
            self.stack_2_3_model.append(self.markGrid[2][3])
            self.markGrid[2][3] = mark
            if b ==True:
                self.capstoneSpots[2][3] = mark
        elif position == "33":
            self.stack_3_3_model.append(self.markGrid[3][3])
            self.markGrid[3][3] = mark
            if b ==True:
                self.capstoneSpots[3][3] = mark
        elif position == "43":
            self.stack_4_3_model.append(self.markGrid[4][3])
            self.markGrid[4][3] = mark
            if b ==True:
                self.capstoneSpots[4][3] = mark

        elif position == "04":
            self.stack_0_4_model.append(self.markGrid[0][4])
            self.markGrid[0][4] = mark
            if b ==True:
                self.capstoneSpots[0][4] = mark
        elif position == "14":
            self.stack_1_4_model.append(self.markGrid[1][4])
            self.markGrid[1][4] = mark
            if b ==True:
                self.capstoneSpots[1][4] = mark
        elif position == "24":
            self.stack_2_4_model.append(self.markGrid[2][4])
            self.markGrid[2][4] = mark
            if b ==True:
                self.capstoneSpots[2][4] = mark
        elif position == "34":
            self.stack_3_4_model.append(self.markGrid[3][4])
            self.markGrid[3][4] = mark
            if b ==True:
                self.capstoneSpots[3][4] = mark
        elif position == "44":
            self.stack_4_4_model.append(self.markGrid[4][4])
            self.markGrid[4][4] = mark
            if b ==True:
                self.capstoneSpots[4][4] = mark


    #Feed this method an x and y coordinate for it to check if that spot is occupied
    def spot_occupied(self,posx,posy):

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
        
        position = self.get_square(posx, posy)

        if position == "00":
            if self.markGrid[0][0] !=('') :
                return True
        elif position == "10":
            if self.markGrid[1][0]!=('') :
                return True
        elif position == "20":
            if self.markGrid[2][0]!=('') :
                return True
        elif position == "30":
            if self.markGrid[3][0]!=('') :
                return True
        elif position == "40":
            if self.markGrid[4][0]!=('') :
                return True

        elif position == "01":
            if self.markGrid[0][1]!=('') :
                return True
        elif position == "11":
            if self.markGrid[1][1]!=('') :
                return True
        elif position == "21":
            if self.markGrid[2][1]!=('') :
                return True
        elif position == "31":
            if self.markGrid[3][1]!=('') :
                return True
        elif position == "41":
            if self.markGrid[4][1]!=('') :
                return True

        elif position == "02":
            if self.markGrid[0][2]!=('') :
                return True
        elif position == "12":
            if self.markGrid[1][2]!=('') :
                return True
        elif position == "22":
            if self.markGrid[2][2]!=('') :
                return True
        elif position == "32":
            if self.markGrid[3][2]!=('') :
                return True
        elif position == "42":
            if self.markGrid[4][2]!=('') :
                return True

        elif position == "03":
            if self.markGrid[0][3]!=('') :
                return True
        elif position == "13":
            if self.markGrid[1][3]!=('') :
                return True
        elif position == "23":
            if self.markGrid[2][3]!=('') :
                return True
        elif position == "33":
            if self.markGrid[3][3]!=('') :
                return True
        elif position == "43":
            if self.markGrid[4][3]!=('') :
                return True

        elif position == "04":
            if self.markGrid[0][4]!=('') :
                return True
        elif position == "14":
            if self.markGrid[1][4]!=('') :
                return True
        elif position == "24":
            if self.markGrid[2][4]!=('') :
                return True
        elif position == "34":
            if self.markGrid[3][4]!=('') :
                return True
        elif position == "44":
            if self.markGrid[4][4]!=('') :
                return True

    def is_wall(self, posx, posy):

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

        position = self.get_square(posx, posy)

        if position == "00":
            if self.markGrid[0][0] == ('Z'):
                return True
        elif position == "10":
            if self.markGrid[1][0] == ('Z'):
                return True
        elif position == "20":
            if self.markGrid[2][0] == ('Z'):
                return True
        elif position == "30":
            if self.markGrid[3][0] == ('Z'):
                return True
        elif position == "40":
            if self.markGrid[4][0] == ('Z'):
                return True

        elif position == "01":
            if self.markGrid[0][1] == ('Z'):
                return True
        elif position == "11":
            if self.markGrid[1][1] == ('Z'):
                return True
        elif position == "21":
            if self.markGrid[2][1] == ('Z'):
                return True
        elif position == "31":
            if self.markGrid[3][1] == ('Z'):
                return True
        elif position == "41":
            if self.markGrid[4][1] == ('Z'):
                return True

        elif position == "02":
            if self.markGrid[0][2] == ('Z'):
                return True
        elif position == "12":
            if self.markGrid[1][2] == ('Z'):
                return True
        elif position == "22":
            if self.markGrid[2][2] == ('Z'):
                return True
        elif position == "32":
            if self.markGrid[3][2] == ('Z'):
                return True
        elif position == "42":
            if self.markGrid[4][2] == ('Z'):
                return True

        elif position == "03":
            if self.markGrid[0][3] == ('Z'):
                return True
        elif position == "13":
            if self.markGrid[1][3] == ('Z'):
                return True
        elif position == "23":
            if self.markGrid[2][3] == ('Z'):
                return True
        elif position == "33":
            if self.markGrid[3][3] == ('Z'):
                return True
        elif position == "43":
            if self.markGrid[4][3] == ('Z'):
                return True

        elif position == "04":
            if self.markGrid[0][4] == ('Z'):
                return True
        elif position == "14":
            if self.markGrid[1][4] == ('Z'):
                return True
        elif position == "24":
            if self.markGrid[2][4] == ('Z'):
                return True
        elif position == "34":
            if self.markGrid[3][4] == ('Z'):
                return True
        elif position == "44":
            if self.markGrid[4][4] == ('Z'):
                return True
