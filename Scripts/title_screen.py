import pygame
from constants import *
from level_manager import *
from game_level import *

class TitleScreen():
    def __init__(self):
        #Because this text never changes, we can load it in the constructor
        #Otherwise, we may need to move render into draw
        font = pygame.font.SysFont('Calibri', 25, True, False)
        pygame.init()

        #The underscore character indicates that this is a private instance variable
        self._text = font.render("404: Tak Game Not Found", True, BLACK)
        self._proceed = font.render("Press \"P\" to play or \"ESC\" to quit.", True, BLACK)
    
    def handle_keyboard_event(self, event):
        
        if event.type == pygame.KEYDOWN:
            # An argument can be made to place leaving the level in the main loop
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
            elif event.key == pygame.K_p:
                LevelManager().load_level(GameLevel())
            #elif event.key == pygame.K_c:
                #LevelManager().load_level(CreditsScreen())

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
    
    def draw(self, screen):
        # Clear the screen
        screen.fill(WHITE)
        
        # Draw my title text!
        screen.blit(self._text, [200, 200])
        screen.blit(self._proceed, [125, 350])
