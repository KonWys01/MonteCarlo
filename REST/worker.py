from fastapi import FastAPI, Request
from montecarlo import monte_carlo

app = FastAPI()

@app.post("/worker_task")
async def worker_task(request: Request):
    data = await request.json()
    samples = int(data.get("samples", 1_000_000))
    result = monte_carlo(samples)
    return {"result": result}