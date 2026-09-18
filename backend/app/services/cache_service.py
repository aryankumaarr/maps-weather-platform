# os lets the Python read enviroment variables such as redis url
import os

# Redis is the Python client used to communicate with the Redis server
from redis import Redis

# Gets the Redis connection address from the environment
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
# Creates a Redis client that the backend can use to read and write cached data.
redis_client = Redis.from_url(REDIS_URL, decode_responses=True)

# Saves a value in Redis using a key
def set_cache(key, value):
    redis_client.set(key, value)


# Reads a cached value from Redis using its key
def get_cache(key):
    return redis_client.get(key)