import calcul
import historique

def demander_donnees():
    """Demande le poids et la taille à l'utilisateur."""
    try:
        poids = float(input("Entrez votre poids (kg): "))
        taille = float(input("Entrez votre taille (m): "))
        return poids, taille
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        return demander_donnees()

def afficher_resultat(imc):
    """Affiche l'IMC et sa catégorie."""
    print(f"Votre IMC est : {imc:.2f}")

    if imc < 18.5:
        print("Catégorie : Insuffisance pondérale")
    elif imc < 25:
        print("Catégorie : Poids normal")
    elif imc < 30:
        print("Catégorie : Surpoids")
    else:
        print("Catégorie : Obésité")

def lancer_interface():
    """Gère toute la logique d'interface du calculateur IMC."""
    poids, taille = demander_donnees()
    imc = calcul.calculer_imc(poids, taille)

    afficher_resultat(imc)
    historique.sauvegarder_imc(imc)

    print("\nIMC enregistré dans l'historique.")
