import random
import math
from math import sqrt
import sys

N = int(sys.argv[1]) #numero di coppie di coordinate da generare
print("N", N)

if (N < 2):
    print("N dev'essere almeno pari a 2")
    sys.exit(1)

K = int(sys.argv[2]) #numero di stime
print("K", K)

M = 0

#eseguo prima un'unica stima del valore del pi greco
for i in range(N):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if(x**2 + y**2 <=1):
        M += 1
        
stima_pi = 4 * M / N

print("M ", M)
print("prima stima del pi greco: ", stima_pi)


#eseguo K stime del valore del pi greco

def cerchio():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    area = x**2 + y**2
    return area

def stima():
    M2 = 0
    for i in range(N):
        area = cerchio()
        if area <= 1:
            M2 += 1
    stima2_pi = 4 * M2 / N
    return stima2_pi

stima_lista = []

for i in range (K):
    stima_lista.append(stima())

valor_medio = sum(stima_lista) / K

scarto_quad = 0

for s in stima_lista:
    scarto_quad += (valor_medio - s)**2

dev_std = math.sqrt(scarto_quad / (K-1))

print("media: ", valor_medio)
print("deviazione standard: ", dev_std)