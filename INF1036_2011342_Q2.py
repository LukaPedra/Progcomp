import numpy as np


#Cara >= 0.5
#Coroa < 0.5
m = 2147483647
nsamples = 10000
a = 39373
c = 0
def LCG(seed,a,c,m,nsamples):
    u = []
    x = seed
    for i in range(0,nsamples):
        xn = (a * x + c) % m
        u.append(float(xn)/float(m))
        x = xn
    return u

def lm(n,p=0.5):
    moedasLM = np.random.sample(n)
    resp = 0
    i = 0
    for m in moedasLM:
        if m > p:
            resp = resp + 1*2**i 
        else:
            resp = resp + 0*2**i 
        i = i + 1
    pos = (2**n - 1)
    return resp/pos
ListaLCG = LCG(1284,a,c, m, nsamples)
ListaMT = np.random.sample(nsamples)
def checaResultadoA(lcg,mt):
    conta = 0
    i = 0
    while(i<nsamples):
        if ((mt[i]> 3/8) and (mt[i] <= (4/8))) and lcg[i]>=0.5:
            conta = conta + 1
        i = i + 1
    return conta

def checaResultadoB(lcg, mt):
    conta = 0
    i = 0 
    for n in lcg:
        if mt[i] > 6/7 and n >= 0.5:
            conta = conta + 1
        i = i + 1
    return conta
def checaResultadoC(mt):
    conta = 0
    prob = 0.45
    for i in mt:
        LM = lm(100)
        if (i >= prob and ((LM <= 3/8) and LM > 1/8)):
            #Caso face 2 e 3
            conta = conta + 1
        if (i < prob and ((LM <= 5/8) and LM > 4/8)):
            conta = conta + 1
    return conta
print(checaResultadoA(ListaLCG,ListaMT))
print(checaResultadoB(ListaLCG,ListaMT))
print(checaResultadoC(ListaMT))