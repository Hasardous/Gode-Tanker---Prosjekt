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

# Timer
FPS = 10
timer = pygame.time.Clock()
timer_text = pygame.font.SysFont('Consolas', 30)

# Tankenes parametre i et dictionary
# TODO HAR IKKE NOEN REELLE TALL
tank_1_params = {
  "LEFT": CENTER_HORIZONTAL - 25,
  "TOP": CENTER_VERTICAL - 25,
  "WIDTH": 150,
  "HEIGHT": 250,
  "FILL_COLOUR": BLUE,
  "OUTLINE_COLOUR": WHITE,
  "BORDER_WIDTH": 3
}

tank_2_params = {
  "LEFT": CENTER_HORIZONTAL + 50,
  "TOP": CENTER_VERTICAL + 50,
  "WIDTH": 150,
  "HEIGHT": 250,
  "FILL_COLOUR": BLUE,
  "OUTLINE_COLOUR": WHITE,
  "BORDER_WIDTH": 3
}
