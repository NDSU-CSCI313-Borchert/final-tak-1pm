"""
    
    Author: Skyler Svendsen
"""
import pygame
import random
from constants import *
from board import *
from level_manager import *
from title_screen import *

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
        board.rect.x = (SCREEN_WIDTH / 2)
        board.rect.y = (SCREEN_HEIGHT / 2)
        self.all_sprites_list.add(board)



        # Loop until the user clicks the close button.
        done = False
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        
        
    
    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            # An argument can be made to place leaving the level in the main loop
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()

    #No need to do anything here, unless we've got some animation
    def update(self):
        self.screen.fill(WHITE)
        
        self.all_sprites_list.update()

    def draw(self, screen):
        self.all_sprites_list.draw(screen)
        title_string = 'Let\'s play Tak!'
        font = pygame.font.SysFont('Helvetica', 15, True, False)
        text = font.render(title_string, True, BLACK)
        screen.blit(text, [10, 10])
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
