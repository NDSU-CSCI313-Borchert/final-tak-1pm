"""
    
    Authors: Skyler Svendsen, Michael Footitt, Nick Hilger
"""
import pygame
import random
import pprint
from constants import *
from board import *
from player import *
from stone import *
from capstone import *
from level_manager import *
from board_model import *
import math
from title_screen import *

import pygame.time

class GameLevel():
    def __init__(self, p1_wins=0, p2_wins=0, p1_score=0, p2_score=0, size="", design=""):
        # Initialize Pygame
        pygame.init()
        
        # Set the height and width of the screen
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        
        # These are lists of 'sprites.' Each block in the program is
        # added to this list. The list is managed by a class called 'Group.'

        # This is a list of every sprite.
        # All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()
        self.board_list = pygame.sprite.Group()
        
        
        level_manager = LevelManager()
        
        self.done = False

        # set the board's size and design
        self.size = size
        self.design = design

        # Create the board
        board_type = str(self.size + self.design)
        
        self.board = Board(board_type)
        self.board.rect.center = (SCREEN_CENTER)
        self.board_list.add(self.board)
        self.board_model = BoardModel(self.board.rect.topleft, self.size)

        # set how many pieces there are (based on board size)
        self.piece_total = 0
        self.capstone_total = 0
        if self.size == "3x3":
            self.piece_total = 10
        elif self.size == "4x4":
            self.piece_total = 15
        elif self.size == "5x5":
            self.piece_total = 21
            self.capstone_total = 1
        
        # Create the players
        self.player1 = Player(self.piece_total, self.capstone_total)
        self.player1.name = "Player One"
        self.player2 = Player(self.piece_total, self.capstone_total)
        self.player2.name = "Player Two"

        #Create the pieces
        self.player1pieces = []
        self.player2pieces = []
        for i in range(0, (self.piece_total-1) * 2):
            stone1 = Stone("brown_stone", "brown_wall")
            stone1.rect.x = (SCREEN_WIDTH / 6) - 100
            stone1.rect.y = (SCREEN_HEIGHT / 2)
            self.all_sprites_list.add(stone1)
            self.player1pieces.append(stone1)
        
            stone2 = Stone("beige_stone", "beige_wall")
            stone2.rect.x = (SCREEN_WIDTH / 6 * 5)
            stone2.rect.y = (SCREEN_HEIGHT / 2)
            self.all_sprites_list.add(stone2)
            self.player2pieces.append(stone2)
        
        '''
        self.player2pieces = []
        for i in range(0, self.piece_total-1):
            stone = Stone("beige_stone", "beige_wall")
            stone.rect.x = (SCREEN_WIDTH / 6 * 5)
            stone.rect.y = (SCREEN_HEIGHT / 2)
            self.all_sprites_list.add(stone)
            self.player2pieces.append(stone)
        '''
        
        #Create the capstones if board size allows it
        if self.capstone_total > 0:
            self.player1capstone = Capstone("brown_capstone")
            self.player1capstone.rect.x = (SCREEN_WIDTH / 6) - 95
            self.player1capstone.rect.y = (SCREEN_HEIGHT / 2) + 150
            self.all_sprites_list.add(self.player1capstone)
            
            self.player2capstone = Capstone("beige_capstone")
            self.player2capstone.rect.x = ((SCREEN_WIDTH / 6 * 5) - 0)
            self.player2capstone.rect.y = (SCREEN_HEIGHT / 2) + 150
            self.all_sprites_list.add(self.player2capstone)
        
        self.stack_0_0 = []
        self.stack_0_1 = []
        self.stack_0_2 = []
        self.stack_0_3 = []
        self.stack_0_4 = []
        self.stack_1_0 = []
        self.stack_1_1 = []
        self.stack_1_2 = []
        self.stack_1_3 = []
        self.stack_1_4 = []
        self.stack_2_0 = []
        self.stack_2_1 = []
        self.stack_2_2 = []
        self.stack_2_3 = []
        self.stack_2_4 = []
        self.stack_3_0 = []
        self.stack_3_1 = []
        self.stack_3_2 = []
        self.stack_3_3 = []
        self.stack_3_4 = []
        self.stack_4_0 = []
        self.stack_4_1 = []
        self.stack_4_2 = []
        self.stack_4_3 = []
        self.stack_4_4 = []
        
        self.current_grid_pos = ""
        
        # Loop until the user clicks the close button.
        done = False
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.start_time = pygame.time.get_ticks()

        self.current_player = self.player1
        self.sprite_click_list = []

        self.button = pygame.Rect(50, SCREEN_HEIGHT - 50, 100, 30)
        self.click_count = 0

        self.p1_wins = p1_wins
        self.p2_wins = p2_wins
        self.p1_score = p1_score
        self.p2_score = p2_score

        self.winner = ""
        self.done = False


    #Animation
    def update(self):

        if not self.done:
            counting_time = pygame.time.get_ticks() - self.start_time

            self.minutes = str(int(counting_time/60000)).zfill(2)
            self.seconds = str(int((counting_time%60000)/1000)).zfill(2)

        self.screen.fill(WHITE)

        pos = pygame.mouse.get_pos()

        for sprite in self.sprite_click_list:
            sprite.rect.x = pos[0]-40
            sprite.rect.y = pos[1]-25

        self.all_sprites_list.update()

    def handle_keyboard_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_CLICK:

            pos = pygame.mouse.get_pos()
            
            self.current_x = pos[0]
            self.current_y = pos[1]

            grid_pos = self.board_model.get_square(self.current_x, self.current_y)

            if self.button.collidepoint(pos):
                LevelManager().load_level(GameLevel(self.p1_wins, self.p2_wins, self.p1_score, self.p2_score, self.size, self.design))

            #No piece has been picked up yet
            if self.click_count == 0:
                
                #regular piece p1 pick up logic
                if self.player1.stones > 0 and not self.done:
                    p1top = self.player1pieces[0]

                    if p1top.rect.collidepoint(pos) and self.current_player == self.player1:
                        self.player1.removeStone()
                        self.sprite_click_list.append(self.player1pieces.pop())
                        self.click_count += 1
                #capstone p1 pick up logic
                if self.player1.capstones > 0 and not self.done:
                    p1top = self.player1capstone
                    
                    if p1top.rect.collidepoint(pos) and self.current_player == self.player1:
                        self.player1.removeCapstone()
                        self.sprite_click_list.append(self.player1capstone)
                        self.click_count += 1
                
                #regular piece p2 pick up logic
                if self.player2.stones > 0 and not self.done:
                    p2top = self.player2pieces[0]

                    if p2top.rect.collidepoint(pos) and self.current_player == self.player2:
                        self.player2.removeStone()
                        self.sprite_click_list.append(self.player2pieces.pop())
                        self.click_count += 1
                
                #capstone p2 pick up logic
                if self.player2.capstones > 0 and not self.done:
                    p2top = self.player2capstone
                        
                    if p2top.rect.collidepoint(pos) and self.current_player == self.player2:
                        self.player2.removeCapstone()
                        self.sprite_click_list.append(self.player2capstone)
                        self.click_count += 1

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

