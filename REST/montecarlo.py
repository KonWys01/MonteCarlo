import random
import math
import sys
import numpy as np

def f(x):
    return np.fabs(np.sin(x) * np.exp(-0.1 * x**2))

def monte_carlo_integration(samples: int):
    total = 0.0
    for _ in range(samples):
        x = random.uniform(-5, 5)
        total += f(x)
    
    area = (5 * 10)
    return area * total / samples
