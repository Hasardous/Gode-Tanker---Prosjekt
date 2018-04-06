'''Tankmodell av Gode Tanker'''

# Importering av nødvendige biblioteker

import matplotlib.pyplot as plt
import math

# Variabler

# Starttiden

r1 = 0.135
r2 = 0.135
A_t1 = math.pi() * r1^2
A_t2 = math.pi() * r2^2
max_h1 = 0.25
max_h2 = 0.25
A_hull1 = 0 #todo
A_hull2 = 0 #todo
g = 9.81  
q_inn1 = 0 #todo
C = 0.61
k = C * math.sqrt(2*g)
dt = 60
min_h = 0.01
maks_t = 4800

# Initialverdier 

h_1 = 0.20
h_2 = 0.20
q_inn2 = 0
t = 0
# Modell

def euler(h, dh, dt):
  return h + dh * dt

def stigning(A_h, A_t, h, q_inn):
  return 1/A_t * (q_inn - A_h * k * math.sqrt(h))

def hastighet(h):
  if h > 0.0:
    return k * math.sqrt(h)
  else:
    return 0.0

# Program

t_hist = [] 
h1_hist = [] 
h2_hist = [] 

while h_1 > min_h and t < maks_t:
  if t > 0: 
    h_1 = euler(h_1, stigning(A_hull1, A_t1, h_1, q_inn1), dt)
    v_1 = hastighet(h_1) 
    q_inn2 = A_hull1 * v_1 
    h_2 = euler(h_2, stigning(A_hull2, A_t2, h_2, q_inn2), dt)
    v_2 = hastighet(h_2)
  
  # print("t = {} => h_1 = {} \t q_inn1 = {} \t h_2 = {} \t q_inn2 = {}".format(t, round(h_1,2), q_inn1, round(h_2,2), round(q_inn2,4)))
  t_hist.append(t)
  h1_hist.append(h_1)
  h2_hist.append(h_2)
  t += dt

# Plotting

plt.plot(t_hist, h1_hist)
plt.plot(t_hist, h2_hist)
plt.ylabel('Høyde [m]')
plt.xlabel('Tid [s]')
plt.axis([0, t_lim, min(h1_hist)*0.9, max(h1_hist)*1.1])
plt.grid()
plt.show()
    
    
