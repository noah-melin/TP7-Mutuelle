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

    const response = await fetch('/calculer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nom, prenom, age, reponses })
    });

    const data = await response.json();

    // Afficher le résultat
    document.getElementById("displayNom").textContent = data.nom;
    document.getElementById("displayAge").textContent = data.age;
    document.getElementById("displayCout").textContent = data.cout_total;

    document.getElementById("resultat").style.display = "block";
});
