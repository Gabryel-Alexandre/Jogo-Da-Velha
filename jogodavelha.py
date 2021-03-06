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
vit = "n"
matriz = [
          [" "," "," "],
          [" "," "," "],
          [" "," "," "]
]


def tela():
  global matriz
  global quantidadeDeJogadas
  os.system('cls')
  print("    0   1   2")
  print("0:  "+matriz[0][0] +" | "+ matriz[0][1]+ " | "+ matriz[0][2])
  print("   -----------")
  print("1:  "+matriz[1][0] +" | "+ matriz[1][1]+ " | "+ matriz[1][2])
  print("   -----------")
  print("2:  "+matriz[2][0] +" | "+ matriz[2][1]+ " | "+ matriz[2][2])
  
  print("Jogadas: "+str(quantidadeDeJogadas))


def jogadorHumano():
  global quantidadeDeJogadas
  global jogadorVez
  global quantidadeMaximaDeJogadas
  global matriz

  if jogadorVez == 2 and quantidadeDeJogadas < quantidadeMaximaDeJogadas:
    

    try:
      linha = int (input("Digite a Linha : "))
      coluna = int (input("Digite a coluna : "))
      while matriz[linha][coluna] !=" ":
        linha = int (input("Digite a Linha : "))
        coluna = int (input("Digite a coluna : "))
      matriz [linha][coluna] = "X"
      jogadorVez = 1
      quantidadeDeJogadas+= 1
    except:
      print("Linha ou coluna inválida")
      os.system("pause")


def jogadorCPU():
  global quantidadeDeJogadas
  global jogadorVez
  global quantidadeMaximaDeJogadas
  global matriz
  global vit
  
  if jogadorVez == 1 and quantidadeDeJogadas < quantidadeMaximaDeJogadas and vit =="n":
    
    linha =  random.randrange(0,3)
    coluna = random.randrange(0,3)
    while matriz[linha][coluna] !=" ":
      linha = random.randrange(0,3)
      coluna = random.randrange(0,3)
    matriz[linha][coluna]="O"
    quantidadeDeJogadas+=1
    jogadorVez = 2

def verificador():
  global matriz
  global vit
  vitoria = "n"
  simbolos = ["X","O"]

  for s in simbolos:
    vitoria = "n"
    ic=il = 0
    #Verificar Linhas
    while il <3:
      soma = 0
      ic = 0 
      while ic < 3:
        if(matriz[il][ic]==s):
          soma+=1
        ic+=1
      
      if(soma==3):
        vitoria = s
        break
      il+=1
    if(vitoria!="n"):
      break
    #Verificar Colunas
    ic=il = 0
    while ic <3:
      soma = 0
      il = 0 
      while il < 3:
        if(matriz[il][ic]==s):
          soma+=1
        il+=1
      
      ic+=1
      if(soma==3):
        vitoria = s
        break
    if(vitoria!="n"):
      break

    #Verificar Diagonal 1
    soma = 0 
    idiag = 0
    while(idiag < 3 ):
      if(matriz[idiag][idiag]==s):
        soma+=1

      idiag+=1
    if(soma==3):
      vitoria = s
      break
     #Verificar Diagonal 2
    soma = 0 
    idiagl = 0
    idiagc = 2
    while(idiagc >= 0 ):
      if(matriz[idiagl][idiagc]==s):
        soma+=1

      idiagl+=1
      idiagc-=1
    if(soma==3):
      vitoria = s
      break
  vit = vitoria
  return vitoria

def redefinir():
  global matriz 
  global quantidadeDeJogadas
  global quantidadeMaximaDeJogadas
  global jogadorVez
  global vit 
  quantidadeDeJogadas = 0
  quantidadeMaximaDeJogadas = 9 
  jogadorVez = 2
  vit = "n"
  matriz = [
          [" "," "," "],
          [" "," "," "],
          [" "," "," "]
  ]

while(True):
  tela()
  jogadorHumano()
  vit = verificador()
  jogadorCPU()
  vit = verificador()
  if vit!="n":
    tela()
    if(vit =="X"):
      print("O jogador humano venceu e ouve {} jogadas ".format(quantidadeDeJogadas))
    else:
      print("A maquina venceu e ouve {} jogadas ".format(quantidadeDeJogadas))
    rep = input("Deseja jogar novamente ? (Sim,Não)")
    print(rep)
    if rep.lower =="sim" or rep.lower == "s":
      redefinir()
    else:
      print("Obigado por jogar :D")
      break
  if quantidadeDeJogadas == quantidadeMaximaDeJogadas and vit =="n":
    tela()
    print("Não ouve vencedores")
    rep = str(input("Deseja jogar novamente ? (Sim,Não)"))
    if rep.lower =="sim" or rep.lower == "s":
      redefinir()
    else:
      print("Obigado por jogar :D")
      break  