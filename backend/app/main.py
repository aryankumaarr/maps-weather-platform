from fastapi import FastAPI

# Imports the router object containing our route-related API endpoints.
from app.api.routes import router

app = FastAPI(
    title="Maps Weather Platform API",
    version="1.0.0"
)

# Connects the route endpoints to FastAPI and adds /api before their paths.
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
