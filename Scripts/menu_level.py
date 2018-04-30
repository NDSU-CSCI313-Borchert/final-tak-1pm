import pygame
from constants import *
from level_manager import *
from title_screen import *
from game_level import *
from board import *

class MenuLevel():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        # we will join the dimension and design, which will act as a
        # key when calling the art class

        self.sizes = ["5x5", "4x4", "3x3"]
        self.designs = ["Yellow", "Brown", "Summerbreeze", "Space"]

        self.size_index = 0
        self.design_index = 0

        self.preview_list = pygame.sprite.Group()

        self.preview = "3x3" + str(self.designs[0])
        
        self.board = Board(self.preview)
        self.board.rect.center = (SCREEN_CENTER)
        self.preview_list.add(self.board)

    def update(self):
        pass

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
            elif event.key == pygame.K_s:
                if self.size_index < len(self.sizes)-1:
                    self.size_index += 1
                else:
                    self.size_index = 0
            elif event.key == pygame.K_d:
                if self.design_index < len(self.designs)-1:
                    self.design_index += 1
                else:
                    self.design_index = 0
                self.preview = "3x3" + str(self.designs[self.design_index])
                self.board = Board(self.preview)
                self.board.rect.center = (SCREEN_CENTER)
                self.preview_list.add(self.board)
            elif event.key == pygame.K_p:
                LevelManager().load_level(GameLevel(size=self.sizes[self.size_index], design=self.designs[self.design_index]))


    def draw(self, screen):
        screen.fill(WHITE)

        self.preview_list.draw(screen)
        
        header_string = "Board Settings:"
        size_string = "Board [S]ize: " + str(self.sizes[self.size_index])
        design_string = "Board [D]esign: " + str(self.designs[self.design_index])
        progress_string = "ESC to go back, P to play."

        head_font = pygame.font.SysFont("Helvetica", 30, True, False)
        font = pygame.font.SysFont("Helvetica", 20, True, False)

        head_text = head_font.render(header_string, True, BLACK)
        size_text = font.render(size_string, True, BLACK)
        design_text = font.render(design_string, True, BLACK)
        progress_text = head_font.render(progress_string, True, BLACK)

        screen.blit(head_text, [(SCREEN_WIDTH/2)-100, 50])
        screen.blit(size_text, [(SCREEN_WIDTH/2)-100, 300])
        screen.blit(design_text, [(SCREEN_WIDTH/2)-100, 400])
        screen.blit(progress_text, [(SCREEN_WIDTH/2)-100, SCREEN_HEIGHT-300])


        pygame.display.flip()
