document.getElementById("inscriptionForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const nom = document.getElementById("nom").value;
    const prenom = document.getElementById("prenom").value;
    const age = document.getElementById("age").value;
    const reponses = Array.from(document.querySelectorAll('input[name="question"]:checked')).map(el => "Oui");

    const response = await fetch('/calculer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nom, prenom, age, reponses })
    });

    const data = await response.json();

    // Affichage du résultat
    document.getElementById("displayNom").textContent = `${prenom} ${nom}`;
    document.getElementById("displayAge").textContent = age;
    document.getElementById("displayCout").textContent = data.cout_total;

    document.getElementById("resultat").style.display = "block";
});
