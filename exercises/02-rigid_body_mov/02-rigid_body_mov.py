# -*- coding: utf-8 -*-
"""Atividade_movimento_corpo_rigido - Antônio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17aIf1GNL5iO8ZVpns561JiS4jhvKDjXe

Considere uma câmera representada pelos eixos coordenados abaixo.
Note que o eixo Z, o qual representa o eixo óptico da câmera está apontado para cima.
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# %matplotlib inline
import numpy as np
from math import sin, cos, pi

def set_plot(ax=None,figure = None,lim=[-2,2]):
    if figure ==None:
        figure = plt.figure(figsize=(8,8))
    if ax==None:
        ax = plt.axes(projection='3d')

    ax.set_title("camera referecnce")
    ax.set_xlim(lim)
    ax.set_xlabel("x axis")
    ax.set_ylim(lim)
    ax.set_ylabel("y axis")
    ax.set_zlim(lim)
    ax.set_zlabel("z axis")
    return ax

#adding quivers to the plot
def draw_arrows(point,base,axis,length=1.5):
    # The object base is a matrix, where each column represents the vector
    # of one of the axis, written in homogeneous coordinates (ax,ay,az,0)


    # Plot vector of x-axis
    axis.quiver(point[0],point[1],point[2],base[0,0],base[1,0],base[2,0],color='red',pivot='tail',  length=length)
    # Plot vector of y-axis
    axis.quiver(point[0],point[1],point[2],base[0,1],base[1,1],base[2,1],color='green',pivot='tail',  length=length)
    # Plot vector of z-axis
    axis.quiver(point[0],point[1],point[2],base[0,2],base[1,2],base[2,2],color='blue',pivot='tail',  length=length)

    return axis


### Setting printing options
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
np.set_printoptions(precision=3,suppress=True)

"""Crie suas funções de translação e rotação nos três eixos."""

def move(dx,dy,dz):
    T = np.eye(4)
    T[0,-1]=dx
    T[1,-1]=dy
    T[2,-1]=dz
    return T

def z_rotation(angle):
    rotation_matrix=np.array([[cos(angle),-sin(angle),0,0],[sin(angle),cos(angle),0,0],[0,0,1,0],[0,0,0,1]])
    return rotation_matrix

def x_rotation(angle):
    rotation_matrix=np.array([[1,0,0,0],[0, cos(angle),-sin(angle),0],[0, sin(angle), cos(angle),0],[0,0,0,1]])
    return rotation_matrix

def y_rotation(angle):
    rotation_matrix=np.array([[cos(angle),0, sin(angle),0],[0,1,0,0],[-sin(angle), 0, cos(angle),0],[0,0,0,1]])
    return rotation_matrix

# base vector values
e1 = np.array([[1],[0],[0],[0]]) # X
e2 = np.array([[0],[1],[0],[0]]) # Y
e3 = np.array([[0],[0],[1],[0]]) # Z
base = np.hstack((e1,e2,e3))

print ('Cartesian base: \n',base)
#origin point
point =np.array([[0],[0],[0],[1]])

cam = np.hstack((base,point))

print ('Origin: \n',point)

print ('cam: \n',cam)

ax0 = set_plot()
draw_arrows(point,base,ax0)

"""Execute as transformações necessárias para posicionar o eixo óptico da câmera na horizontal (eixo Z), tendo o eixo Y apontando para baixo e o eixo X para a direita (sem alteração da orientação atual). Além disso, posicione essa câmera no ponto (2,7,3).

