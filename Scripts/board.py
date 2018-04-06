import pygame
from art import *

class Board(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super().__init__()

        self.image = Art.get_image(sprite)

        self.rect = self.image.get_rect()
