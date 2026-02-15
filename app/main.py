from fastapi import FastAPI
from app.controllers.scraper_controller import router as scraper_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Backend Tesis")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scraper_router)


@app.get("/")
def root():
    return {"mensaje": "API tesis activa"}
