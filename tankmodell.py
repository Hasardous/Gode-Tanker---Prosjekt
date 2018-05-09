'''Simulering av tankene i prosjektet Gode Tanker'''

# Importering av nødvendige biblioteker

import matplotlib.pyplot as plt
import math
import animasjon

# Variabler

r_1 = 0.11825
r_2 = 0.11825
A_T1 = 0.0439
A_T2 = 0.0439
max_h1 = 0.265 
max_h2 = 0.265
A_hull1 = math.pi * 0.005 **2
A_hull2 = math.pi * 0.005 **2
g = 9.81
q_inn_1 = 0.00005 #bruker 20 sek på en liter
C = 0.60 #TODO Default 0.61 
k = C * math.sqrt(2*g)
d_t = 1 #[default=0.01 eller 0.1]
min_h = 0.001
max_t = 1000 #480

# Dynamisk Skjermstørelse

animasjon.screen_size(max_h1, max_h2)

# Initialverdier

h_1 = 0.15 #TODO
h_2 = 0.10 #TODO
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
  
# Animasjon
  
animasjon.main_loop(max_h1, max_h2, t, h_1, h_2)
t += d_t

# Plotting

plt.plot(t_hist, h1_hist, label='Tank 1')
plt.plot(t_hist, h2_hist, label='Tank 2')
plt.ylabel('Høyde [m]')
plt.xlabel('Tid [s]')
plt.axis([0, max_t, 0, 0.30])
plt.legend()
plt.grid()
plt.show()
