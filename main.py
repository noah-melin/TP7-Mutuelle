from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir les fichiers statiques
app.mount("/", StaticFiles(directory=".", html=True), name="static")

@app.post("/calculer")
async def calculer_mensualites(request: Request):
    try:
        data = await request.json()
        nom = data.get("nom")
        prenom = data.get("prenom")
        age_utilisateur = int(data.get("age"))
        reponses_questionnaire = data.get("reponses", [])

        # Calcul des mensualités
        cout_base = 50
        cout_questions = reponses_questionnaire.count("Oui") * 10
        surcharge_age = 0
        if age_utilisateur > 65:
            surcharge_age = 0.02 * (age_utilisateur - 65) * cout_base
        cout_total = round(cout_base + cout_questions + surcharge_age, 2)

        return {"nom_complet": f"{prenom} {nom}", "age": age_utilisateur, "cout_total": cout_total}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8182) 
