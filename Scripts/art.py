import pygame
import os

pygame.init()

art_dictionary = {"5x5": "5_5_Blue_Yellow.png", "brown_stone": "Stone_Brown.png", "beige_stone": "Stone_Beige.png", "brown_capstone": "Capstone_Brown.png", "beige_capstone": "Capstone_Beige.png"}


class Art:
    def __init__(self, screen, color, level="Game Level"):
        global art_dictionary

        screen.fill(color)
        if level == "Game Level":
            art_dict = {"5x5": "5_5_Blue_Yellow.png", "brown_stone": "Stone_Brown.png", "beige_stone": "Stone_Beige.png", "brown_capstone": "Capstone_Brown.png", "beige_capstone": "Capstone_Beige.png"}

        art_dictionary = art_dict

    def get_image(image_request):
        os.chdir("..")
        os.chdir("Assets")

        image_needed = art_dictionary.get(str(image_request))
        return pygame.image.load(image_needed)
