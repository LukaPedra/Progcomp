import numpy as np

nsamples = 100000
comprimento = 7
altura = 7
Lx = np.random.uniform(-2, 5, nsamples)
Ly = np.random.uniform(0, altura, nsamples)


points = list(zip(Lx, Ly))


def f(x):
    return -x**2 + x + 6
def g(x):
    return -x**2 + 6*x - 5

def area(points):
    count = 0
    for x, y in points:
        if y <= f(x) or y <= g(x):
            count += 1
    return count / len(points)

print(area(points)*comprimento*altura)
