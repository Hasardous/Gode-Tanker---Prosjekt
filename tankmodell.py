'''Simulering av tankene i prosjektet Gode Tanker'''

# Importering av nødvendige biblioteker

import matplotlib.pyplot as plt
import math
import animasjon

# Starting og kjøring av pygame
animasjon.main_loop()

# Variabler

r_1 = 13.5 # todo
r_2 = 13.5 # todo
A_T1 = math.pi * r_1 ** 2
A_T2 = math.pi * r_2 ** 2
max_h1 = 25 # todo
max_h2 = 25 # todo
A_hull1 = 25 #todo
A_hull2 = 21 #todo
g = 9.81
q_inn_1 = 192 #todo
C = 0.61
k = C * math.sqrt(2*g)
d_t = 0.01
min_h = 0.001
max_t = 480

# Initialverdier

h_1 = 20 # todo
h_2 = 20 # todo
q_inn_2 = 0.0
t = 0

# Modell

def euler(h, d_h, delta_t):
  '''Kjører Eulers metode'''
  return h + d_h * delta_t

def stigning(A_h, A_t, h, q_inn):
  '''Regner ut stigningstallet fra modellen'''
  return 1/A_t * (q_inn - A_h * k * math.sqrt(h))

def hastighet(h):
  '''Regner ut hastigheten til q_ut'''
  if h > 0.0:
    return k * math.sqrt(h)
  else:
    return 0.0

# Program

t_hist = []
h1_hist = []
h2_hist = []

while h_1 > min_h and h_2 > min_h and t < max_t and h_1 < max_h1 and h_2 < max_h2:
  if t > 0:
    h_1 = euler(h_1, stigning(A_hull1, A_T1, h_1, q_inn_1), d_t)
    v_1 = hastighet(h_1)
    q_inn_2 = A_hull1 * v_1
    h_2 = euler(h_2, stigning(A_hull2, A_T2, h_2, q_inn_2), d_t)
    v_2 = hastighet(h_2)

  # print("t = {} => h_1 = {} \t q_inn_1 = {} \t h_2 = {} \t q_inn_2 = {}".format(t, round(h_1,2), q_inn_1, round(h_2,2), round(q_inn_2,4)))
  t_hist.append(t)
  h1_hist.append(h_1)
  h2_hist.append(h_2)
  t += d_t
  
  # Animasjon (Bruker animasjon.py, husk denne i tillegg)
  # Ikke designet enda (Framework)
  TANK_1 = animasjon.tank_1(h_1, max_h1) # Genererer tankenes parametere fra høyden
  TANK_2 = animasjon.tank_2(h_2, max_h2) # Kanskje integrere tankhøyden? (max_h)
  animasjon.time_update(t, d_t) # En av delene
  animasjon.screen_update(tank_1, tank_2) # Oppdaterer tankinnholdet (Ikke Hovedloop)

# Plotting

plt.plot(t_hist, h1_hist)
plt.plot(t_hist, h2_hist)
plt.ylabel('Høyde [m]')
plt.xlabel('Tid [s]')
plt.axis([0, max_t, 0, max(h1_hist)*1.1])
plt.grid()
plt.show()
