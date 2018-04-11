'''Simulering av tankene i prosjektet Gode Tanker'''

# Importering av nødvendige biblioteker

import matplotlib.pyplot as plt
import math

# Variabler

r_1 = 0.135
r_2 = 0.135
A_T1 = math.pi() * r_1^2
A_T2 = math.pi() * r_2^2
max_h1 = 0.25
max_h2 = 0.25
A_hull1 = 0 #todo
A_hull2 = 0 #todo
g = 9.81
q_inn_1 = 0 #todo
C = 0.61
k = C * math.sqrt(2*g)
d_t = 60
min_h = 0.01
max_t = 4800

# Initialverdier

h_1 = 0.20
h_2 = 0.20
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

while h_1 > min_h and t < max_t:
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

# Plotting

plt.plot(t_hist, h1_hist)
plt.plot(t_hist, h2_hist)
plt.ylabel('Høyde [m]')
plt.xlabel('Tid [s]')
plt.axis([0, max_t, min(h1_hist)*0.9, max(h1_hist)*1.1])
plt.grid()
plt.show()
