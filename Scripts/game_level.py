"""
    
    Author: Skyler Svendsen
"""
import pygame
import random
from constants import *
from board import *
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

        # Loop until the user clicks the close button.
        done = False
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.start_time = pygame.time.get_ticks()

        self.current_player = "Player One"

        self.grid = []

        for row in range(5):
            self.grid.append([])
            for column in range(5):
                self.grid[row].append(0)
        
    
    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            # An argument can be made to place leaving the level in the main loop
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()

    #No need to do anything here, unless we've got some animation
    def update(self):

        counting_time = pygame.time.get_ticks() - self.start_time

        self.minutes = str(int(counting_time/60000)).zfill(2)
        self.seconds = str(int((counting_time%60000)/1000)).zfill(2)

        self.screen.fill(WHITE)
        
        self.all_sprites_list.update()

    def handle_keyboard_event(self, event):

        if event.type == pygame.KEYDOWN:
            # An argument can be made to place leaving the level in the main loop
            if event.key == pygame.K_SPACE:
                if self.current_player == "Player One":
                    self.current_player = "Player Two"
                else:
                    self.current_player = "Player One"
            elif event.key == pygame.K_r:
                LevelManager.load_level(GameLevel())

    def draw(self, screen):
        seconds = self.seconds
        minutes = self.minutes
        self.all_sprites_list.draw(screen)

        title_string = 'Let\'s play Tak!'
        font = pygame.font.SysFont('Helvetica', 15, True, False)
        text = font.render(title_string, True, BLACK)
        timer = font.render('Time:  ' + str(str(minutes) + ":" + str(seconds)), True, BLACK)
        player_turn = font.render(self.current_player + "\'s Turn.", True, BLACK)
        screen.blit(text, [10, 10])
        screen.blit(timer, [SCREEN_WIDTH/2, 10])
        screen.blit(player_turn, [SCREEN_WIDTH/2, 40])
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
