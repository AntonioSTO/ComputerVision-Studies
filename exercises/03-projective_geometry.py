# -*- coding: utf-8 -*-
"""Antonio Sant Ana de Oliveira - exercicio_geometria_projetiva.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SA5qV2w1Rps5_RLLJphAw1SIiR9d9LoF

#Exercícios
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

### Setting printing options
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
np.set_printoptions(precision=3,suppress=True)

"""###1- Dê as coordenadas cartesianas dos pontos:

a) (2, 5, 6)

b) (1, -2, 3)

c) (5, -1, -2, -4)

Siga o exemplo de código abaixo:

"""

p1 = np.array([8,2,4])
print(p1)
p1c = p1/p1[2]
print(p1c)

p1 = np.array([2,5,6])
plc1 = p1/p1[2]

p2 = np.array([1,-2,3])
plc2 = p2/p2[2]

p3 = np.array([5,-1,-2,-4])
plc3 = p3/p3[3]

print(p1)
print(p2)
print(p3)

print(plc1)
print(plc2)
print(plc3)

"""###2- Determine se o ponto "p" pertence ou não à reta "r":

a) r = (3, 5, 2), p = (1, -1, 1)

b) r = (3, 5, 2), p = (1, 0, 1)

c) r = (3, 5, 2), p = (1, 1, 1)

d) r = (2, 1, -6), p = (-2, 0, 1)

e) r = (2, 1, -6), p = (-2, -4, 1)

f) r = (-4, 7, 0), p = (5, -3, 1)

g) r = (-4, 7, 0), p = (14, 28, 3)

h) r = (0, 0, 1), p = (0, 0, 1)

i) r = (0, 0, 1), p = (4, 0, 0)

Siga o exemplo de código abaixo:
"""

#reta
r = np.array([3, 3, 1])
#ponto
p = np.array([1, 1, 2])
#fazer o produto interno e verificar se dá zero
d = np.dot(r,p)
print(d)
if d == 0:
    print("O ponto pertence à reta.")
else:
    print("O ponto não pertence à reta.")

def pertence(r,p):
  d = np.dot(r,p)
  if d == 0:
      print(f"O ponto {p} pertence à reta {r}.")
  else:
      print(f"O ponto {p} não pertence à reta {r}.")

retas = [[3, 5, 2], [2, 1, -6], [-4, 7, 0], [0, 0, 1]]
pontos = [[1, -1, 1],[1, 0, 1],[1, 1, 1],[-2,0,1],[-2, -4, 1],[5, -3, 1],[14, 28, 3],[0, 0, 1],[4, 0, 0]]

for i in range(len(pontos)):
  if i < 3:
    pertence(np.array(retas[0]), np.array(pontos[i]))
  elif i < 5:
    pertence(np.array(retas[1]), np.array(pontos[i]))
  elif i < 7:
    pertence(np.array(retas[2]), np.array(pontos[i]))
  else:
    pertence(np.array(retas[3]), np.array(pontos[i]))

"""###3-Determine a reta que passa pelos pontos:

a) (2, 3, 1) e (5, 6, 4)

b) (-3, 1, -2) e (3, 2, -1)

c) (8, -3, -1) e (-7, 9, 0)

Siga o exemplo de código abaixo:

"""

#pontos
p1 = np.array ([10,-3, 1])
p2 = np.array ([-3, 5, 1])

#calcula a reta

r = np.cross(p1,p2)
print("A reta é ", r)

p1 = np.array ([2,3,1])
p2 = np.array ([5, 6, 4])

r = np.cross(p1,p2)
print("A reta 1 é ", r)

p3 = np.array ([-3,1, -2])
p4 = np.array ([3, 2, -1])

r = np.cross(p3,p4)
print("A reta 2 é ", r)

p5 = np.array ([8,-3, -1])
p6 = np.array ([-7, 9, 0])

r = np.cross(p5,p6)
print("A reta 3 é ", r)

"""###4- Determine o ponto de encontro dos seguintes pares de retas:

a)  (1, 0, 0) e (0, 1, 0)

b)  (3, 5, 1) e (4, 6, 2)

c)  (3, 5, 1) e (0, 0, 1)

d)  (3, 5, 1) e (3, 5, 2)

Siga o exemplo de código abaixo:
"""

# retas
r1 = np.array([4, 7, 3])
r2 = np.array([-3, 1, -5])

# ponto de encontro
p = np.cross(r1,r2)
p = p/p[2]
print("O ponto de encontro é ", p)

def pontoEncontro(r1,r2):
  p = np.cross(r1,r2)

  if p[2] != 0:
    p = p/p[2]
    print("O ponto de encontro é ", p)
  else:
    print("O ponto de encontro é ", p)

r1s = [[1, 0, 0],[3, 5, 1],[3, 5, 1],[3, 5, 1]]
r2s = [[0, 1, 0],[4, 6, 2],[0, 0, 1],[3, 5, 2]]

for i in range(len(r1s)):
  pontoEncontro(np.array(r1s[i]),np.array(r2s[i]))