Faça o seu código abaixo.
"""

# Faça as transformações

# Imprima o valor da camera original e camera transformada

R_cam = x_rotation(-pi/2)
T_cam = move(2,7,3)

cam2 = T_cam@R_cam@cam

print("Cam: ", cam)

print("Cam2: ", cam2)

"""Vamos agora plotar o seu resultado."""

ax0 = set_plot(lim=[-2,10])
draw_arrows(point,base,ax0)
draw_arrows(cam[:,-1],cam[:,0:3],ax0)

ax1 = set_plot(lim=[-2,10])
draw_arrows(point,base,ax1)
draw_arrows(cam2[:,-1],cam2[:,0:3],ax1)

"""Agora vamos incluir um objeto na cena. Vamos usar a casa que já apresentamos no material das aulas de python."""

#Creating a house

house = np.array([[0,         0,         0],
         [0,  -10.0000,         0],
         [0, -10.0000,   12.0000],
         [0,  -10.4000,   11.5000],
         [0,   -5.0000,   16.0000],
         [0,         0,   12.0000],
         [0,    0.5000,   11.4000],
         [0,         0,   12.0000],
         [0,         0,         0],
  [-12.0000,         0,         0],
  [-12.0000,   -5.0000,         0],
  [-12.0000,  -10.0000,         0],
         [0,  -10.0000,         0],
         [0,  -10.0000,   12.0000],
[-12.0000,  -10.0000,   12.0000],
  [-12.0000,         0,   12.0000],
         [0,         0,   12.0000],
         [0,  -10.0000,   12.0000],
         [0,  -10.5000,   11.4000],
  [-12.0000,  -10.5000,   11.4000],
  [-12.0000,  -10.0000,   12.0000],
  [-12.0000,   -5.0000,   16.0000],
         [0,   -5.0000,   16.0000],
         [0,    0.5000,   11.4000],
  [-12.0000,    0.5000,   11.4000],
  [-12.0000,         0,   12.0000],
  [-12.0000,   -5.0000,   16.0000],
  [-12.0000,  -10.0000,   12.0000],
  [-12.0000,  -10.0000,         0],
  [-12.0000,   -5.0000,         0],
  [-12.0000,         0,         0],
  [-12.0000,         0,   12.0000],
  [-12.0000,         0,         0]])

house = np.transpose(house)

#add a vector of ones to the house matrix to represent the house in homogeneous coordinates
house = np.vstack([house, np.ones(np.size(house,1))])

ax0 = set_plot(lim=[-15,20])
draw_arrows(point,base,ax0)
ax0.plot3D(house[0,:], house[1,:], house[2,:], 'red')
# Plotando a quina da casa que está em (0,0,0) para servir de referência
ax0.scatter(house[0,0], house[1,0], house[2,0],'b')


# Plote a câmera também - altere o código abaixo, se necessário
draw_arrows(cam2[:,-1],cam2[:,0:3],ax0)

"""Agora você deverá rotacionar a casa de -30 graus em torno do eixo Z e posicioná-la de tal forma que sua quina (0,0,0) ficará em (3, 20, 2).

