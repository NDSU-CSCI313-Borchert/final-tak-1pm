import pygame
from art import *

class Stone(pygame.sprite.Sprite):
    def __init__(self, sprite1, sprite2):
        super().__init__()
        self.images = []
        self.images.append(Art.get_image(sprite1))
        self.images.append(Art.get_image(sprite2))
        
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
    
        if self.index == 0:
            self.name = "flat"
        else:
            self.name = "wall"

    def flipStone(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        if self.index == 0:
            self.name = "flat"
        else:
            self.name = "wall"
