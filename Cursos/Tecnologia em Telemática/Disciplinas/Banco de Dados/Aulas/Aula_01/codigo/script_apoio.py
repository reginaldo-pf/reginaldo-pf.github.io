#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Apoio -- Aula 01: Introdução aos Sistemas de Banco de Dados e Modelagem Conceitual
Disciplina: Banco de Dados
IFCE Campus Tauá -- Prof. Reginaldo Pereira Fernandes
"""

import numpy as np
import matplotlib.pyplot as plt

# Configuracao visual acessivel recomendada
plt.style.use('seaborn-v0_8-colorblind')
plt.rcParams.update({
    'figure.figsize': (10, 6),
    'axes.labelsize': 13,
    'axes.titlesize': 15,
    'lines.linewidth': 2.2
})

def despine(ax):
    """Remove bordas superior e direita para visualizacao limpa."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

def main():
    print(f"Executando script de apoio da Aula 01: Introdução aos Sistemas de Banco de Dados e Modelagem Conceitual")
    # Insira aqui os dados e simulacoes da aula

if __name__ == '__main__':
    main()
