import random
import math
from math import sqrt
import sys
print(sys.argv)

N = 10000 #numero di coppie da generare
M = 0

#meglio fare funzione che restituisce x, y

for i in range(N):
    x = random.random()
    y = random.random()
    #totale.append([x,y])
    if(x**2 + y**2 <=1):
        #cerchio.append([x,y])
        M += 1
        stima_pi = 4 * M / N


print("M ", M)

print("prima stima del pi greco: ", stima_pi)


#ora provo con valor medio

def coordinates() :
        a = random.random()
        return a

def cerchio():
    x = coordinates()
    y = coordinates()
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


k = 10
somma_tot = 0
for i in range (k):
    somma_tot += stima()

valor_medio_new = somma_tot / k
for i in range (k):
    dev_std_new = math.sqrt((valor_medio_new - stima())**2 / (k-1))

print("media: ", valor_medio_new)
print("dev standard: ", dev_std_new)