###############piece pickup from grid logic###################
                
                #find the grid that was clicked on
                if grid_pos == "00":
                    
                    #grab index of top piece
                    index = len(self.stack_0_0) - 1
                    
                    #if current stack has a piece in it, we are safe to call operations
                    if len(self.stack_0_0) > 0:
                        self.current_grid_pos = "00"
                        #check current player against color of piece
                        if self.current_player == self.player1 and self.stack_0_0[index].color == "brown":
                            
                            #if current player matches color of piece clicked on, allow to push to sprite click list
                            self.sprite_click_list.append(self.stack_0_0.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_0_0[index].color == "beige":
                            self.sprite_click_list.append(self.stack_0_0.pop())
                            self.click_count = 2
                elif grid_pos == "10":
                    index = len(self.stack_1_0) - 1
                    if len(self.stack_1_0) > 0:
                        self.current_grid_pos = "10"
                        if self.current_player == self.player1 and self.stack_1_0[index].color == "brown":
                            self.sprite_click_list.append(self.stack_1_0.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_1_0[index].color == "beige":
                            self.sprite_click_list.append(self.stack_1_0.pop())
                            self.click_count = 2
                elif grid_pos == "20":
                    index = len(self.stack_2_0) - 1
                    if len(self.stack_2_0) > 0:
                        self.current_grid_pos = "20"
                        if self.current_player == self.player1 and self.stack_2_0[index].color == "brown":
                            self.sprite_click_list.append(self.stack_2_0.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_2_0[index].color == "beige":
                            self.sprite_click_list.append(self.stack_2_0.pop())
                            self.click_count = 2
                elif grid_pos == "30":
                    index = len(self.stack_3_0) - 1
                    if len(self.stack_3_0) > 0:
                        self.current_grid_pos = "30"
                        if self.current_player == self.player1 and self.stack_3_0[index].color == "brown":
                            self.sprite_click_list.append(self.stack_3_0.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_3_0[index].color == "beige":
                            self.sprite_click_list.append(self.stack_3_0.pop())
                            self.click_count = 2
                elif grid_pos == "40":
                    index = len(self.stack_4_0) - 1
                    if len(self.stack_4_0) > 0:
                        self.current_grid_pos = "40"
                        if self.current_player == self.player1 and self.stack_4_0[index].color == "brown":
                            self.sprite_click_list.append(self.stack_4_0.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_4_0[index].color == "beige":
                            self.sprite_click_list.append(self.stack_4_0.pop())
                            self.click_count = 2

                elif grid_pos == "01":
                    index = len(self.stack_0_1) - 1
                    if len(self.stack_0_1) > 0:
                        self.current_grid_pos = "01"
                        if self.current_player == self.player1 and self.stack_0_1[index].color == "brown":
                            self.sprite_click_list.append(self.stack_0_1.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_0_1[index].color == "beige":
                            self.sprite_click_list.append(self.stack_0_1.pop())
                            self.click_count = 2
                elif grid_pos == "11":
                    index = len(self.stack_1_1) - 1
                    if len(self.stack_1_1) > 0:
                        self.current_grid_pos = "11"
                        if self.current_player == self.player1 and self.stack_1_1[index].color == "brown":
                            self.sprite_click_list.append(self.stack_1_1.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_1_1[index].color == "beige":
                            self.sprite_click_list.append(self.stack_1_1.pop())
                            self.click_count = 2
                elif grid_pos == "21":
                    index = len(self.stack_2_1) - 1
                    if len(self.stack_2_1) > 0:
                        self.current_grid_pos = "21"
                        if self.current_player == self.player1 and self.stack_2_1[index].color == "brown":
                            self.sprite_click_list.append(self.stack_2_1.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_2_1[index].color == "beige":
                            self.sprite_click_list.append(self.stack_2_1.pop())
                            self.click_count = 2
                elif grid_pos == "31":
                    index = len(self.stack_3_1) - 1
                    if len(self.stack_3_1) > 0:
                        self.current_grid_pos = "31"
                        if self.current_player == self.player1 and self.stack_3_1[index].color == "brown":
                            self.sprite_click_list.append(self.stack_3_1.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_3_1[index].color == "beige":
                            self.sprite_click_list.append(self.stack_3_1.pop())
                            self.click_count = 2
                elif grid_pos == "41":
                    index = len(self.stack_4_1) - 1
                    if len(self.stack_4_1) > 0:
                        self.current_grid_pos = "41"
                        if self.current_player == self.player1 and self.stack_4_1[index].color == "brown":
                            self.sprite_click_list.append(self.stack_4_1.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_4_1[index].color == "beige":
                            self.sprite_click_list.append(self.stack_4_1.pop())
                            self.click_count = 2

                elif grid_pos == "02":
                    index = len(self.stack_0_2) - 1
                    if len(self.stack_0_2) > 0:
                        self.current_grid_pos = "02"
                        if self.current_player == self.player1 and self.stack_0_2[index].color == "brown":
                            self.sprite_click_list.append(self.stack_0_2.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_0_2[index].color == "beige":
                            self.sprite_click_list.append(self.stack_0_2.pop())
                            self.click_count = 2
                elif grid_pos == "12":
                    index = len(self.stack_1_2) - 1
                    if len(self.stack_1_2) > 0:
                        self.current_grid_pos = "12"
                        if self.current_player == self.player1 and self.stack_1_2[index].color == "brown":
                            self.sprite_click_list.append(self.stack_1_2.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_1_2[index].color == "beige":
                            self.sprite_click_list.append(self.stack_1_2.pop())
                            self.click_count = 2
                elif grid_pos == "22":
                    index = len(self.stack_2_2) - 1
                    if len(self.stack_2_2) > 0:
                        self.current_grid_pos = "22"
                        if self.current_player == self.player1 and self.stack_2_2[index].color == "brown":
                            self.sprite_click_list.append(self.stack_2_2.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_2_2[index].color == "beige":
                            self.sprite_click_list.append(self.stack_2_2.pop())
                            self.click_count = 2
                elif grid_pos == "32":
                    index = len(self.stack_3_2) - 1
                    if len(self.stack_3_2) > 0:
                        self.current_grid_pos = "32"
                        if self.current_player == self.player1 and self.stack_3_2[index].color == "brown":
                            self.sprite_click_list.append(self.stack_3_2.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_3_2[index].color == "beige":
                            self.sprite_click_list.append(self.stack_3_2.pop())
                            self.click_count = 2
                elif grid_pos == "42":
                    index = len(self.stack_4_2) - 1
                    if len(self.stack_4_2) > 0:
                        self.current_grid_pos = "42"
                        if self.current_player == self.player1 and self.stack_4_2[index].color == "brown":
                            self.sprite_click_list.append(self.stack_4_2.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_4_2[index].color == "beige":
                            self.sprite_click_list.append(self.stack_4_2.pop())
                            self.click_count = 2

                elif grid_pos == "03":
                    index = len(self.stack_0_3) - 1
                    if len(self.stack_0_3) > 0:
                        self.current_grid_pos = "03"
                        if self.current_player == self.player1 and self.stack_0_3[index].color == "brown":
                            self.sprite_click_list.append(self.stack_0_3.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_0_3[index].color == "beige":
                            self.sprite_click_list.append(self.stack_0_3.pop())
                            self.click_count = 2
                elif grid_pos == "13":
                    index = len(self.stack_1_3) - 1
                    if len(self.stack_1_3) > 0:
                        self.current_grid_pos = "13"
                        if self.current_player == self.player1 and self.stack_1_3[index].color == "brown":
                            self.sprite_click_list.append(self.stack_1_3.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_1_3[index].color == "beige":
                            self.sprite_click_list.append(self.stack_1_3.pop())
                            self.click_count = 2
                elif grid_pos == "23":
                    index = len(self.stack_2_3) - 1
                    if len(self.stack_2_3) > 0:
                        self.current_grid_pos = "23"
                        if self.current_player == self.player1 and self.stack_2_3[index].color == "brown":
                            self.sprite_click_list.append(self.stack_2_3.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_2_3[index].color == "beige":
                            self.sprite_click_list.append(self.stack_2_3.pop())
                            self.click_count = 2
                elif grid_pos == "33":
                    index = len(self.stack_3_3) - 1
                    if len(self.stack_3_3) > 0:
                        self.current_grid_pos = "33"
                        if self.current_player == self.player1 and self.stack_3_3[index].color == "brown":
                            self.sprite_click_list.append(self.stack_3_3.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_3_3[index].color == "beige":
                            self.sprite_click_list.append(self.stack_3_3.pop())
                            self.click_count = 2
                elif grid_pos == "43":
                    index = len(self.stack_4_3) - 1
                    if len(self.stack_4_3) > 0:
                        self.current_grid_pos = "43"
                        if self.current_player == self.player1 and self.stack_4_3[index].color == "brown":
                            self.sprite_click_list.append(self.stack_4_3.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_4_3[index].color == "beige":
                            self.sprite_click_list.append(self.stack_4_3.pop())
                            self.click_count = 2

                elif grid_pos == "04":
                    index = len(self.stack_0_4) - 1
                    if len(self.stack_0_4) > 0:
                        self.current_grid_pos = "04"
                        if self.current_player == self.player1 and self.stack_0_4[index].color == "brown":
                            self.sprite_click_list.append(self.stack_0_4.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_0_4[index].color == "beige":
                            self.sprite_click_list.append(self.stack_0_4.pop())
                            self.click_count = 2
                elif grid_pos == "14":
                    index = len(self.stack_1_4) - 1
                    if len(self.stack_1_4) > 0:
                        self.current_grid_pos = "14"
                        if self.current_player == self.player1 and self.stack_1_4[index].color == "brown":
                            self.sprite_click_list.append(self.stack_1_4.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_1_4[index].color == "beige":
                            self.sprite_click_list.append(self.stack_1_4.pop())
                            self.click_count = 2
                elif grid_pos == "24":
                    index = len(self.stack_2_4) - 1
                    if len(self.stack_2_4) > 0:
                        self.current_grid_pos = "24"
                        if self.current_player == self.player1 and self.stack_2_4[index].color == "brown":
                            self.sprite_click_list.append(self.stack_2_4.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_2_4[index].color == "beige":
                            self.sprite_click_list.append(self.stack_2_4.pop())
                            self.click_count = 2
                elif grid_pos == "34":
                    index = len(self.stack_3_4) - 1
                    if len(self.stack_3_4) > 0:
                        self.current_grid_pos = "34"
                        if self.current_player == self.player1 and self.stack_3_4[index].color == "brown":
                            self.sprite_click_list.append(self.stack_3_4.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_3_4[index].color == "beige":
                            self.sprite_click_list.append(self.stack_3_4.pop())
                            self.click_count = 2
                elif grid_pos == "44":
                    index = len(self.stack_4_4) - 1
                    if len(self.stack_4_4) > 0:
                        self.current_grid_pos = "44"
                        if self.current_player == self.player1 and self.stack_4_4[index].color == "brown":
                            self.sprite_click_list.append(self.stack_4_4.pop())
                            self.click_count = 2
                        elif self.current_player == self.player2 and self.stack_4_4[index].color == "beige":
                            self.sprite_click_list.append(self.stack_4_4.pop())
                            self.click_count = 2
                
                #for each spite in grid
                    #if self.sprite.collidepoint(pos):
                        #if grid pos contains a stack of pieces
                            #if left click push piece on to moving stack
                            #elif right click replaces piece from moving stack to grid stack

                        #function to only allow piece to move one space adjacent

            #unplayed piece has been picked up and is in sprite click list
            elif self.click_count == 1:
                if (self.board.rect.topleft[0] < self.current_x < self.board.rect.topright[0]) and (self.board.rect.topleft[1] < self.current_y < self.board.rect.bottomleft[1]):
                    # This code helps the pieces snap in place
                    distance_to_snap = 145
                    stone = self.sprite_click_list[0]
                    px, py = stone.rect.center
                    
                    position = self.board_model.get_square(px, py)
                    adjacent_positions = self.board_model.get_adjacent_squares(position)
                    
                    """
                    if position == self.current_grid_pos:
                        self.click_count = 0
                    """
                    
####################################code that handles placing a piece#####################################
                    #if spot is occupied don't allow placement
                    if self.board_model.spot_occupied(px, py):
                        print("Occupied")
                        pass
                    #if capstone.name == 'capstone'
                        #self.board_model.Mark_spot(px,py,if player 1 this true, this should be false if not a standing stone)
                    
                    #if spot is unoccupied allow placement
                    else:
                        """
                        if self.current_player == self.player1:
                            if stone.name == "wall":
                                self.board_model.Mark_spot(px,py,True,True)
                            else:
                                self.board_model.Mark_spot(px,py,True,False)
                        elif self.current_player == self.player2:
                            if stone.name == "wall":
                                self.board_model.Mark_spot(px,py,False,True)
                            else:
                                self.board_model.Mark_spot(px,py,False,False)
                        """
                        
                        for cx, cy in self.board_model.coord_grid:
                            if math.hypot(cx-px, cy-py) < distance_to_snap:
                                stone.rect.x = cx+25
                                stone.rect.y = cy+45
                                break
                        
                        if position == "00":
                            self.place_piece_on_grid("00")
                        elif position == "10":
                            self.place_piece_on_grid("10")
                        elif position == "20":
                            self.place_piece_on_grid("20")
                        elif position == "30":
                            self.place_piece_on_grid("30")
                        elif position == "40":
                            self.place_piece_on_grid("40")
                        
                        elif position == "01":
                            self.place_piece_on_grid("01")
                        elif position == "11":
                            self.place_piece_on_grid("11")
                        elif position == "21":
                            self.place_piece_on_grid("21")
                        elif position == "31":
                            self.place_piece_on_grid("31")
                        elif position == "41":
                            self.place_piece_on_grid("41")

                        elif position == "02":
                            self.place_piece_on_grid("02")
                        elif position == "12":
                            self.place_piece_on_grid("12")
                        elif position == "22":
                            self.place_piece_on_grid("22")
                        elif position == "32":
                            self.place_piece_on_grid("32")
                        elif position == "42":
                            self.place_piece_on_grid("42")

                        elif position == "03":
                            self.place_piece_on_grid("03")
                        elif position == "13":
                            self.place_piece_on_grid("13")
                        elif position == "23":
                            self.place_piece_on_grid("23")
                        elif position == "33":
                            self.place_piece_on_grid("33")
                        elif position == "43":
                            self.place_piece_on_grid("43")

                        elif position == "04":
                            self.place_piece_on_grid("04")
                        elif position == "14":
                            self.place_piece_on_grid("14")
                        elif position == "24":
                            self.place_piece_on_grid("24")
                        elif position == "34":
                            self.place_piece_on_grid("34")
                        elif position == "44":
                            self.place_piece_on_grid("44")

                                    
                # Clicking outside the board will toggle the piece between road and wall
                else:
                    self.sprite_click_list[0].flipStone()

            #grid piece is in sprite click list
            elif self.click_count == 2:
                if (self.board.rect.topleft[0] < self.current_x < self.board.rect.topright[0]) and (self.board.rect.topleft[1] < self.current_y < self.board.rect.bottomleft[1]):
                # This code helps the pieces snap in place
                    distance_to_snap = 145
                    stone = self.sprite_click_list[0]
                    px, py = stone.rect.center
                    position = self.board_model.get_square(px, py)
                    adjacent_positions = self.board_model.get_adjacent_squares(self.current_grid_pos)
                    adjacent_positions_length = len(adjacent_positions)
                ####################################code that handles placing a piece#####################################
                #if spot is occupied don't allow placement
                if self.board_model.spot_occupied_by_wall(px, py):
                    #####MUST UPDATE METHOD AFTER MIKE GETS HIS PIECE DONE##############
                    pass
                for x in range(0, adjacent_positions_length):
                    if position == adjacent_positions[x]:
                        
                        for cx, cy in self.board_model.coord_grid:
                            if math.hypot(cx-px, cy-py) < distance_to_snap:
                                stone.rect.x = cx+25
                                stone.rect.y = cy+45
                                break
                        
                        self.place_piece_on_grid(adjacent_positions[x])
                        
                
                
        elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT_CLICK:
            print ("Right click")

            pos = pygame.mouse.get_pos()
            self.current_x = pos[0]
            self.current_y = pos[1]
    
            #for each spite in grid
                #if self.sprite.collidepoint(pos):
                    #function to only allow piece to move one space adjacent

    def place_piece_on_grid(self, position):
        if position == "00":
            self.stack_0_0.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "10":
            self.stack_1_0.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "20":
            self.stack_2_0.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "30":
            self.stack_3_0.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "40":
            self.stack_4_0.append(self.sprite_click_list.pop())
            self.end_turn()
        
        elif position == "01":
            self.stack_0_1.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "11":
            self.stack_1_1.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "21":
            self.stack_2_1.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "31":
            self.stack_3_1.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "41":
            self.stack_4_1.append(self.sprite_click_list.pop())
            self.end_turn()
            
        elif position == "02":
            self.stack_0_2.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "12":
            self.stack_1_2.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "22":
            self.stack_2_2.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "32":
            self.stack_3_2.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "42":
            self.stack_4_2.append(self.sprite_click_list.pop())
            self.end_turn()

        elif position == "03":
            self.stack_0_3.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "13":
            self.stack_1_3.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "23":
            self.stack_2_3.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "33":
            self.stack_3_3.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "43":
            self.stack_4_3.append(self.sprite_click_list.pop())
            self.end_turn()
        
        elif position == "04":
            self.stack_0_4.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "14":
            self.stack_1_4.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "24":
            self.stack_2_4.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "34":
            self.stack_3_4.append(self.sprite_click_list.pop())
            self.end_turn()
        elif position == "44":
            self.stack_4_4.append(self.sprite_click_list.pop())
            self.end_turn()

        self.click_count = 0
    
    def end_turn(self):
        ################################set up for the mark grid method############################################
        
        #create the local info for each stacks
        stack_0_0_info = []
        stack_0_1_info = []
        stack_0_2_info = []
        stack_0_3_info = []
        stack_0_4_info = []
        stack_1_0_info = []
        stack_1_1_info = []
        stack_1_2_info = []
        stack_1_3_info = []
        stack_1_4_info = []
        stack_2_0_info = []
        stack_2_1_info = []
        stack_2_2_info = []
        stack_2_3_info = []
        stack_2_4_info = []
        stack_3_0_info = []
        stack_3_1_info = []
        stack_3_2_info = []
        stack_3_3_info = []
        stack_3_4_info = []
        stack_4_0_info = []
        stack_4_1_info = []
        stack_4_2_info = []
        stack_4_3_info = []
        stack_4_4_info = []
        
        #if there's something in the stack
        if len(self.stack_0_0) > 0:
            #append the position
            stack_0_0_info.append("00")
            #append the name of the top stone
            stack_0_0_info.append(self.stack_0_0[len(self.stack_0_0) - 1].name)
            #append the color of the top stone
            stack_0_0_info.append(self.stack_0_0[len(self.stack_0_0) - 1].color)
        else:
            #append the position
            stack_0_0_info.append("00")
            #append nothing as it is an empty stack
            stack_0_0_info.append("")
            #append nothing as it is an empty stack
            stack_0_0_info.append("")
                        
        if len(self.stack_0_1) > 0:
            stack_0_1_info.append("01")
            stack_0_1_info.append(self.stack_0_1[len(self.stack_0_1) - 1].name)
            stack_0_1_info.append(self.stack_0_1[len(self.stack_0_1) - 1].color)
        else:
            stack_0_1_info.append("01")
            stack_0_1_info.append("")
            stack_0_1_info.append("")
                        
        if len(self.stack_0_2) > 0:
            stack_0_2_info.append("02")
            stack_0_2_info.append(self.stack_0_2[len(self.stack_0_2) - 1].name)
            stack_0_2_info.append(self.stack_0_2[len(self.stack_0_2) - 1].color)
        else:
            stack_0_2_info.append("02")
            stack_0_2_info.append("")
            stack_0_2_info.append("")
                
        if len(self.stack_0_3) > 0:
            stack_0_3_info.append("03")
            stack_0_3_info.append(self.stack_0_3[len(self.stack_0_3) - 1].name)
            stack_0_3_info.append(self.stack_0_3[len(self.stack_0_3) - 1].color)
        else:
            stack_0_3_info.append("03")
            stack_0_3_info.append("")
            stack_0_3_info.append("")
                        
        if len(self.stack_0_4) > 0:
            stack_0_4_info.append("04")
            stack_0_4_info.append(self.stack_0_4[len(self.stack_0_4) - 1].name)
            stack_0_4_info.append(self.stack_0_4[len(self.stack_0_4) - 1].color)
        else:
            stack_0_4_info.append("04")
            stack_0_4_info.append("")
            stack_0_4_info.append("")
                        
        if len(self.stack_1_0) > 0:
            stack_1_0_info.append("10")
            stack_1_0_info.append(self.stack_1_0[len(self.stack_1_0) - 1].name)
            stack_1_0_info.append(self.stack_1_0[len(self.stack_1_0) - 1].color)
        else:
            stack_1_0_info.append("10")
            stack_1_0_info.append("")
            stack_1_0_info.append("")
                    
        if len(self.stack_1_1) > 0:
            stack_1_1_info.append("11")
            stack_1_1_info.append(self.stack_1_1[len(self.stack_1_1) - 1].name)
            stack_1_1_info.append(self.stack_1_1[len(self.stack_1_1) - 1].color)
        else:
            stack_1_1_info.append("11")
            stack_1_1_info.append("")
            stack_1_1_info.append("")
                        
        if len(self.stack_1_2) > 0:
            stack_1_2_info.append("12")
            stack_1_2_info.append(self.stack_1_2[len(self.stack_1_2) - 1].name)
            stack_1_2_info.append(self.stack_1_2[len(self.stack_1_2) - 1].color)
        else:
            stack_1_2_info.append("12")
            stack_1_2_info.append("")
            stack_1_2_info.append("")
                        
        if len(self.stack_1_3) > 0:
            stack_1_3_info.append("13")
            stack_1_3_info.append(self.stack_1_3[len(self.stack_1_3) - 1].name)
            stack_1_3_info.append(self.stack_1_3[len(self.stack_1_3) - 1].color)
        else:
            stack_1_3_info.append("13")
            stack_1_3_info.append("")
            stack_1_3_info.append("")
            
        if len(self.stack_1_4) > 0:
            stack_1_4_info.append("14")
            stack_1_4_info.append(self.stack_1_4[len(self.stack_1_4) - 1].name)
            stack_1_4_info.append(self.stack_1_4[len(self.stack_1_4) - 1].color)
        else:
            stack_1_4_info.append("14")
            stack_1_4_info.append("")
            stack_1_4_info.append("")
                        
        if len(self.stack_2_0) > 0:
            stack_2_0_info.append("20")
            stack_2_0_info.append(self.stack_2_0[len(self.stack_2_0) - 1].name)
            stack_2_0_info.append(self.stack_2_0[len(self.stack_2_0) - 1].color)
        else:
            stack_2_0_info.append("20")
            stack_2_0_info.append("")
            stack_2_0_info.append("")
                        
        if len(self.stack_2_1) > 0:
            stack_2_1_info.append("21")
            stack_2_1_info.append(self.stack_2_1[len(self.stack_2_1) - 1].name)
            stack_2_1_info.append(self.stack_2_1[len(self.stack_2_1) - 1].color)
        else:
            stack_2_1_info.append("21")
            stack_2_1_info.append("")
            stack_2_1_info.append("")
                        
        if len(self.stack_2_2) > 0:
            stack_2_2_info.append("22")
            stack_2_2_info.append(self.stack_2_2[len(self.stack_2_2) - 1].name)
            stack_2_2_info.append(self.stack_2_2[len(self.stack_2_2) - 1].color)
        else:
            stack_2_2_info.append("22")
            stack_2_2_info.append("")
            stack_2_2_info.append("")
                        
        if len(self.stack_2_3) > 0:
            stack_2_3_info.append("23")
            stack_2_3_info.append(self.stack_2_3[len(self.stack_2_3) - 1].name)
            stack_2_3_info.append(self.stack_2_3[len(self.stack_2_3) - 1].color)
        else:
            stack_2_3_info.append("23")
            stack_2_3_info.append("")
            stack_2_3_info.append("")
                
        if len(self.stack_2_4) > 0:
            stack_2_4_info.append("24")
            stack_2_4_info.append(self.stack_2_4[len(self.stack_2_4) - 1].name)
            stack_2_4_info.append(self.stack_2_4[len(self.stack_2_4) - 1].color)
        else:
            stack_2_4_info.append("24")
            stack_2_4_info.append("")
            stack_2_4_info.append("")
                        
        if len(self.stack_3_0) > 0:
            stack_3_0_info.append("30")
            stack_3_0_info.append(self.stack_3_0[len(self.stack_3_0) - 1].name)
            stack_3_0_info.append(self.stack_3_0[len(self.stack_3_0) - 1].color)
        else:
            stack_3_0_info.append("30")
            stack_3_0_info.append("")
            stack_3_0_info.append("")
                        
        if len(self.stack_3_1) > 0:
            stack_3_1_info.append("31")
            stack_3_1_info.append(self.stack_3_1[len(self.stack_3_1) - 1].name)
            stack_3_1_info.append(self.stack_3_1[len(self.stack_3_1) - 1].color)
        else:
            stack_3_1_info.append("31")
            stack_3_1_info.append("")
            stack_3_1_info.append("")

        if len(self.stack_3_2) > 0:
            stack_3_2_info.append("32")
            stack_3_2_info.append(self.stack_3_2[len(self.stack_3_2) - 1].name)
            stack_3_2_info.append(self.stack_3_2[len(self.stack_3_2) - 1].color)
        else:
            stack_3_2_info.append("32")
            stack_3_2_info.append("")
            stack_3_2_info.append("")
                        
        if len(self.stack_3_3) > 0:
            stack_3_3_info.append("33")
            stack_3_3_info.append(self.stack_3_3[len(self.stack_3_3) - 1].name)
            stack_3_3_info.append(self.stack_3_3[len(self.stack_3_3) - 1].color)
        else:
            stack_3_3_info.append("33")
            stack_3_3_info.append("")
            stack_3_3_info.append("")

        if len(self.stack_3_4) > 0:
            stack_3_4_info.append("34")
            stack_3_4_info.append(self.stack_3_4[len(self.stack_3_4) - 1].name)
            stack_3_4_info.append(self.stack_3_4[len(self.stack_3_4) - 1].color)
        else:
            stack_3_4_info.append("34")
            stack_3_4_info.append("")
            stack_3_4_info.append("")
                        
        if len(self.stack_4_0) > 0:
            stack_4_0_info.append("40")
            stack_4_0_info.append(self.stack_4_0[len(self.stack_4_0) - 1].name)
            stack_4_0_info.append(self.stack_4_0[len(self.stack_4_0) - 1].color)
        else:
            stack_4_0_info.append("40")
            stack_4_0_info.append("")
            stack_4_0_info.append("")

        if len(self.stack_4_1) > 0:
            stack_4_1_info.append("41")
            stack_4_1_info.append(self.stack_4_1[len(self.stack_4_1) - 1].name)
            stack_4_1_info.append(self.stack_4_1[len(self.stack_4_1) - 1].color)
        else:
            stack_4_1_info.append("41")
            stack_4_1_info.append("")
            stack_4_1_info.append("")

        if len(self.stack_4_2) > 0:
            stack_4_2_info.append("42")
            stack_4_2_info.append(self.stack_4_2[len(self.stack_4_2) - 1].name)
            stack_4_2_info.append(self.stack_4_2[len(self.stack_4_2) - 1].color)
        else:
            stack_4_2_info.append("42")
            stack_4_2_info.append("")
            stack_4_2_info.append("")
                        
        if len(self.stack_4_3) > 0:
            stack_4_3_info.append("43")
            stack_4_3_info.append(self.stack_4_3[len(self.stack_4_3) - 1].name)
            stack_4_3_info.append(self.stack_4_3[len(self.stack_4_3) - 1].color)
        else:
            stack_4_3_info.append("43")
            stack_4_3_info.append("")
            stack_4_3_info.append("")

        if len(self.stack_4_4) > 0:
            stack_4_4_info.append("44")
            stack_4_4_info.append(self.stack_4_4[len(self.stack_4_4) - 1].name)
            stack_4_4_info.append(self.stack_4_4[len(self.stack_4_4) - 1].color)
        else:
            stack_4_4_info.append("44")
            stack_4_4_info.append("")
            stack_4_4_info.append("")
        
        #Send current snapshot to data model
        self.board_model.mark_grid(stack_0_0_info, stack_0_1_info, stack_0_2_info, stack_0_3_info, stack_0_4_info, stack_1_0_info, stack_1_1_info, stack_1_2_info, stack_1_3_info, stack_1_4_info, stack_2_0_info, stack_2_1_info, stack_2_2_info, stack_2_3_info, stack_2_4_info, stack_3_0_info, stack_3_1_info, stack_3_2_info, stack_3_3_info, stack_3_4_info, stack_4_0_info, stack_4_1_info,  stack_4_2_info, stack_4_3_info, stack_4_4_info)
                        

################################End of piece placements/Victory checks/Player switch####################################
        if self.current_player == self.player1:
            if self.board_model.check_victory("1f"):
                self.done = True
                self.winner = "Player One"
                self.p1_wins += 1
                self.p1_score += (25 + self.player1.stones)
            else:
                self.current_player = self.player2
        else:
            if self.board_model.check_victory("2f"):
                self.done = True
                self.winner = "Player Two"
                self.p2_wins += 1
                self.p2_score += (25 + self.player2.stones)
            else:
                self.current_player = self.player1
        print(self.winner)
    
    def draw(self, screen):
        seconds = self.seconds
        minutes = self.minutes
        self.board_list.draw(screen)
        self.all_sprites_list.draw(screen)

        title_string = 'Let\'s play Tak!'
        reset_string = 'Reset'
        font = pygame.font.SysFont('Helvetica', 15, True, False)

        title_text = font.render(title_string, True, BLACK)
        reset_button_text = font.render(reset_string, True, BLACK)
        timer = font.render('Time:  ' + str(str(minutes) + ":" + str(seconds)), True, BLACK)

        player_turn = font.render(self.current_player.name + "\'s Turn.", True, BLACK)
        player1_pieces_remaining = font.render("Remaining stones: " + str(self.player1.stones), True, BLACK)
        player1_capstone_remaining = font.render("Remaining capstones: " + str(self.player1.capstones), True, BLACK)
        player2_pieces_remaining = font.render("Remaining stones: " + str(self.player2.stones), True, BLACK)
        player2_capstone_remaining = font.render("Remaining capstones: " + str(self.player2.capstones), True, BLACK)

        player_1_wins = font.render("Wins: " + str(self.p1_wins), True, BLACK)
        player_2_wins = font.render("Wins: " + str(self.p2_wins), True, BLACK)
        player1_score = font.render("Score: " + str(self.p1_score), True, BLACK)
        player2_score = font.render("Score: " + str(self.p2_score), True, BLACK)

        win_message = font.render(self.winner + " has won! Hit the Reset button to play again!", True, BLACK)

        screen.blit(title_text, [SCREEN_WIDTH / 2 - 80, 10])
        screen.blit(timer, [SCREEN_WIDTH/2 - 80, 30])

        if not self.done:
            screen.blit(player_turn, [SCREEN_WIDTH/2 - 80, 50])

        screen.blit(player1_pieces_remaining, [(SCREEN_WIDTH / 6) - 130, SCREEN_HEIGHT / 2 + 75])
        screen.blit(player2_pieces_remaining, [(SCREEN_WIDTH / 6 * 5) - 30, SCREEN_HEIGHT / 2 + 75])

        if self.capstone_total > 0:
            screen.blit(player1_capstone_remaining, [(SCREEN_WIDTH / 6) - 130, SCREEN_HEIGHT / 2 + 350])
            screen.blit(player2_capstone_remaining, [(SCREEN_WIDTH / 6 * 5) - 30, SCREEN_HEIGHT / 2 + 350])

        if self.done:
            screen.blit(win_message, [SCREEN_WIDTH/2-80, 50])

        if self.p1_wins > 0:
            screen.blit(player_1_wins, [(SCREEN_WIDTH / 6) - 80, 200])
        if self.p2_wins > 0:
            screen.blit(player_2_wins, [(SCREEN_WIDTH / 6 * 5) + 30, 200])

        if self.p1_score > 0:
            screen.blit(player1_score, [(SCREEN_WIDTH /6 - 80), 250])

        if self.p2_score > 0:
            screen.blit(player2_score, [(SCREEN_WIDTH /6 * 5) + 30, 250])

        pygame.draw.rect(screen, [255, 0, 0], self.button)
        screen.blit(reset_button_text, [75, SCREEN_HEIGHT - 40])
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
