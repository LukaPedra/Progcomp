import numpy as np
from scipy.integrate import quad

# Função para calcular a integral de f(x)
def f(x, b):
    return b * x**4 * (1 - x)

# Encontrar o valor de b que faz a integral de f(x) igual a 1
b_values = range(25, 33)  # Valores possíveis de b
bFinal = 0
for b in b_values:
    integral, _ = quad(f, 0, 1, args=(b,))
    aux = integral - 1
    if np.isclose(aux, 0):
        bFinal = b
        break
print("C) Valor de b: ", bFinal)
###########################################################################
#B)
# Simulação para calcular P(X <= 0.7)
n_samples = 100000
x_samples = np.random.uniform(0, 1, n_samples)
conta = 0

for i in range(n_samples):
    if f(x_samples[i], bFinal) <= 0.7:
        conta = conta + 1
#prob = np.mean([f(x,bFinal) for x in x_samples if x <= 0.7])
print("B) Probabilidade: ", conta/n_samples)


# Simulação para calcular a média de X
mediax = np.mean([x * f(x,bFinal) for x in x_samples])
print("C) Média de X: ", mediax)