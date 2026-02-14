from fastapi import APIRouter, HTTPException
from app.schemas.scraper_schema import ScrapeRequest
from app.services.playstore_service import scrapear_comentarios, leer_comentarios

router = APIRouter(prefix="/api", tags=["Scraper PlayStore"])


@router.post("/playstore")
def ejecutar_scraping(data: ScrapeRequest):

    try:
        total = scrapear_comentarios(data.url, data.quantity)
        return {
            "status": "ok",
            "comentarios_guardados": total
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/comments")
def obtener_comentarios():

    comentarios = leer_comentarios()

    return {
        "total": len(comentarios),
        "data": comentarios
    }
