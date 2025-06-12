import random
import redis
import os
import socket
import numpy as np
from datetime import datetime, timezone

def f(x):
    return np.fabs(np.sin(x) * np.exp(-0.1 * x**2))

def monte_carlo(n=1_000_000):
    total = 0.0
    for _ in range(n):
        x = random.uniform(-5, 5)
        total += f(x)
    area = 10
    return total / n * area

if __name__ == "__main__":
    start = datetime.now()
    iso_start = start.isoformat()
    result = monte_carlo()
    end = datetime.now()
    iso_end = end.isoformat()
    hostname = socket.gethostname()

    redis_host = os.environ.get("REDIS_HOST", "redis")
    r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

    r.rpush("results", f"{hostname}|{result}|{iso_start}|{iso_end}")
