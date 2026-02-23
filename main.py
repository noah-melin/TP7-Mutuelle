from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configuration CORS pour éviter les erreurs de cross-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir les fichiers statiques (HTML, CSS, JS)
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# Route pour calculer les mensualités
@app.post("/calculer")
async def calculer_mensualites(request: Request):
    data = await request.json()
    nom = data.get("nom")
    age = int(data.get("age"))
    reponses = data.get("reponses", [])

    # Logique de calcul des mensualités
    cout_base = 50
    cout_questions = reponses.count("Oui") * 10
    surcharge_age = 0
    if age > 65:
        surcharge_age = 0.02 * (age - 65) * cout_base
    cout_total = round(cout_base + cout_questions + surcharge_age, 2)

    return {"nom": nom, "age": age, "cout_total": cout_total}

# Lancement du serveur
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8173)  # Remplacez 8173 par votre port (ex: 8017 pour user17)
