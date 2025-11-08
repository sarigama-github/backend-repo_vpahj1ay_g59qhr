from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Any, Dict
from bson import ObjectId

from database import db, create_document, get_documents
from schemas import Contact

app = FastAPI(title="Web Studio API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def test() -> Dict[str, Any]:
    # Verify DB connection
    try:
        await db.command("ping")
        status = "ok"
    except Exception as e:  # noqa: BLE001
        status = f"error: {e}"
    return {"status": status}


@app.post("/contact")
async def submit_contact(payload: Contact) -> Dict[str, Any]:
    data = payload.dict()
    doc = await create_document("contact", data)
    # Normalize ObjectId for JSON
    doc["_id"] = str(doc.get("_id", ""))
    return {"success": True, "data": doc}


@app.get("/packages")
async def list_packages() -> Dict[str, Any]:
    # Static packages for now (no need to persist)
    return {
        "items": [
            {
                "slug": "onepage",
                "name": "Onepage",
                "price": "à partir de 499€",
                "features": [
                    "Page unique impactante",
                    "Design sur-mesure",
                    "Optimisé mobile",
                    "Déploiement rapide",
                ],
            },
            {
                "slug": "vitrine",
                "name": "Vitrine",
                "price": "à partir de 1290€",
                "features": [
                    "Jusqu'à 5 pages",
                    "CMS léger",
                    "SEO de base",
                    "Formulaire de contact",
                ],
            },
            {
                "slug": "ecommerce",
                "name": "E‑commerce",
                "price": "sur devis",
                "features": [
                    "Catalogue & panier",
                    "Paiements sécurisés",
                    "Dashboard commandes",
                    "Intégrations tierces",
                ],
            },
        ]
    }
