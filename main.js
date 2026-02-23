document.getElementById("inscriptionForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const nom = document.getElementById("nom").value;
    const prenom = document.getElementById("prenom").value;
    const age = document.getElementById("age").value;

    // Récupérer les réponses aux questions
    const reponses = [];
    for (let i = 1; i <= 5; i++) {
        const ouiChecked = document.querySelector(`input[name="q${i}"][value="Oui"]:checked`);
        if (ouiChecked) {
            reponses.push("Oui");
        }
    }

    try {
        const response = await fetch('/calculer', {  // URL relative
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nom, prenom, age, reponses })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Afficher les résultats
        document.getElementById("displayNom").textContent = data.nom_complet;
        document.getElementById("displayAge").textContent = data.age;
        document.getElementById("displayCout").textContent = data.cout_total;

        // Afficher le bloc de résultats
        document.getElementById("resultat").style.display = "block";

        // Faire défiler la page vers le résultat
        document.getElementById("resultat").scrollIntoView({ behavior: 'smooth' });
    } catch (error) {
        console.error("Erreur lors de la soumission du formulaire:", error);
        alert("Une erreur est survenue lors de la soumission du formulaire. Veuillez réessayer.");
    }
});
