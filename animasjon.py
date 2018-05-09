'''Animasjon av vanntankene i prosjektet Gode tanker'''
# Importerer nødvendige biblioteker
import sys
import pygame

# Starter opp PyGame
pygame.init()

# Definerer farger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 105, 148)

def screen_size(t1_h, t2_h):
    '''Lager skjermen basert på høyeste tank'''
    t_h = max([t1_h*1000, t2_h*1000])
    new_height = 130 + int(t_h)

    global SIZE
    global CENTER_HORIZONTAL
    global screen
    SIZE = WIDTH, HEIGHT = 640, new_height
    CENTER_HORIZONTAL = WIDTH // 2
    screen = pygame.display.set_mode(SIZE)

# Clock og en font
FPS = 60
clock = pygame.time.Clock()
TIMER_FONT = pygame.font.SysFont('Consolas', 30)

# Tankenes parametre i et dictionary
def tank_1(level, max_height):
    '''Genererer parametre for tank 1'''
    tank_1_params = {
        "LEFT": CENTER_HORIZONTAL - 175,
        "TOP": 75,
        "WIDTH": 150,
        "HEIGHT": max_height*1000,
        "FILL_COLOUR": BLUE,
        "OUTLINE_COLOUR": WHITE,
        "BORDER_WIDTH": 3,
        "LEVEL": level*1000
    }
    return tank_1_params

def tank_2(level, max_height):
    '''Genererer parametre for tank 2'''
    tank_2_params = {
        "LEFT": CENTER_HORIZONTAL + 25,
        "TOP": 75,
        "WIDTH": 150,
        "HEIGHT": max_height*1000,
        "FILL_COLOUR": BLUE,
        "OUTLINE_COLOUR": WHITE,
        "BORDER_WIDTH": 3,
        "LEVEL": level*1000
    }
    return tank_2_params
#Hoveloop som kjøres via tankmodellen
def main_loop(max_h_1, max_h_2, t, level_1, level_2):
    '''Animasjon av tanker. Kjører resten av animeringen via funksjoner'''
    #Lager en sort skjerm
    screen.fill(BLACK)

    #Passer på at PyGame ikke krasjer når du lukker den.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Kjører tegnefunksjonene.
    t_1 = tank_1(level_1, max_h_1)
    t_2 = tank_2(level_2, max_h_2)
    time_update(t)
    tank_update(t_1, t_2)

    #Oppdaterer skjermen.
    pygame.display.flip()
    clock.tick(FPS)

def time_update(t):
    '''Genererer og oppdaterer timer på toppen av skjermen'''
    timer_string = "Tid: {} sekunder".format(round(t, 2))
    timer = TIMER_FONT.render(timer_string, True, WHITE)
    #Henter rektangelet til teksten og plasserer sentrum i definert x og y
    timer_rect = timer.get_rect()
    timer_rect.center = (CENTER_HORIZONTAL), 50
    screen.blit(timer, timer_rect)

def tank_update(tank_1_params, tank_2_params):
    '''Generer tankene basert på parameterdictionaries'''
    # Tegner opp innholdet i tankene
    pygame.draw.rect(screen, BLUE,
                     pygame.Rect(tank_1_params["LEFT"],
                                 tank_1_params["TOP"] + (tank_1_params["HEIGHT"]-tank_1_params["LEVEL"]),
                                 tank_1_params["WIDTH"],
                                 tank_1_params["LEVEL"]))

    pygame.draw.rect(screen, BLUE,
                     pygame.Rect(tank_2_params["LEFT"],
                                 tank_2_params["TOP"] + (tank_2_params["HEIGHT"]-tank_2_params["LEVEL"]),
                                 tank_2_params["WIDTH"],
                                 tank_2_params["LEVEL"]))


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

    #Tegner opp navn under tankene
    tank_1_name = TIMER_FONT.render("Tank 1", True, WHITE)
    #Henter rektangelet til teksten og plasserer sentrum i definert x og y
    tank_1_name_rect = tank_1_name.get_rect()
    tank_1_name_rect.center = (tank_1_params["LEFT"] + (tank_1_params["WIDTH"] // 2)), (tank_1_params["TOP"] + tank_1_params["HEIGHT"]) + 20
    screen.blit(tank_1_name, tank_1_name_rect)   

    tank_2_name = TIMER_FONT.render("Tank 2", True, WHITE)
    tank_2_name_rect = tank_2_name.get_rect()
    tank_2_name_rect.center = (tank_2_params["LEFT"] + (tank_2_params["WIDTH"] // 2)), (tank_2_params["TOP"] + tank_2_params["HEIGHT"]) + 20
    screen.blit(tank_2_name, tank_2_name_rect)   