Faça o seu código aqui.
"""

R_house = z_rotation(-pi/6)
T_house = move(3,20,2)

house = T_house@R_house@house

"""Agora vamos plotar a câmera e a casa no mesmo gráfico."""

ax0 = set_plot(lim=[-15,20])
draw_arrows(point,base,ax0)
ax0.plot3D(house[0,:], house[1,:], house[2,:], 'red')
# Plotando a quina da casa para servir de referência
ax0.scatter(house[0,0], house[1,0], house[2,0],'b')

# Plote a câmera também - altere o código abaixo, se necessário
draw_arrows(cam2[:,3],cam2[:,0:3],ax0)

"""Calcule qual o valor das coordenadas da quina da casa no referencial da câmera. Lembre-se que a quina da casa está posicionada em (3, 20, 2) e que a câmera está posicionada em (2, 7, 3), ambas no referencial do mundo. Mas o referencial da câmera possui orientações diferentes do referencial do mundo. Faça o seu código logo abaixo e imprima a sua resposta usando "print"."""

# Transformação acumulada para colocar o referencial da câmera onde se encontra atualmente:
# inclui a rotação acumulada e a translação da origem
# Essa transformação faz a conversão de coordenadas no referencial da câmera para o referencial do mundo

def change_world2cam (M,point_world):
      #Convert from world frame to camera frame
      M_inv = np.linalg.inv(M)
      p_cam = np.dot(M_inv,point_world)
      return p_cam

M = np.dot(T_cam,R_cam)

print(change_world2cam(M, np.array([3,20,2,1])))

"""Imagine agora que você deverá rotacionar a sua câmera em torno do seu eixo Y (que está na vertical) de 45 graus e depois incliná-la de -15 graus em torno do eixo X (que está na horizontal), mas sem tirá-la da posição onde ela se encontra.
Faça seu código abaixo.
"""

# Dica: Faça uma rotação de cada vez e plote o resultado em cada caso para você ter certeza de que está correto

origem = np.linalg.inv(M)@M

Ry = y_rotation(pi/4)
Rx = x_rotation(-pi/12)

teste_cam2 = M@Rx@Ry@origem

print(teste_cam2)

"""Vamos agora plotar o seu resultado."""

ax0 = set_plot(lim=[-15,20])
draw_arrows(point,base,ax0)
ax0.plot3D(house[0,:], house[1,:], house[2,:], 'red')
# Plotando a quina da casa que está em (0,0,0) para servir de referência
ax0.scatter(house[0,0], house[1,0], house[2,0],'b')

# Plote a câmera também - altere o código abaixo, se necessário
draw_arrows(teste_cam2[:,-1],teste_cam2[:,0:3],ax0)

"""Calcule novamente qual o valor das coordenadas da quina da casa no referencial da câmera. Lembre-se que a quina da casa está posicionada em (3, 20, 2) e que a câmera está posicionada em (2, 7, 3), ambas no referencial do mundo. Mas o referencial da câmera possui orientações diferentes do referencial do mundo. Faça o seu código logo abaixo e imprima a sua resposta usando "print"."""

# Transformação acumulada para colocar o referencial da câmera onde se encontra atualmente:
# inclui a rotação acumulada e a translação da origem
# Essa transformação faz a conversão de coordenadas no referencial da câmera para o referencial do mundo

def change_world2cam (M,point_world):
      #Convert from world frame to camera frame
      M_inv = np.linalg.inv(M)
      p_cam = np.dot(M_inv,point_world)
      return p_cam

new_M = M@Rx@Ry

print(change_world2cam(new_M, np.array([3,20,2,1])))

"""Vamos agora transladar a câmera de 5 unidades na direção de seu eixo Z. Faça o seu código abaixo."""

# Lembre-se que é preciso levar a câmera para a origem antes de realizar a
# transformação que ocorrerá no próprio eixo da câmera

origem = np.linalg.inv(new_M)@new_M

Tz = move(0,0,5)

teste_cam3 = new_M@Tz@origem

print(teste_cam3)

"""Vamos plotar mais uma vez a casa e a câmera em sua nova postura (posição e orientação). Para comparação, plote também a postura anterior da câmera."""

ax0 = set_plot(lim=[-15,20])
draw_arrows(point,base,ax0)
ax0.plot3D(house[0,:], house[1,:], house[2,:], 'red')
# Plotando a quina da casa para servir de referência
ax0.scatter(house[0,0], house[1,0], house[2,0],'b')

# Plote a câmera também - altere o código abaixo, se necessário
draw_arrows(teste_cam3[:,-1],teste_cam3[:,0:3],ax0)

"""Por fim, vamos transladar a câmera no referencial do mundo de -10 unidades no eixo Z. Faça seu código abaixo."""

T_mundo = move(0,0,-10)

teste_cam4 = T_mundo@teste_cam3

print(teste_cam4)

"""E plotar mais uma vez o seu resultado, mostrando a casa, o referencial original e a câmera em sua nova postura (posição e orientação). Para comparação, plote também a postura anterior da câmera."""

ax0 = set_plot(lim=[-15,20])
draw_arrows(point,base,ax0)
ax0.plot3D(house[0,:], house[1,:], house[2,:], 'red')
# Plotando a quina da casa para servir de referência
ax0.scatter(house[0,0], house[1,0], house[2,0],'b')

# Plote a câmera também - altere o código abaixo, se necessário
draw_arrows(teste_cam4[:,-1],teste_cam4[:,0:3],ax0)