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

        self.markGrid = [['' for i in range(self.dimensions)] for j in range(self.dimensions)]
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

    def check_victory(self, target):
        x_victory = self.check_victory_x(target)
        if not x_victory:
            y_victory = self.check_victory_y(target)
        if x_victory or y_victory:
            return True
        else:
            return False

    def check_victory_x(self, target):
        self.target = target
        self.current_x = None
        self.current_y = None
        self.victory = False
        self.checks = 0

        # self.markGrid[row][column]
        
        for col in range(0, self.dimensions):
            if self.markGrid[0][col] == self.target:
                self.current_x = 0
                self.current_y = col
                break

        # vertical checking
        if self.current_x is not None:
            while self.current_x < self.dimensions:
                print(str(self.current_x) + "," + str(self.current_y))
                # failsafe to avoid infinite looping
                self.checks += 1
                if self.checks == 50:
                    break
                if self.markGrid[self.current_x][self.current_y] == self.target:
                        if self.current_x == (self.dimensions - 1):
                            self.victory = True
                            break
                        # prioritize the direction you are checking for
                        elif self.current_x < self.dimensions-1 and self.markGrid[self.current_x + 1][self.current_y] == self.target:
                            self.current_x += 1
                        elif self.current_y < self.dimensions-1 and self.markGrid[self.current_x][self.current_y + 1] == self.target:
                            self.current_y += 1
                        elif self.markGrid[self.current_x][self.current_y-1] == self.target and self.current_y > 0:
                            self.current_y -= 1
                        else:
                            break

        return self.victory

    def check_victory_y(self, target):
        self.target = target
        self.current_x = None
        self.current_y = None
        self.victory = False
        self.checks = 0
        
        for row in range(0, self.dimensions):
            if self.markGrid[row][0] == self.target:
                self.current_x = row
                self.current_y = 0
                break

        # vertical checking
        if self.current_y is not None:
            while self.current_y < self.dimensions:
                print(str(self.current_x) + "," + str(self.current_y))
                # failsafe to avoid infinite looping
                self.checks += 1
                if self.checks == 50:
                    break
                if self.markGrid[self.current_x][self.current_y] == self.target:
                        if self.current_y == (self.dimensions - 1):
                            self.victory = True
                            break
                        # prioritize the direction you are checking for
                        elif self.current_y < self.dimensions-1 and self.markGrid[self.current_x][self.current_y + 1] == self.target:
                            self.current_y += 1
                        elif self.current_x < self.dimensions-1 and self.markGrid[self.current_x + 1][self.current_y] == self.target:
                            self.current_x += 1
                        elif self.markGrid[self.current_x - 1][self.current_y] == self.target and self.current_x > 0:
                            self.current_x -= 1
                        else:
                            break

        return self.victory
      
    
    def marking(self,position,name,color):
        
        mark = ''
        
        if name == "flat" and color == "brown":
            mark='1f'
        elif name == "flat" and color == "beige":
            mark='2f'
        elif name == "wall" and color == "brown":
            mark='1w'
        elif name =="wall" and color =="beige":
            mark='2w'
        elif name =="capstone" and color =="brown":
            mark='1c'
        elif name =="capstone" and color =="beige":
            mark='2c'

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
    
    def mark_grid(self,stack00,stack10,stack20,stack30,stack40,stack01,stack11,stack21,stack31,stack41,stack02,stack12,stack22,stack32,stack42,stack03,stack13,stack23,stack33,stack43,stack04,stack14,stack24,stack34,stack44):
        self.marking(stack00[len(stack00) - 3], stack00[len(stack00) - 2], stack00[len(stack00) - 1])
        self.marking(stack10[len(stack10) - 3], stack10[len(stack10) - 2], stack10[len(stack10) - 1])
        self.marking(stack20[len(stack20) - 3], stack20[len(stack20) - 2], stack20[len(stack20) - 1])
        self.marking(stack30[len(stack30) - 3], stack30[len(stack30) - 2], stack30[len(stack30) - 1])
        self.marking(stack40[len(stack40) - 3], stack40[len(stack40) - 2], stack40[len(stack40) - 1])
        
        self.marking(stack01[len(stack01) - 3], stack01[len(stack01) - 2], stack01[len(stack01) - 1])
        self.marking(stack11[len(stack11) - 3], stack11[len(stack11) - 2], stack11[len(stack11) - 1])
        self.marking(stack21[len(stack21) - 3], stack21[len(stack21) - 2], stack21[len(stack21) - 1])
        self.marking(stack31[len(stack31) - 3], stack31[len(stack31) - 2], stack31[len(stack31) - 1])
        self.marking(stack41[len(stack41) - 3], stack41[len(stack41) - 2], stack41[len(stack41) - 1])
        
        self.marking(stack02[len(stack02) - 3], stack02[len(stack02) - 2], stack02[len(stack02) - 1])
        self.marking(stack12[len(stack12) - 3], stack12[len(stack12) - 2], stack12[len(stack12) - 1])
        self.marking(stack22[len(stack22) - 3], stack22[len(stack22) - 2], stack22[len(stack22) - 1])
        self.marking(stack32[len(stack32) - 3], stack32[len(stack32) - 2], stack32[len(stack32) - 1])
        self.marking(stack42[len(stack42) - 3], stack42[len(stack42) - 2], stack42[len(stack42) - 1])
        
        self.marking(stack03[len(stack03) - 3], stack03[len(stack03) - 2], stack03[len(stack03) - 1])
        self.marking(stack13[len(stack13) - 3], stack13[len(stack13) - 2], stack13[len(stack13) - 1])
        self.marking(stack23[len(stack23) - 3], stack23[len(stack23) - 2], stack23[len(stack23) - 1])
        self.marking(stack33[len(stack33) - 3], stack33[len(stack33) - 2], stack33[len(stack33) - 1])
        self.marking(stack43[len(stack43) - 3], stack43[len(stack43) - 2], stack43[len(stack43) - 1])
        
        self.marking(stack04[len(stack04) - 3], stack04[len(stack04) - 2], stack04[len(stack04) - 1])
        self.marking(stack14[len(stack14) - 3], stack14[len(stack14) - 2], stack14[len(stack14) - 1])
        self.marking(stack24[len(stack24) - 3], stack24[len(stack24) - 2], stack24[len(stack24) - 1])
        self.marking(stack34[len(stack34) - 3], stack34[len(stack34) - 2], stack34[len(stack34) - 1])
        self.marking(stack44[len(stack44) - 3], stack44[len(stack44) - 2], stack44[len(stack44) - 1])
    
        print(self.markGrid[0][0])
        print(self.markGrid[1][0])
        print(self.markGrid[2][0])
        print(self.markGrid[3][0])
        print(self.markGrid[4][0])

        print(self.markGrid[0][1])
        print(self.markGrid[1][1])
        print(self.markGrid[2][1])
        print(self.markGrid[3][1])
        print(self.markGrid[4][1])
    
        print(self.markGrid[0][2])
        print(self.markGrid[1][2])
        print(self.markGrid[2][2])
        print(self.markGrid[3][2])
        print(self.markGrid[4][2])
    
        print(self.markGrid[0][3])
        print(self.markGrid[1][3])
        print(self.markGrid[2][3])
        print(self.markGrid[3][3])
        print(self.markGrid[4][3])

        print(self.markGrid[0][4])
        print(self.markGrid[1][4])
        print(self.markGrid[2][4])
        print(self.markGrid[3][4])
        print(self.markGrid[4][4])

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

    '''
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
        '''
    
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

    def spot_occupied_by_wall(self,posx,posy):
        
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
