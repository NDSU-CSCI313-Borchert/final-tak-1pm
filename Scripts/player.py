import pygame
from art import *

class Player():
    def __init__(self, stones, capstones):
        super().__init__()

        self.stones = stones
        self.capstones = capstones

    def removeStone(self):
        if self.stones > 0:
            self.stones -= 1

    def removeCapstone(self):
        if self.capstones > 0:
            self.capstones -= 1
