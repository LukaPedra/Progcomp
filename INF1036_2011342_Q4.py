
import numpy as np

def p(x):
    return (30 * x * (1-x)**4)

def h(x):
    return (1/(1-0))

def inversa_h(x):
    return (0 + (1-0)*x)

def AmostraX(n_samples):
    x = np.zeros(n_samples)
    c = 2.458
    for i in range(n_samples):
        while (True):
            u1 = np.random.sample(1)
            y = inversa_h(u1) 
            u2 = np.random.sample(1)
            if (u2 <= p(y)/(c*h(y))):
                x[i] = y  
                break
    return x

n_samples = 10000
X = AmostraX(n_samples)
print(X)
print(np.mean(X))
print(np.var(X))



