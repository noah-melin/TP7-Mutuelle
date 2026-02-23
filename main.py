from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# 1. Configuration CORS
# Indispensable pour autoriser les requêtes venant de ton navigateur
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Route API : Calcul des mensualités
# Doit impérativement être placée AVANT le mount des fichiers statiques
@app.post("/calculer")
async def calculer_mensualites(request: Request):
    try:
        data = await request.json()
        nom = data.get("nom")
        prenom = data.get("prenom")
        # Conversion forcée en entier pour éviter les erreurs de calcul
        age_utilisateur = int(data.get("age"))
        reponses_questionnaire = data.get("reponses", [])

        # Logique métier du calcul
        cout_base = 50
        # Ajout de 10€ par réponse "Oui"
        cout_questions = reponses_questionnaire.count("Oui") * 10
        
        # Surcharge pour les seniors
        surcharge_age = 0
        if age_utilisateur > 65:
            surcharge_age = 0.02 * (age_utilisateur - 65) * cout_base
            
        cout_total = round(cout_base + cout_questions + surcharge_age, 2)

        return {
            "nom_complet": f"{prenom} {nom}", 
            "age": age_utilisateur, 
            "cout_total": cout_total
        }
    except Exception as e:
        # Renvoie une erreur propre au front-end si les données sont mal formées
        raise HTTPException(status_code=400, detail=str(e))

# 3. Servir les fichiers statiques (HTML, CSS, JS)
# Cette route "fourre-tout" est placée en dernier
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# 4. Point d'entrée pour lancer le serveur
if __name__ == "__main__":
    # On écoute sur toutes les interfaces (0.0.0.0) sur ton port spécifique
    uvicorn.run(app, host="0.0.0.0", port=8223)