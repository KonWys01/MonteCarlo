FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN pip install fastapi uvicorn httpx numpy

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]