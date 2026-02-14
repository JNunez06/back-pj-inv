from fastapi import FastAPI
from app.controllers.scraper_controller import router as scraper_router

app = FastAPI(title="Backend Tesis")

app.include_router(scraper_router)


@app.get("/")
def root():
    return {"mensaje": "API tesis activa"}
