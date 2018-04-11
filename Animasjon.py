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
tank_1_params = {
  "LEFT": CENTER_HORIZONTAL - 175,
  "TOP": CENTER_VERTICAL - 125,
  "WIDTH": 150,
  "HEIGHT": 250,
  "FILL_COLOUR": BLUE,
  "OUTLINE_COLOUR": WHITE,
  "BORDER_WIDTH": 3
}

tank_2_params = {
  "LEFT": CENTER_HORIZONTAL + 25,
  "TOP": CENTER_VERTICAL - 125,
  "WIDTH": 150,
  "HEIGHT": 250,
  "FILL_COLOUR": BLUE,
  "OUTLINE_COLOUR": WHITE,
  "BORDER_WIDTH": 3
}

# TESTKJØRING
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
   
   # Fyll in skjermen
   screen.fill(BLACK)
  
   # Tegner opp innholdet i tankene (konstant halvfull)
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
   
   #Timer på toppen
   timer_string = "Runtime: {} seconds".format(round(pygame.time.get_ticks() / 1000, 1))
   timer = timer_font.render(timer_string, True, WHITE)
   timer_rect = timer.get_rect()
   timer_rect.center = (CENTER_HORIZONTAL), (CENTER_VERTICAL - 175)
   screen.blit(timer, timer_rect)
   
   #Skjermoppdatering
   pygame.display.flip()
   clock.tick(FPS)
