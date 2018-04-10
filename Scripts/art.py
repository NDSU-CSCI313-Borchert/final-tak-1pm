import pygame
import os

pygame.init()

art_dictionary = {"5x5": "5_5_Blue_Yellow.png", "brown_stone": "Stone_Brown.png", "beige_stone": "Stone_Beige.png", "brown_capstone": "Capstone_Brown.png", "beige_capstone": "Capstone_Beige.png", "brown_wall": "Standing_Brown.png", "beige_wall": "Standing_Beige.png"}


class Art:
    def __init__(self, screen, color, level="Game Level"):
        global art_dictionary

        screen.fill(color)
        if level == "Game Level":
            art_dict = {"5x5": "5_5_Blue_Yellow.png", "brown_stone": "Stone_Brown.png", "beige_stone": "Stone_Beige.png", "brown_capstone": "Capstone_Brown.png", "beige_capstone": "Capstone_Beige.png", "brown_wall": "Standing_Brown.png", "beige_wall": "Standing_Beige.png"}

        art_dictionary = art_dict

    def get_image(image_request):
        image_needed = art_dictionary.get(str(image_request))
        path = os.path.join("../Assets/", image_needed)
        return pygame.image.load(path)
