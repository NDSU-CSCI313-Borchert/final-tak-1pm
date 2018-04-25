import pygame
import os

pygame.init()

art_dictionary = {"5x5_Brown": "5_5_Brown_Beige.png", "4x4_Brown": "4_4_Brown_Beige.png", "3x3_Brown":"3_3_Brown_Beige.png", "5x5_Blue":"5_5_Blue_Yellow.png", "4x4_Blue":"4_4_Blue_Yellow.png", "3x3_Blue":"3_3_Blue_Yellow.png", "5x5_Summer":"5_5_Summer_Breeze.png", "4x4_Summer":"4_4_Summer_Breeze.png", "3x3_Summer":"3_3_Summer_Breeze.png", "5x5_Space":"5_5_Space.png", "4x4_Space":"4_4_Space.png", "3x3_Space":"3_3_Space.png", "brown_stone": "Stone_Brown.png", "beige_stone": "Stone_Beige.png", "brown_capstone": "Capstone_Brown.png", "beige_capstone": "Capstone_Beige.png", "brown_wall": "Standing_Brown.png", "beige_wall": "Standing_Beige.png"}


class Art:
    def __init__(self, screen, color, level="Game Level"):
        global art_dictionary

        screen.fill(color)
        if level == "Game Level":
            art_dict = {"5x5_Brown": "5_5_Brown_Beige.png", "4x4_Brown": "4_4_Brown_Beige.png", "3x3_Brown":"3_3_Brown_Beige.png", "5x5_Blue":"5_5_Blue_Yellow.png", "4x4_Blue":"4_4_Blue_Yellow.png", "3x3_Blue":"3_3_Blue_Yellow.png", "5x5_Summer":"5_5_Summer_Breeze.png", "4x4_Summer":"4_4_Summer_Breeze.png", "3x3_Summer":"3_3_Summer_Breeze.png", "5x5_Space":"5_5_Space.png", "4x4_Space":"4_4_Space.png", "3x3_Space":"3_3_Space.png", "brown_stone": "Stone_Brown.png", "beige_stone": "Stone_Beige.png", "brown_capstone": "Capstone_Brown.png", "beige_capstone": "Capstone_Beige.png", "brown_wall": "Standing_Brown.png", "beige_wall": "Standing_Beige.png"}

        art_dictionary = art_dict

    def get_image(image_request):
        image_needed = art_dictionary.get(str(image_request))
        path = os.path.join("../Assets/", image_needed)
        return pygame.image.load(path)
