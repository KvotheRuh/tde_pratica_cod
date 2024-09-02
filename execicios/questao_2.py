# ALUNO: CARLOS MORCIANI
# CURSO: CIÊNCIA DA COMPUTAÇÃO

import matplotlib.pyplot as plt
import numpy as np
import math

# Questão 2

cabo = plt.Rectangle(xy=(-2.5,0), width=5,height=-20, color="black")
fig, ax = plt.subplots()

raio = 10
bordas = 64
t = np.linspace(0, 2*np.pi, bordas+1)
x = raio*np.cos(t)
y = raio*np.sin(t)
ax.plot([-10, 10], [-20, -20], color='black', alpha=0)
plt.plot(x,y, color="black")
plt.axis("equal") 
plt.title("Raquete")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
ax.fill(x,y, color="red")
ax.add_patch(cabo)

plt.show()