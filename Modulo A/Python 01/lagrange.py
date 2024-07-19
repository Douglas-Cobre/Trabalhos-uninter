#LAGRANGE é uma função do SCIPY que pode encontrar a interpolação de um POLINÔMIO usando 3 coordenadas.
from scipy.interpolate import *

x = [0,5,8]
y = [6,2,15]
res = lagrange(x,y)
print(res)

#Polinômios são muito usados em modelos 3d