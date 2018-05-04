import pygame
from art import *

class Capstone(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super().__init__()
        self.image = Art.get_image(sprite)
        self.rect = self.image.get_rect()
        self.name = "capstone"

        if sprite == "brown_capstone":
            self.color = "brown"
        elif sprite == "beige_capstone":
            self.color = "beige"

