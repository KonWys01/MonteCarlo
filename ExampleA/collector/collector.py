import redis
import time
from datetime import datetime
r = redis.Redis(host='redis', port=6379, decode_responses=True)

while True:
    results = r.lrange("results", 0, -1)
    values = [float(x.split(":")[1]) for x in results]

    if len(results) == 5:
        starts = []
        ends = []
        values = []

        for entry in results:
            parts = entry.split("|")
            hostname = parts[0]
            result = float(parts[1])
            iso_start = parts[2]
            iso_end = parts[3]

            start_time = datetime.fromisoformat(iso_start)
            end_time = datetime.fromisoformat(iso_end)

            starts.append(start_time)
            ends.append(end_time)
            values.append(result)

        # oblicz statystyki
        avg = sum(values) / len(values)
        total_duration = max(ends) - min(starts)

        print(f"AVG: {avg} TIME: {total_duration}")
