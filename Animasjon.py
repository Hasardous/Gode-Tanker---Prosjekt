'''Animasjon av vanntankene i prosjektet Gode tanker'''
# TODO - Konverter mye til funksjoner som kan kjøres sammen med tankmodell.py
# TODO - Dynamisk Skjermstørelse
# Importerer nødvendige biblioteker

import sys
import pygame

# Starter opp PyGame
pygame.init()

# Definerer farger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 105, 148)

# Definerer Vinduet og noen posisjoner
SIZE = WIDTH, HEIGHT = 640, 480
CENTER_HORIZONTAL = WIDTH // 2
CENTER_VERTICAL = HEIGHT // 2
screen = pygame.display.set_mode(SIZE)


# Clock og en font
FPS = 10
clock = pygame.time.Clock()
timer_font = pygame.font.SysFont('Consolas', 30)

# Tankenes parametre i et dictionary
# TODO HAR IKKE NOEN REELLE TALL
def tank_1(level, max_height):
    '''Genererer parametre for tank 1'''
    tank_1_params = {
        "LEFT": CENTER_HORIZONTAL - 175,
        "TOP": CENTER_VERTICAL - 125,
        "WIDTH": 150,
        "HEIGHT": max_height*10,
        "FILL_COLOUR": BLUE,
        "OUTLINE_COLOUR": WHITE,
        "BORDER_WIDTH": 3,
        "LEVEL": level*10
    }
    return tank_1_params

def tank_2(level, max_height):
    '''Genererer parametre for tank 2'''
    tank_2_params = {
        "LEFT": CENTER_HORIZONTAL + 25,
        "TOP": CENTER_VERTICAL - 125,
        "WIDTH": 150,
        "HEIGHT": max_height*10,
        "FILL_COLOUR": BLUE,
        "OUTLINE_COLOUR": WHITE,
        "BORDER_WIDTH": 3,
        "LEVEL": level*10
    }
    return tank_2_params

# TODO - Tenke på om system.sleep() kan være lurt (tankmodell.py) 


def main_loop():
    '''Holder Pygame kjørende'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def time_update(t):
    '''Genererer og oppdaterer timer på toppen av skjermen'''
    timer_string = "Tid: {} sekunder".format(t)
    timer = timer_font.render(timer_string, True, WHITE)
    timer_rect = timer.get_rect()
    timer_rect.center = (CENTER_HORIZONTAL), 75
    screen.blit(timer, timer_rect)
    pygame.display.flip()

def screen_update(tank_1_params, tank_2_params):
    # Tegner opp omrisset til tankene
    pygame.draw.rect(screen, WHITE,
                     pygame.Rect(tank_1_params["LEFT"],
                                 tank_1_params["TOP"],
                                 tank_1_params["WIDTH"],
                                 tank_1_params["HEIGHT"]),
                     tank_1_params["BORDER_WIDTH"])

    pygame.draw.rect(screen, WHITE,
                     pygame.Rect(tank_2_params["LEFT"],
                                 tank_2_params["TOP"],
                                 tank_2_params["WIDTH"],
                                 tank_2_params["HEIGHT"]),
                     tank_2_params["BORDER_WIDTH"])

    # Tegner opp innholdet i tankene
    pygame.draw.rect(screen, BLUE,
                     pygame.Rect(tank_1_params["LEFT"],
                                 tank_1_params["TOP"] + tank_1_params["LEVEL"],
                                 tank_1_params["WIDTH"],
                                 tank_1_params["LEVEL"]))

    pygame.draw.rect(screen, BLUE,
                     pygame.Rect(tank_2_params["LEFT"],
                                 tank_2_params["TOP"] + tank_2_params["LEVEL"],
                                 tank_2_params["WIDTH"],
                                 tank_2_params["LEVEL"]))

    # Oppdaterer skjermen (clock.tick er jeg usikker på)
    pygame.display.flip()
    clock.tick(FPS)
