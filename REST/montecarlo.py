import random
import math
import sys
import numpy as np

def f(x):
    return np.fabs(np.sin(x) * np.exp(-0.1 * x**2))

def monte_carlo(n: int = 1_000_000):
    total = 0.0
    for _ in range(n):
        x = random.uniform(-5, 5)
        total += f(x)
    area = 10
    return total / n * area
