import numpy as np


#Passo 1: gere uma variável aleatória uniforme 𝑈 no intervalo (0, 1).
#Passo 2: 𝑋 ← 𝐹−1(𝑈)

#A) inversa de f(x) = 5xˆ4 é F-1(x) = xˆ(1/5) (calculado no papel)
def geraA(n_samples):
    X = np.zeros(n_samples) # n_samples posições com 0
    U = np.random.sample(n_samples) # n_samples valores em [0.0, 1.0)
    for i in range(n_samples):
        X[i] = U[i]**(1/5)
    return X

print(geraA(10))

def inversa2(x):
    return -(-5+(-10*x+10)**(1/2))/5 #caculada fora do programa
#B) inversa de f(x)
def geraB(n_samples):
    X = np.zeros(n_samples) # n_samples posições com 0
    U = np.random.sample(n_samples) # n_samples valores em [0.0, 1.0)
    for i in range(n_samples):
        if U[i] <= 0.6:
            X[i] = (3*U[i]/5)**(1/2) #caculada fora do programa
        else:
            X[i] = inversa2(U[i])
    return X

print(geraB(10))