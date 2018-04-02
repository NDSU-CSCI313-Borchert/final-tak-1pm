import pygame
from constants import *
from level_manager import *
from title_screen import *
from game_level import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,
                                  SCREEN_HEIGHT])

#first line in text is the title screen music


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

level_manager = LevelManager()
level_manager.load_level(TitleScreen())
current_level1 = level_manager.get_current_level()

done = False

# -------- Main Program Loop -----------
while not done:
    current_level = level_manager.get_current_level()
    
    if current_level == None:
        break
    
    current_level.update()
    current_level.draw(screen)
    #Needs Game Logic

    # Update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break

        current_level.handle_keyboard_event(event)


pygame.quit()
