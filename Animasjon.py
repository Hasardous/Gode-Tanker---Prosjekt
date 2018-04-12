'''Animasjon av vanntankene i prosjektet Gode tanker'''
# TODO - Konverter mye til funksjoner som kan kjøres sammen med tankmodell.py
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
screen = pygame.display.set_mode(SIZE)
CENTER_HORIZONTAL = WIDTH // 2
CENTER_VERTICAL = HEIGHT // 2

# Clock og en font
FPS = 10
clock = pygame.time.Clock()
timer_font = pygame.font.SysFont('Consolas', 30)

# Tankenes parametre i et dictionary
# TODO HAR IKKE NOEN REELLE TALL
# Må kunne endre på helst én param for å forandre høyden
# Level? Krever også endring lenger ned i draw.rect()
# Disse må genereres i en funksjon som kan kjøres fra tankmodell.py
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
# TESTKJØRING
# Må Konverteres til en funksjon
# Tar imot tank_params dictionaries
# Oppdaterer skjermen for hvert nye tall den mottar (aka hver gang den kjøres)
# Splittes i to?
# En som kjører hele tiden i tankmodell.py
# Og en som oppdateres med nye tall
# system.sleep() kan være lurt (tankmodell.py) 
pygame.display.flip()
clock.tick(FPS)

def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fyll in skjermen
        screen.fill(BLACK)

def time_update():
    #Timer på toppen
    #Timer_string må forandres
    #Trenger t fra tankmodell.py
    #TODO Konverter til funksjon time_update(t eller d_t)
    timer_string = "Runtime: {} seconds".format(round(pygame.time.get_ticks() / 1000, 1))
    timer = timer_font.render(timer_string, True, WHITE)
    timer_rect = timer.get_rect()
    #TODO REMEMBER Center_Vertical changes
    timer_rect.center = (CENTER_HORIZONTAL), (CENTER_VERTICAL - 175)
    screen.blit(timer, timer_rect)

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
                                 tank_1_params["TOP"] + tank_1_params["HEIGHT"]/2,
                                 tank_1_params["WIDTH"],
                                 tank_1_params["HEIGHT"]/2))

    pygame.draw.rect(screen, BLUE,
                     pygame.Rect(tank_2_params["LEFT"],
                                 tank_2_params["TOP"] + tank_2_params["HEIGHT"]/2,
                                 tank_2_params["WIDTH"],
                                 tank_2_params["HEIGHT"]/2))
