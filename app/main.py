from fastapi import FastAPI
from app.routers.internal import router as internal_router

app = FastAPI()

app.include_router(internal_router)

@app.get("/")
def health():
    return {"status": "Backend is running"}
