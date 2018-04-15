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
    def __init__(self, p1_wins=0, p2_wins=0):
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
        board = Board("5x5")
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

        self.winner = ""
        self.done = False


    #Animation
    def update(self):

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

        if event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()
            self.current_x = pos[0]
            self.current_y = pos[1]

            if self.button.collidepoint(pos):
                LevelManager().load_level(GameLevel(self.p1_wins, self.p2_wins))

            if self.click_count == 0:
                if self.player1.stones > 0:
                    p1top = self.player1pieces[0]

                    if p1top.rect.collidepoint(pos) and self.current_player == self.player1:
                        self.player1.removeStone()
                        self.sprite_click_list.append(self.player1pieces.pop())
                        self.click_count += 1

                if self.player2.stones > 0:
                    p2top = self.player2pieces[0]

                    if p2top.rect.collidepoint(pos) and self.current_player == self.player2:
                        self.player2.removeStone()
                        self.sprite_click_list.append(self.player2pieces.pop())
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
                            else:
                                self.current_player = self.player2
                        else:
                            if self.board_model.Check_victoryY():
                                self.done = True
                                self.winner = "Player Two"
                            else:
                                self.current_player = self.player1
                        print(self.winner)

                # Clicking while outside the board will toggle the piece between
                # road and wall
                else:
                    self.sprite_click_list[0].flipStone()



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
        player2_pieces_remaining = font.render("Remaining stones: " + str(self.player2.stones), True, BLACK)
        player_1_wins = font.render("Wins: " + str(self.p1_wins), True, BLACK)
        player_2_wins = font.render("Wins: " + str(self.p2_wins), True, BLACK)

        screen.blit(title_text, [SCREEN_WIDTH / 2 - 80, 10])
        screen.blit(timer, [SCREEN_WIDTH/2 - 80, 30])
        screen.blit(player_turn, [SCREEN_WIDTH/2 - 80, 50])

        screen.blit(player1_pieces_remaining, [(SCREEN_WIDTH / 6) - 130, SCREEN_HEIGHT / 2 + 75])
        screen.blit(player2_pieces_remaining, [(SCREEN_WIDTH / 6 * 5) - 30, SCREEN_HEIGHT / 2 + 75])

        if self.p1_wins > 0:
            screen.blit(player_1_wins, [(SCREEN_WIDTH / 6) - 80, 200])
        if self.p2_wins > 0:
            screen.blit(player_2_wins, [(SCREEN_WIDTH / 6 * 5) + 30, 200])

        pygame.draw.rect(screen, [255, 0, 0], self.button)
        screen.blit(reset_button_text, [75, SCREEN_HEIGHT - 40])
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
