# -*- coding: utf-8 -*-
"""JogoDaVelha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ocIKTwKmNNodRlzFQ9xMCZCnUieuZzSP
"""

import os 
import random

jogarDenovo = True
quantidadeDeJogadas = 0
quantidadeMaximaDeJogadas = 9 
jogadorVez = 2
vit = False
matriz = [
          [" "," "," "],
          [" "," "," "],
          [" "," "," "]
]


def tela():
  global matriz
  global quantidadeDeJogadas
  os.system("cls")
  print("    0   1   2")
  print("0:  "+matriz[0][0] +" | "+ matriz[0][1]+ " | "+ matriz[0][2])
  print("   -----------")
  print("1:  "+matriz[1][0] +" | "+ matriz[1][1]+ " | "+ matriz[1][2])
  print("   -----------")
  print("2:  "+matriz[2][0] +" | "+ matriz[2][1]+ " | "+ matriz[2][2])
  
  print("Jogadas: "+str(quantidadeDeJogadas))


while(True):