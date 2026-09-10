from fastapi import FastAPI

app = FastAPI(
    title="Maps Weather Platform API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Backend is running"}