from scipy.integrate import quad
import numpy as np


# Estarei usando o scipy apenas para realizar as contas de integrais, como seria usar o integrate em R
# A função quad calcula as integrais, recebendo como paramêtro a função, start, stop, paramêtro a ser utilizado na função, nesse caso seria b

def f(x, b):
    return b * x**4 * (1 - x)


def integrate_fx(b):
    integral_result, _ = quad(f, 0, 1, b)
    return integral_result - 1


for b in range(25, 33):
    if np.isclose(integrate_fx(b), 0):
        print(f"Questão 3) letra a: O valor de b é {b}")
        break


def f(x):
    b = 30
    return b * x**4 * (1 - x)


integral_result, _ = quad(f, 0, 0.7)

print(f"Questão 3) letra b: P(X ≤ 0.7) é aproximadamente {integral_result}")


def mediaX(x):
    return x * f(x)


media_x, _ = quad(mediaX, 0, 1)

print(f"Questão 3) letra c: a média X é aproximadamente {media_x}")
