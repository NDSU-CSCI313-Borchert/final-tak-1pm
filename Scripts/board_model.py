import pygame
from board import *
from constants import *

class BoardModel():
    def __init__(self,x,y):
        super().__init__()
        # self.grid = [[((SCREEN_WIDTH/4)+(151*i),(SCREEN_HEIGHT/6+(151*j))) for i in range(5)] for j in range(5)]
        # print('\n'.join([''.join(['{0}'.format(item) for item in row]) for row in self.grid]))

        self.coord_grid = []
        for x in range(5):
            for y in range(5):
                self.coord_grid.append(((SCREEN_WIDTH/4)+(151*x),(SCREEN_HEIGHT/6+(151*y))))

        self.grid2 = []

        self.markGrid = [['' for i in range(5)] for j in range(5)]

    def get_grid(self):
        return self.grid




    def Check_victory(self):
        my_list =[]
        my_listy =[]
        #I find my first position to start
        for x in range(0,4):
            if self.markGrid[x][0]==('X'):
                currentX=x
                currentY=0
                my_list.append(currentX)
                my_listy.append(currentY)
                break
        #this check only runs if we found a mark
        while currentX < 5:
            if self.markGrid[currentX][currentY] ==('X'):
                #Look to the spot to the right for the mark
                if self.markGrid[currentX][currentY+1] ==('X'): 
                    currentY+=1
                    while currentY > 0:
                        if self.markGrid[currentX][currentY+1] ==('X'): 
                            currentY+=1
                        elif self.markGrid[currentX+1][currentY] ==('X'):
                            currentX+=1
                        elif self.markGrid[currentX-1][currentY] ==('X'):
                            currentX -=1
                        if currentX ==4:
                            return True
                    while currentX == 0:
                        if self.markGrid[currentX][currentY+1] ==('X'): 
                            currentY+=1
                        elif self.markGrid[currentX+1][currentY] ==('X'):
                            currentX+=1
                        if currentX ==4:
                            return True

                    
                elif self.markGrid[currentX-1][currentY] ==('X'):
                    currentX -=1
                elif self.markGrid[currentX+1][currentY] ==('X'):
                    currentX+=1
            
     
            



        
        #for x in range(0, 4):
         #   if board[x][0] == ('X'):
        #       current_spot = board[x][0]
        #       self.grid2 = current_spot
        #       break
                #I need a little help with logic, am i able to use current spot to check the spot next to it like current_spot[x][y+1]
        # if board[x + 1][0] == ('X'):
        #   current_spot = board[x+1][0]
        #   self.grid2[2] = current_spot
        #   if board[x + 2][0] == ('X'):
        #       current_spot = board[x + 2][0]
        #       self.grid2[3] = current_spot

        #   if board[x + 1][1] == ('X'):
        #           current_spot = board[x + 1][1]
        #           self.grid2[3] = current_spot

        # if board[x][0+1] == ('X'):
        #   current_spot = board[x][0+1]
        #   self.grid2[2] = current_spot

        #if board[x - 1][0] == ('X'):
        #   current_spot= board[x-1][0]
        #   self.grid2[3] = current_spot
        for x in range(0, 4):
            if self.markGrid[x][0] == ('X') and self.markGrid[x][1] == ('X') and self.markGrid[x][2] == ('X') and self.markGrid[x][3] == ('X') and \
                    self.markGrid[x][4] == ('X'):
                return True
            if self.markGrid[x][0] == ('Y') and self.markGrid[x][1] == ('Y') and self.markGrid[x][2] == ('Y') and self.markGrid[x][3] == ('Y') and \
                    self.markGrid[x][4] == ('Y'):
                return True
        for y in range(0, 4):
            if self.markGrid[0][y] == ('X') and self.markGrid[1][y] == ('X') and self.markGrid[2][y] == ('X') and self.markGrid[3][y] == ('X') and \
                    self.markGrid[4][y] == ('X'):
                return True
            if self.markGrid[0][y] == ('Y') and self.markGrid[1][y] == ('Y') and self.markGrid[2][y] == ('Y') and self.markGrid[3][y] == ('Y') and \
                    self.markGrid[4][y] == ('Y'):
                return True
            #1down and straight across
        if self.markGrid[0][0] == ('X') and self.markGrid[1][0] and self.markGrid[1][1] and self.markGrid[1][2] and self.markGrid[1][3] and self.markGrid[1][4]:
            return True
        #one down one to the right, then straight across
        if self.markGrid[0][0] == ('X') and self.markGrid[1][0]  == ('X') and self.markGrid[1][1] == ('X') and self.markGrid[2][1] == ('X') and self.markGrid[2][2] == ('X') and self.markGrid[2][3] == ('X') and self.markGrid[2][4] == ('X'):
            return True
        #one down, one to the right, one more down, and all the way across
        if self.markGrid[0][0] == ('X') and self.markGrid[1][0]  == ('X') and self.markGrid[1][1] == ('X') and self.markGrid[2][1] == ('X') and self.markGrid[2][2] == ('X') and self.markGrid[2][3] == ('X') and self.markGrid[2][4] == ('X'):
            return True
        # one down, one to the right, two more down, and all the way across
        if self.markGrid[0][0] == ('X') and self.markGrid[1][0]  == ('X') and self.markGrid[1][1] == ('X') and self.markGrid[2][1] == ('X') and self.markGrid[3][1] == ('X') and self.markGrid[3][2] == ('X') and self.markGrid[3][3] == ('X') and self.markGrid[3][4] == ('X'):
            return True
        # one down, one to the right, three more down, and all the way across
        if self.markGrid[0][0] == ('X') and self.markGrid[1][0] == ('X') and self.markGrid[1][1] == ('X') and \
                self.markGrid[2][1] == ('X') and self.markGrid[3][1] == ('X') and self.markGrid[3][2] == ('X') and \
                self.markGrid[3][3] == ('X') and self.markGrid[4][3]==('X') and self.markGrid[3][4] == ('X'):
            return True

        return False
