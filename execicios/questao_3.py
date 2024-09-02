# ALUNO: CARLOS MORCIANI
# CURSO: CIÊNCIA DA COMPUTAÇÃO

import matplotlib.pyplot as plt
import numpy as np
import math

# Questão 3

def calculando(n):
  if n < 0:
    print("Valor Inválido")
  
  else:
    contador = n + 1
    soma = sum([(pow(-1,i))/(2*i+1) for i in range(contador)])
    calculo = 4*(1-soma)
    print(calculo)
n = 10000
calculando(n)
