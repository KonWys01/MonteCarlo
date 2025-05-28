import random
import math
import sys

def f(x, y):
    return math.fabs(math.exp(-x**2 - y**2) * math.cos(2 * x) * math.sin(2 * y))

def monte_carlo_integration(samples: int):
    total = 0.0
    for _ in range(samples):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        total += f(x, y)
    
    area = (5 * 10)  # bo [-5, 5] × [-5, 5] = 10 × 10 = 100
    return area * total / samples