#pos x from the mouse, position y from the mouse, a boolean stating weather or not it is player1, then if the stone is a standing stone.
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
        if posx > 374 and posx < 526 and posy > 316 and posy < 467:
            self.markGrid[1][0] = mark
        if posx > 374 and posx < 526 and posy > 467 and posy < 619:
            self.markGrid[2][0] = mark
        if posx > 374 and posx < 526 and posy > 618 and posy < 771:
            self.markGrid[3][0] = mark
        if posx > 374 and posx < 526 and posy > 770 and posy < 921:
            self.markGrid[4][0] = mark
        #The first row
        if posx > 526 and posx < 677 and posy > 166 and posy < 317:
            self.markGrid[0][1] = mark
        #The second column
        if posx > 526 and posx < 677 and posy > 316 and posy < 468:
            self.markGrid[1][1] = mark
        if posx > 526 and posx < 677 and posy > 467 and posy < 619:
            self.markGrid[2][1] = mark
        if posx > 526 and posx < 677 and posy > 618 and posy < 771:
            self.markGrid[3][1] = mark
        if posx > 526 and posx < 677 and posy > 770 and posy < 921:
            self.markGrid[4][1] = mark


        #Third Column
        if posx > 677 and posx < 826 and posy > 166 and posy < 317:
            self.markGrid[0][2] = mark
        if posx > 677 and posx < 826 and posy > 316 and posy < 468:
            self.markGrid[1][2] = mark
        if posx > 677 and posx < 826 and posy > 467 and posy < 619:
            self.markGrid[2][2] = mark
        if posx > 677 and posx < 826 and posy > 618 and posy < 771:
            self.markGrid[3][2] = mark
        if posx > 677 and posx < 826 and posy > 770 and posy < 921:
            self.markGrid[4][2] = mark
        #fourth coloumn
        if posx > 826 and posx < 978 and posy > 166 and posy < 317:
            self.markGrid[0][3] = mark
        if posx > 826 and posx < 978 and posy > 316 and posy < 468:
            self.markGrid[1][2] = mark
        if posx > 826 and posx < 978 and posy > 467 and posy < 619:
            self.markGrid[2][2] = mark
        if posx > 826 and posx < 978 and posy > 618 and posy < 771:
            self.markGrid[3][2] = mark
        if posx > 826 and posx < 978 and posy > 770 and posy < 921:
            self.markGrid[4][2] = mark
        #fifth coloumn
        if posx > 977 and posx < 1129 and posy > 166 and posy < 317:
            self.markGrid[0][4] = mark
        if posx > 977 and posx < 1129 and posy > 316 and posy < 468:
            self.markGrid[1][2] = mark
        if posx > 977 and posx < 1129 and posy > 467 and posy < 619:
            self.markGrid[2][2] = mark
        if posx > 977 and posx < 1129 and posy > 618 and posy < 771:
            self.markGrid[3][2] = mark
        if posx > 977 and posx < 1129 and posy > 770 and posy < 921:
            self.markGrid[4][2] = mark
