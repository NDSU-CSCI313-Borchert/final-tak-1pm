"""
    
    Author: Skyler Svendsen
"""
import pygame
import random
from constants import *
from board import *
from player import *
from stone import *
from capstone import *
from level_manager import *
from title_screen import *

import pygame.time

class GameLevel():
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        # Set the height and width of the screen
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        
        # These are lists of 'sprites.' Each block in the program is
        # added to this list. The list is managed by a class called 'Group.'

        # This is a list of every sprite.
        # All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()
        
        
        level_manager = LevelManager()
        
        self.done = False
        
        # Create the board
        board = Board("5x5")
        board.rect.x = (SCREEN_WIDTH / 4)
        board.rect.y = (SCREEN_HEIGHT / 6)
        self.all_sprites_list.add(board)
        
        # Create the players
        self.player1 = Player()
        self.player1.name = "Player One"
        self.player2 = Player()
        self.player2.name = "Player Two"
        
        #Create the pieces
        self.player1pieces = []
        for i in range(0, 20):
            stone = Stone("brown_stone")
            stone.rect.x = (SCREEN_WIDTH / 6) - 100
            stone.rect.y = (SCREEN_HEIGHT / 2)
            self.all_sprites_list.add(stone)
            self.player1pieces.append(stone)
        
        self.player2pieces = []
        for i in range(0, 20):
            stone = Stone("beige_stone")
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

        self.grid = []

        for row in range(5):
            self.grid.append([])
            for column in range(5):
                self.grid[row].append(0)

        self.current_x = 0
        self.current_y = 0



#    def handle_keyboard_event(self, event):
#        if event.type == pygame.KEYDOWN:
#            # An argument can be made to place leaving the level in the main loop
#            if event.key == pygame.K_ESCAPE:
#                LevelManager().leave_level()
    #Check if the player has made a road to the other side of the board and won. I am thinking when a player puts a piece down we can mark that spot in the grid.
    def Check_victory(self,board):
        for y in range(0,5):
            if board[0][y] ==('X') and board[1][y] ==('X') and board[2][y] ==('X') and board[3][y] ==('X') and board[4][y] ==('X'):
                return True
            if board[0][y] == ('Y') and board[1][y] == ('Y') and board[2][y] == ('Y') and board[3][y] == ('Y') and board[4][y] == ('Y'):
                return True
        return False
    def print_pos(self):
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        print (x, y)
    

    #No need to do anything here, unless we've got some animation
    def update(self):

        counting_time = pygame.time.get_ticks() - self.start_time

        self.minutes = str(int(counting_time/60000)).zfill(2)
        self.seconds = str(int((counting_time%60000)/1000)).zfill(2)

        self.screen.fill(WHITE)
        
        pos = pygame.mouse.get_pos()
        
        diff_x = self.current_x - pos[0]
        diff_y = self.current_y - pos[1]
        
        for sprite in self.sprite_click_list:
            sprite.rect.x -= diff_x
            sprite.rect.y -= diff_y

        self.all_sprites_list.update()
        if self.Check_victory(self.grid):
            print("Congratulations you won this round of Tak")


    def handle_keyboard_event(self, event):

        if event.type == pygame.KEYDOWN:
            # An argument can be made to place leaving the level in the main loop
            if event.key == pygame.K_SPACE:
                if self.current_player == self.player1:
                    self.current_player = self.player2
                else:
                    self.current_player = self.player1
            elif event.key == pygame.K_r:
                LevelManager().load_level(GameLevel())
            elif event.key == pygame.K_ESCAPE:
                LevelManager.leave_level()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            self.current_x = pos[0]
            self.current_y = pos[1]

            if self.player1.stones > 0:
                p1top = self.player1pieces[0]
                print ("p1x: " + str(p1top.rect.x))
                print ("p1y: " + str(p1top.rect.y))
                    
                if p1top.rect.collidepoint(pos):
                    self.player1.removeStone()
                    self.sprite_click_list.append(self.player1pieces.pop())
                    print ("Piece added")
                        
            if self.player2.stones > 0:
                p2top = self.player2pieces[0]
                print (p2top.rect.x)
                print (p2top.rect.y)


#self.sprite_click_list = [s for s in self.all_sprites_list if s.rect.collidepoint(pos)]
            
            #if self.current_x == p1top.rect.x and self.current_y == p1top.rect.y and player1.stones > 0:
            #if self.player1.stones > 0:
#            if pygame.mouse.get_pressed()[0] and p1top.rect.collidepoint(pygame.mouse.get_pos()):
#                self.player1.removeStone()
#                self.sprite_click_list.append(self.player1pieces.pop())
#                print ("piece added")
#            elif self.current_x == p2top.rect.x and self.current_y == p2top.rect.y and player2.stones > 0:
#                player2.removeStone()
#                self.sprite_click_list.append(player2pieces.pop())
#                print ("piece added")


        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    def draw(self, screen):
        seconds = self.seconds
        minutes = self.minutes
        self.all_sprites_list.draw(screen)

        title_string = 'Let\'s play Tak!'
        font = pygame.font.SysFont('Helvetica', 15, True, False)
        title_text = font.render(title_string, True, BLACK)
        timer = font.render('Time:  ' + str(str(minutes) + ":" + str(seconds)), True, BLACK)
        player_turn = font.render(self.current_player.name + "\'s Turn.", True, BLACK)
        player1_pieces_remaining = font.render("Remaining stones: " + str(self.player1.stones), True, BLACK)
        player2_pieces_remaining = font.render("Remaining stones: " + str(self.player2.stones), True, BLACK)
        screen.blit(title_text, [SCREEN_WIDTH / 2 - 80, 10])
        screen.blit(timer, [SCREEN_WIDTH/2 - 80, 30])
        screen.blit(player_turn, [SCREEN_WIDTH/2 - 80, 50])
        screen.blit(player1_pieces_remaining, [(SCREEN_WIDTH / 6) - 130, SCREEN_HEIGHT / 2 + 75])
        screen.blit(player1_pieces_remaining, [(SCREEN_WIDTH / 6 * 5) - 30, SCREEN_HEIGHT / 2 + 75])
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
