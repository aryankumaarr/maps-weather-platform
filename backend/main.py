# Placeholder entrypoint so the Docker/Compose stack has something to run.
# Backend owner: replace with the real FastAPI app.
from fastapi import FastAPI

app = FastAPI(title="maps-weather-platform API")


@app.get("/health")
def health():
    return {"status": "ok"}
