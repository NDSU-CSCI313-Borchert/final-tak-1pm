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

        print(self.dimensions)

        for x in range(self.dimensions):
            for y in range(self.dimensions):
                print(((pos[0])+(151*x),(pos[1]+(151*y))))
                self.coord_grid.append(((pos[0])+(151*x),(pos[1]+(151*y))))

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
        
        pickup = self.get_square(posx, posy)
        
        if pickup == "00":
            if self.markGrid[0][0]!=(''):
                self.handstack.append(self.markGrid[0][0])
                self.markGrid[0][0]=self.stack.pop()
        elif pickup == "10":
            if self.markGrid[1][0]!=(''):
                self.handstack.append(self.markGrid[1][0])
                self.markGrid[1][0] = self.stack2.pop()
        elif pickup == "20":
            if self.markGrid[2][0]!=(''):
                self.handstack.append(self.markGrid[2][0])
                self.markGrid[2][0] = self.stack3.pop()
        elif pickup == "30":
            if self.markGrid[3][0]!=(''):
                self.handstack.append(self.markGrid[3][0])
                self.markGrid[3][0] = self.stack4.pop()
        elif pickup == "40":
            if self.markGrid[4][0]!=(''):
                self.handstack.append(self.markGrid[4][0])
                self.markGrid[4][0] = self.stack5.pop()

        elif pickup == "01":
            if self.markGrid[0][1]!=(''):
                self.handstack.append(self.markGrid[0][1])
                self.markGrid[0][1] = self.stack6.pop()
        elif pickup == "11":
            if self.markGrid[1][1]!=(''):
                self.handstack.append(self.markGrid[1][1])
                self.markGrid[1][1] = self.stack7.pop()
        elif pickup == "21":
            if self.markGrid[2][1]!=(''):
                self.handstack.append(self.markGrid[2][1])
                self.markGrid[2][1] = self.stack8.pop()
        elif pickup == "31":
            if self.markGrid[3][1]!=(''):
                self.handstack.append(self.markGrid[3][1])
                self.markGrid[3][1] = self.stack9.pop()
        elif pickup == "41":
            if self.markGrid[4][1]!=(''):
                self.handstack.append(self.markGrid[4][1])
                self.markGrid[4][1] = self.stack10.pop()

        elif pickup == "02":
            if self.markGrid[0][2]!=(''):
                self.handstack.append(self.markGrid[0][2])
                self.markGrid[0][2] = self.stack11.pop()
        elif pickup == "12":
            if self.markGrid[1][2]!=(''):
                self.handstack.append(self.markGrid[1][2])
                self.markGrid[1][2] = self.stack12.pop()
        elif pickup == "22":
            if self.markGrid[2][2]!=(''):
                self.handstack.append(self.markGrid[2][2])
                self.markGrid[2][2] = self.stack13.pop()
        elif pickup == "32":
            if self.markGrid[3][2]!=(''):
                self.handstack.append(self.markGrid[3][2])
                self.markGrid[3][2] = self.stack14.pop()
        elif pickup == "42":
            if self.markGrid[4][2]!=(''):
                self.handstack.append(self.markGrid[4][2])
                self.markGrid[4][2] = self.stack15.pop()

        elif pickup == "03":
            if self.markGrid[0][3]!=(''):
                self.handstack.append(self.markGrid[0][3])
                self.markGrid[0][3] = self.stack16.pop()
        elif pickup == "13":
            if self.markGrid[1][3]!=(''):
                self.handstack.append(self.markGrid[1][3])
                self.markGrid[1][3] = self.stack17.pop()
        elif pickup == "23":
            if self.markGrid[2][3]!=(''):
                self.handstack.append(self.markGrid[2][3])
                self.markGrid[2][3] = self.stack18.pop()
        elif pickup == "33":
            if self.markGrid[3][3]!=(''):
                self.handstack.append(self.markGrid[3][3])
                self.markGrid[3][3] = self.stack19.pop()
        elif pickup == "43":
            if self.markGrid[4][3]!=(''):
                self.handstack.append(self.markGrid[4][3])
                self.markGrid[4][3] = self.stack20.pop()

        elif pickup == "04":
            if self.markGrid[0][4]!=(''):
                self.handstack.append(self.markGrid[0][4])
                self.markGrid[0][4] = self.stack21.pop()
        elif pickup == "14":
            if self.markGrid[1][4]!=(''):
                self.handstack.append(self.markGrid[1][4])
            self.markGrid[1][4] = self.stack22.pop()
        elif pickup == "24":
            if self.markGrid[2][4]!=(''):
                self.handstack.append(self.markGrid[2][4])
                self.markGrid[2][4] = self.stack23.pop()
        elif pickup == "34":
            if self.markGrid[3][4]!=(''):
                self.handstack.append(self.markGrid[3][4])
                self.markGrid[3][4] = self.stack24.pop()
        elif pickup == "44":
            if self.markGrid[4][4]!=(''):
                self.handstack.append(self.markGrid[4][4])
                self.markGrid[4][4] = self.stack25.pop()



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
        
        pickup = self.get_square(posx, posy)
        
        if b == True:
            mark = 'X'
        else:
            mark = 'Y'
        
        if pickup == "00":
            self.markGrid[0][0] = mark
        elif pickup == "10":
            self.markGrid[1][0] = mark
        elif pickup == "20":
            self.markGrid[2][0] = mark
        elif pickup == "30":
            self.markGrid[3][0] = mark
        elif pickup == "40":
            self.markGrid[4][0] = mark

        elif pickup == "01":
            self.markGrid[0][1] = mark
        elif pickup == "11":
            self.markGrid[1][1] = mark
        elif pickup == "21":
            self.markGrid[2][1] = mark
        elif pickup == "31":
            self.markGrid[3][1] = mark
        elif pickup == "41":
            self.markGrid[4][1] = mark

        elif pickup == "02":
            self.markGrid[0][2] = mark
        elif pickup == "12":
            self.markGrid[1][2] = mark
        elif pickup == "22":
            self.markGrid[2][2] = mark
        elif pickup == "32":
            self.markGrid[3][2] = mark
        elif pickup == "42":
            self.markGrid[4][2] = mark

        elif pickup == "03":
            self.markGrid[0][3] = mark
        elif pickup == "13":
            self.markGrid[1][3] = mark
        elif pickup == "23":
            self.markGrid[2][3] = mark
        elif pickup == "33":
            self.markGrid[3][3] = mark
        elif pickup == "43":
            self.markGrid[4][3] = mark

        elif pickup == "04":
            self.markGrid[0][4] = mark
        elif pickup == "14":
            self.markGrid[1][4] = mark
        elif pickup == "24":
            self.markGrid[2][4] = mark
        elif pickup == "34":
            self.markGrid[3][4] = mark
        elif pickup == "44":
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
        pickup = self.get_square(posx, posy)
        
        if b == True:
            mark = 'X'
        else:
            mark = 'Y'
        if standingStone == True:
            mark = 'Z'
        
        if pickup == "00":
            self.stack_0_0_model.append(self.markGrid[0][0])
            self.markGrid[0][0] = mark
        elif pickup == "10":
            self.stack_1_0_model.append(self.markGrid[1][0])
            self.markGrid[1][0] = mark
        elif pickup == "20":
            self.stack_2_0_model.append(self.markGrid[2][0])
            self.markGrid[2][0] = mark
        elif pickup == "30":
            self.stack_3_0_model.append(self.markGrid[3][0])
            self.markGrid[3][0] = mark
        elif pickup == "40":
            self.stack_4_0_model.append(self.markGrid[4][0])
            self.markGrid[4][0] = mark

        elif pickup == "01":
            self.stack_0_1_model.append(self.markGrid[0][1])
            self.markGrid[0][1] = mark
        elif pickup == "11":
            self.stack_1_1_model.append(self.markGrid[1][1])
            self.markGrid[1][1] = mark
        elif pickup == "21":
            self.stack_2_1_model.append(self.markGrid[2][1])
            self.markGrid[2][1] = mark
        elif pickup == "31":
            self.stack_3_1_model.append(self.markGrid[3][1])
            self.markGrid[3][1] = mark
        elif pickup == "41":
            self.stack_4_1_model.append(self.markGrid[4][1])
            self.markGrid[4][1] = mark

        elif pickup == "02":
            self.stack_0_2_model.append(self.markGrid[0][2])
            self.markGrid[0][2] = mark
        elif pickup == "12":
            self.stack_1_2_model.append(self.markGrid[1][2])
            self.markGrid[1][2] = mark
        elif pickup == "22":
            self.stack_2_2_model.append(self.markGrid[2][2])
            self.markGrid[2][2] = mark
        elif pickup == "32":
            self.stack_3_2_model.append(self.markGrid[3][2])
            self.markGrid[3][2] = mark
        elif pickup == "42":
            self.stack_4_2_model.append(self.markGrid[4][2])
            self.markGrid[4][2] = mark

        elif pickup == "03":
            self.stack_0_3_model.append(self.markGrid[0][3])
            self.markGrid[0][3] = mark
        elif pickup == "13":
            self.stack_1_3_model.append(self.markGrid[1][3])
            self.markGrid[1][3] = mark
        elif pickup == "23":
            self.stack_2_3_model.append(self.markGrid[2][3])
            self.markGrid[2][3] = mark
        elif pickup == "33":
            self.stack_3_3_model.append(self.markGrid[3][3])
            self.markGrid[3][3] = mark
        elif pickup == "43":
            self.stack_4_3_model.append(self.markGrid[4][3])
            self.markGrid[4][3] = mark

        elif pickup == "04":
            self.stack_0_4_model.append(self.markGrid[0][4])
            self.markGrid[0][4] = mark
        elif pickup == "14":
            self.stack_1_4_model.append(self.markGrid[1][4])
            self.markGrid[1][4] = mark
        elif pickup == "24":
            self.stack_2_4_model.append(self.markGrid[2][4])
            self.markGrid[2][4] = mark
        elif pickup == "34":
            self.stack_3_4_model.append(self.markGrid[3][4])
            self.markGrid[3][4] = mark
        elif pickup == "44":
            self.stack_4_4_model.append(self.markGrid[4][4])
            self.markGrid[4][4] = mark
        pprint.pprint(self.markGrid)

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
        
        pickup = self.get_square(posx, posy)

        if pickup == "00":
            if self.markGrid[0][0] ==('Z') :
                return True
        elif pickup == "10":
            if self.markGrid[1][0]==('Z') :
                return True
        elif pickup == "20":
            if self.markGrid[2][0]==('Z') :
                return True
        elif pickup == "30":
            if self.markGrid[3][0]==('Z') :
                return True
        elif pickup == "40":
            if self.markGrid[4][0]==('Z') :
                return True

        elif pickup == "01":
            if self.markGrid[0][1]==('Z') :
                return True
        elif pickup == "11":
            if self.markGrid[1][1]==('Z') :
                return True
        elif pickup == "21":
            if self.markGrid[2][1]==('Z') :
                return True
        elif pickup == "31":
            if self.markGrid[3][1]==('Z') :
                return True
        elif pickup == "41":
            if self.markGrid[4][1]==('Z') :
                return True

        elif pickup == "02":
            if self.markGrid[0][2]==('Z') :
                return True
        elif pickup == "12":
            if self.markGrid[1][2]==('Z') :
                return True
        elif pickup == "22":
            if self.markGrid[2][2]==('Z') :
                return True
        elif pickup == "32":
            if self.markGrid[3][2]==('Z') :
                return True
        elif pickup == "42":
            if self.markGrid[4][2]==('Z') :
                return True

        elif pickup == "03":
            if self.markGrid[0][3]==('Z') :
                return True
        elif pickup == "13":
            if self.markGrid[1][3]==('Z') :
                return True
        elif pickup == "23":
            if self.markGrid[2][3]==('Z') :
                return True
        elif pickup == "33":
            if self.markGrid[3][3]==('Z') :
                return True
        elif pickup == "43":
            if self.markGrid[4][3]==('Z') :
                return True

        elif pickup == "04":
            if self.markGrid[0][4]==('Z') :
                return True
        elif pickup == "14":
            if self.markGrid[1][4]==('Z') :
                return True
        elif pickup == "24":
            if self.markGrid[2][4]==('Z') :
                return True
        elif pickup == "34":
            if self.markGrid[3][4]==('Z') :
                return True
        elif pickup == "44":
            if self.markGrid[4][4]==('Z') :
                return True

