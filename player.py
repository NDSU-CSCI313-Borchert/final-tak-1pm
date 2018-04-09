import pygame
from art import *

class Player():
    def __init__(self):
        super().__init__()

        self.stones = 21
        self.capstones = 1

    def removeStone(self):
        if self.stones > 0:
            self.stones -= 1

    def removeCapstone(self):
        if self.capstones > 0:
            self.capstones -= 1
