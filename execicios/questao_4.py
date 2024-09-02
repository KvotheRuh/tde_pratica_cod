# ALUNO: CARLOS MORCIANI
# CURSO: CIÊNCIA DA COMPUTAÇÃO

import matplotlib.pyplot as plt
import numpy as np
import math

# Questão 4

def calcular():
  n = float(input("Insira o número que desejar:"))
  x = n
  if x <= 0:
    print("Valor inválido!! ")
  else:
    divisao = pow(x,0.5)
    calculo = (3*pow(x,2)-1)/divisao
    print(calculo)

calcular()