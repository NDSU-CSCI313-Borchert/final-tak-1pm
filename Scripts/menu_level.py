import pygame
from constants import *
from level_manager import *
from title_screen import *
from game_level import *

class MenuLevel():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        # we will join the dimension and design, which will act as a
        # key when calling the art class

        self.sizes = ["5x5", "4x4", "3x3"]
        self.designs = ["Blue", "Brown", "Summerbreeze"]

        self.size_index = 0
        self.design_index = 0

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager.leave_level()
            elif event.key == pygame.K_s:
                if self.size_index < self.sizes.len():
                    self.size_index += 1
                else:
                    self.size_index = 0
            elif event.key == pygame.K_d:
                if self.design_index < self.designs.len():
                    self.design_index += 1
                else:
                    self.design_index = 0
            elif event.key == pygame.K_p:
                LevelManager.load_level(GameLevel(size=self.sizes[self.size_index]), design=self.designs[self.design_index])


    def draw(self, screen):
        header_string = "Board Settings:"
        size_string = "Board [S]ize: " + str(self.sizes[self.size_index])
        design_string = "Board [D]esign: " + str(self.designs[self.design_index])
        progress_string = "ESC to go back, P to play."

        head_font = pygame.font.SysFont("Helvetica", 30, True, False)
        font = pygame.font.SysFont("Helvetica", 20, True, False)

        head_text = head_font.render(header_string, True, BLACK)
        size_text = font.render(size_string, True, BLACK)
        design_text = font.render(design_string, True, BLACK)
        progress_text = font.render(progress_string, True, BLACK)

        screen.blit(head_text, [(SCREEN_WIDTH/2)-40, 50])
        screen.blit(size_text, [SCREEN_WIDTH/2, 300])
        screen.blit(design_text, [SCREEN_WIDTH/2, 400])
        screen.blit(progress_text, [(SCREEN_WIDTH/2)-100, SCREEN_HEIGHT-50])


        pygame.display.flip()