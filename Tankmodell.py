'''Tankmodell av Gode Tanker'''

# Importering av nødvendige biblioteker

import matplotlib.pyplot as plt
import math

# Variabler

# Initialverdier 

# Modell

def euler(h, dh, dt):
  return h + dh * dt

def stigning(A_h, A_t, h, q_inn):
  return 1/A_t * (q_inn - A_h * k * math.sqrt(h))

