import pygame
froms constants import *

class MenuLevel():
    def __init__(self):
        pygame.init

        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        # we will join the dimension and design, which will act as a
        # key when calling the art class

        sizes = ["5x5", "4x4", "3x3"]
        designs = ["Blue", "Brown", "Summerbreeze"]

        
        
