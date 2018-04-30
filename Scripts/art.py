import pygame
import os

pygame.init()

art_dictionary = {"5x5Brown": "5x5Brown.png", "4x4Brown": "4x4Brown.png", "3x3Brown": "3x3Brown.png",
                  "5x5Yellow": "5x5Yellow.png", "4x4Yellow": "4x4Yellow.png", "3x3Yellow": "3x3Yellow.png",
                  "5x5Summerbreeze": "5x5Summerbreeze.png", "4x4Summerbreeze": "4x4Summerbreeze.png",
                  "3x3Summerbreeze": "3x3Summerbreeze.png",
                  "5x5Space": "5x5Space.png", "4x4Space": "4x4Space.png", "3x3Space": "3x3Space.png",
                  "brown_stone": "Stone_Brown.png", "beige_stone": "Stone_Beige.png",
                  "brown_capstone": "Capstone_Brown.png", "beige_capstone": "Capstone_Beige.png",
                  "brown_wall": "Standing_Brown.png", "beige_wall": "Standing_Beige.png"}


class Art:
    def __init__(self, screen, color, level="Game Level"):
        global art_dictionary

        screen.fill(color)
        if level == "Game Level":
            art_dict = {"5x5Brown": "5x5Brown.png", "4x4Brown": "4x4Brown.png", "3x3Brown": "3x3Brown.png",
                          "5x5Yellow": "5x5Yellow.png", "4x4Yellow": "4x4Yellow.png", "3x3Yellow": "3x3Yellow.png",
                          "5x5Summerbreeze": "5x5Summerbreeze.png", "4x4Summerbreeze": "4x4Summerbreeze.png",
                          "3x3Summerbreeze": "3x3Summerbreeze.png",
                          "5x5Space": "5x5Space.png", "4x4Space": "4x4Space.png", "3x3Space": "3x3Space.png",
                          "brown_stone": "Stone_Brown.png", "beige_stone": "Stone_Beige.png",
                          "brown_capstone": "Capstone_Brown.png", "beige_capstone": "Capstone_Beige.png",
                          "brown_wall": "Standing_Brown.png", "beige_wall": "Standing_Beige.png"}

        art_dictionary = art_dict

    def get_image(image_request):
        image_needed = art_dictionary.get(str(image_request))
        path = os.path.join("../Assets/", str(image_needed))
        return pygame.image.load(path)
