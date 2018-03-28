import pygame
from constants import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,
                                  SCREEN_HEIGHT])

#first line in text is the title screen music


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

done = False

# -------- Main Program Loop -----------
while not done:

    #We've left the TitleScreen - Exit the game
    if current_level == None:
        break

    #Needs Game Logic

    # Update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break


pygame.quit()
