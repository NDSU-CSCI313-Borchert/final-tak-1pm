import pygame

pygame.init()

art_dictionary = {"5x5": "5_5_Blue_Yellow.png"}


class Art:
    def __init__(self, screen, color, level="Game Level"):
        global art_dictionary

        screen.fill(color)
        if level == "Game Level":
            art_dict = {"5x5": "5_5_Blue_Yellow.png"}

        art_dictionary = art_dict

    def get_image(image_request):
        image_needed = art_dictionary.get(str(image_request))
        return pygame.image.load(image_needed)
