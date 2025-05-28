from fastapi import FastAPI, Request
from montecarlo import monte_carlo_integration
import httpx
import asyncio
import time

app = FastAPI()

WORKER_URL = "http://worker:8000/worker_task"
REPEAT_COUNT = 3

@app.post("/local")
async def calculate_local(request: Request):
    data = await request.json()
    samples = int(data.get("samples", 10_000_000))

    start = time.perf_counter()
    results = [monte_carlo_integration(samples) for _ in range(REPEAT_COUNT)]
    end = time.perf_counter()

    avg_result = sum(results) / REPEAT_COUNT

    return {
        "result": avg_result,
        "time_seconds": end - start
    }

@app.post("/swarm")
async def calculate_swarm(request: Request):
    data = await request.json()
    samples = int(data.get("samples", 10_000_000))

    start = time.perf_counter()

    async with httpx.AsyncClient() as client:
        tasks = [
            client.post(WORKER_URL, json={"samples": samples})
            for _ in range(REPEAT_COUNT)
        ]
        responses = await asyncio.gather(*tasks)

    results = [res.json()["result"] for res in responses]
    avg_result = sum(results) / REPEAT_COUNT
    end = time.perf_counter()

    return {
        "result": avg_result,
        "time_seconds": end - start
    }