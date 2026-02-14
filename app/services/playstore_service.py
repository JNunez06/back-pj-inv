from google_play_scraper import reviews, Sort
import re
import json
from pathlib import Path


DATA_PATH = Path("app/data/comments.json")


def extraer_app_id(url: str):
    match = re.search(r'id=([^&]+)', url)
    if not match:
        raise ValueError("No se pudo extraer el app id")
    return match.group(1)


def scrapear_comentarios(url: str, quantity: int):

    app_id = extraer_app_id(url)

    result, _ = reviews(
        app_id,
        lang="es",
        country="pe",
        sort=Sort.NEWEST,
        count=quantity
    )

    comments_only = [r["content"] for r in result]

    DATA_PATH.parent.mkdir(exist_ok=True)

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(comments_only, f, indent=2, ensure_ascii=False)

    return len(comments_only)


def leer_comentarios():

    if not DATA_PATH.exists():
        return []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
