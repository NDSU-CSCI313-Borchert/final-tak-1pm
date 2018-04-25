"""
    
    Author: Skyler Svendsen
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
        
        # Create the board
        board = Board("5x5_Brown")
        board.rect.x = (SCREEN_WIDTH / 4)
        board.rect.y = (SCREEN_HEIGHT / 6)
        self.board_list.add(board)
        self.board_model = BoardModel(SCREEN_WIDTH/4, SCREEN_HEIGHT/6)
        
        # Create the players
        self.player1 = Player()
        self.player1.name = "Player One"
        self.player2 = Player()
        self.player2.name = "Player Two"
        
        #Create the pieces
        self.player1pieces = []
        for i in range(0, 20):
            stone = Stone("brown_stone", "brown_wall")
            stone.rect.x = (SCREEN_WIDTH / 6) - 100
            stone.rect.y = (SCREEN_HEIGHT / 2)
            self.all_sprites_list.add(stone)
            self.player1pieces.append(stone)
        
        self.player2pieces = []
        for i in range(0, 20):
            stone = Stone("beige_stone", "beige_wall")
            stone.rect.x = (SCREEN_WIDTH / 6 * 5)
            stone.rect.y = (SCREEN_HEIGHT / 2)
            self.all_sprites_list.add(stone)
            self.player2pieces.append(stone)

        self.size = size
        self.design = design
        
        #Create the capstones
        self.player1capstone = Capstone("brown_capstone")
        self.player1capstone.rect.x = (SCREEN_WIDTH / 6) - 95
        self.player1capstone.rect.y = (SCREEN_HEIGHT / 2) + 150
        self.all_sprites_list.add(self.player1capstone)
        
        self.player2capstone = Capstone("beige_capstone")
        self.player2capstone.rect.x = ((SCREEN_WIDTH / 6 * 5) - 0)
        self.player2capstone.rect.y = (SCREEN_HEIGHT / 2) + 150
        self.all_sprites_list.add(self.player2capstone)
        
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
            #if self.Check_victory(self.grid):
            #print("Congratulations you won this round of Tak")


    def handle_keyboard_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                LevelManager.leave_level()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_CLICK:

            print ("Left click")

            pos = pygame.mouse.get_pos()
            self.current_x = pos[0]
            self.current_y = pos[1]

            if self.button.collidepoint(pos):
                LevelManager().load_level(GameLevel(self.p1_wins, self.p2_wins, self.p1_score, self.p2_score))

            #No piece picked up
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
                    p1top = self.player2capstone
                        
                    if p1top.rect.collidepoint(pos) and self.current_player == self.player2:
                        self.player2.removeCapstone()
                        self.sprite_click_list.append(self.player2capstone)
                        self.click_count += 1

            elif self.click_count == 1:
                if (SCREEN_WIDTH / 4) < self.current_x < 1129:
                    # This code helps the pieces snap in place
                    distance_to_snap = 130
                    stone = self.sprite_click_list[0]
                    px, py = stone.rect.topleft


                    if self.board_model.spot_occupied(px, py):
                        print("Occupied")
                        pass

                    else:
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

                        for cx, cy in self.board_model.coord_grid:
                            if math.hypot(cx-px, cy-py) < distance_to_snap:
                                stone.rect.x = cx+25
                                stone.rect.y = cy+45
                                break

                        self.sprite_click_list = []

                        self.click_count = 0

                        if self.current_player == self.player1:
                            if self.board_model.Check_victoryX():
                                self.done = True
                                self.winner = "Player One"
                                self.p1_wins += 1
                                self.p1_score += (25 + self.player1.stones)
                            else:
                                self.current_player = self.player2
                        else:
                            if self.board_model.Check_victoryY():
                                self.done = True
                                self.winner = "Player Two"
                                self.p2_wins += 1
                                self.p2_score += (25 + self.player2.stones)
                            else:
                                self.current_player = self.player1
                        print(self.winner)

                # Clicking while outside the board will toggle the piece between
                # road and wall
                else:
                    self.sprite_click_list[0].flipStone()
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT_CLICK:
            print ("Right click")

            pos = pygame.mouse.get_pos()
            self.current_x = pos[0]
            self.current_y = pos[1]
    
            #for each spite in grid
                #if self.sprite.collidepoint(pos):
                    #function to only allow piece to move one space adjacent



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
        screen.blit(player1_capstone_remaining, [(SCREEN_WIDTH / 6) - 130, SCREEN_HEIGHT / 2 + 175])
        screen.blit(player2_pieces_remaining, [(SCREEN_WIDTH / 6 * 5) - 30, SCREEN_HEIGHT / 2 + 75])
        screen.blit(player2_capstone_remaining, [(SCREEN_WIDTH / 6 * 5) - 30, SCREEN_HEIGHT / 2 + 175])

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
