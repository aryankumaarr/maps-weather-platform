from fastapi import FastAPI

# CORSMiddleware allows the frontend to make requests to the FastAPI backend
from fastapi.middleware.cors import CORSMiddleware

# Imports the router object containing our route-related api endpoints
from app.api.routes import router

# Imports the database test function so FastAPI can verify postgresql connectivity
from app.db.database import test_database_connection

# Imports Redis cache functions so FastAPI can test reading and writing
from app.services.cache_service import get_cache, set_cache

app = FastAPI(
    title="Maps Weather Platform API",
    version="1.0.0"
)
# Allows the local Next.js frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Connects the route endpoints to FastAPI and adds /api before their paths
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Temporary endpoint used to prove FastAPI can write to and read from redis
@app.get("/cache-test")
def cache_test():
      # Writes a test value to redis
    set_cache("fastapi_test", "hello_from_fastapi")

    # Reads the same value back from redis
    value = get_cache("fastapi_test")

    return {
        "redis_write": "success",
        "redis_read": value,
    }

# Temporary endpoint used to prove FastAPI can connect to postgresql.
@app.get("/database-test")
def database_test():
    result = test_database_connection()

    return {
        "database": "connected",
        "test_result": result,
    }

