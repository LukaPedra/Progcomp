import numpy as np
#Q1A)
def LCG(seed,a,c,m,nsamples):
    u = []
    x = seed
    for i in range(0,nsamples):
        xn = (a * x + c) % m
        u.append(float(xn)/float(m))
        x = xn
    return u
m = 2147483647
nsamples = 10000
a = 39373
c = 0
lcg = LCG(1284,a,c, m, nsamples)
mt = np.random.sample(nsamples)

def checaResultado1(lcg,mt):
    conta = 0
    i = 0
    while(i<nsamples):
        if (mt[i] <= (1/8)) and lcg[i]>=0.5:
            conta = conta + 1
        i = i + 1
    return conta
    
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

def checaResultado2(lcg):
    conta = 0
    for n in lcg:
        oito = False
        if lm(10) <= 1/7:
            oito = True
        if oito == True and n >= 0.5:
            conta = conta + 1
    return conta

def checaResultado3():
    conta = 0
    mt = np.random.sample(nsamples)
    for i in mt:
        LM = lm(100,0.45)
        if (i < 0.5 and LM < 2/8) or (i>=0.5 and LM < 1/7):
            conta = conta + 1
    return conta

print("Q1a)")
print(checaResultado1(lcg,mt))

print("Q1b)")
print(checaResultado2(lcg))

print("Q1c)")
print(checaResultado3())

#Q2)
def moedas():
    U = []
    conta1 = 0
    conta2 = 0
    i = 0
    while(i<nsamples):
        lanc1 = np.random.sample(1)
        lanc2 = np.random.sample(1)
        lanc3 = np.random.sample(1)
        if lanc2 <= 3/7 and lanc3 <= 3/7:
            conta1 = conta1 + 1
        if (lanc1 <= 3/7 and lanc2 > 3/7) or (lanc2 <= 3/7 and lanc1 > 3/7):
            conta2 = conta2 + 1
        i = i + 1
    print("P(A) = "+str(conta1/nsamples))
    print("P(B) = "+str(conta2/nsamples))
print("Q2")
moedas()
'''b)
Não são indpendentes, a probabilidade de um afeta o de outro. por exemplo, se A for verdadeiro, em B a primeira moeda tem que ser coroa.
'''
