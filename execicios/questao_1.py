# ALUNO: CARLOS MORCIANI
# CURSO: CIÊNCIA DA COMPUTAÇÃO

import matplotlib.pyplot as plt
import numpy as np
import math

# Questao 1

def funcao(n):
    if n <= 2:
        x = np.linspace(-10, 10, 200)
        x = x[x < 2]
        calculo = 1 / np.sqrt(2 - x)
        plt.plot(x, calculo)
        plt.ylabel("Eixo Y")
        plt.xlabel("Eixo X")
        plt.title("Função f(x)")
        plt.show()
        return calculo

    else:
        print("Valor Inválido!!")

funcao(-10)