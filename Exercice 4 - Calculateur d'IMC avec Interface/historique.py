# Author: Émile
# Date: 2025-12-11
# But: Sauvegarder le calcul imc et le nom de la personnne dans un fichier
#      Lire le fichier et afficher son contenue
import datetime
import os

# variable globale temporaire pour tester la fonction
IMC = 21.37
NOM = "John Bloodborne"
IMC2 = 25.23
NOM2 = "Bob Darksouls"


def sauvegarder_calcul(nom: "str", imc: "float") -> "str":
    """
    ### Docstring for sauvegarder_calcul\n
    **Sauvegarde le fichier:** *historique-PrenomNom.txt*\n
    **dans le path:** *./.txt/Nom-Prenom*\n
    **Sous le format suivant:** *Date: mois/jour/annee;	Nom: Prenom Nom;	IMC: 00.00*\n

    :param nom: String qui contient le nom complet du user
    :type nom: "str"
    :param imc: Float qui contient le resultat du calcul IMC
    :type imc: "float"
    :return: Message annoncant le success de la sauvegarde
    :rtype: str
    """
    # path qui contien le fichier de sauvegarde pour chaque users
    path = f"./.txt/{nom.strip().replace(" ", '-')}" # → ex: .txt/John-Bloodborne

    # makedirs lance une erreur si le fichier existe deja le try permet d'a la fois verifier si le fichier existe et de le creer sinon
    try:
        os.makedirs(path)
    except:
        pass

    date = datetime.datetime.now()
    #Sauvegarde dans un fichier
    with open(f"{path}/historique-{nom.lower().title().strip().replace(" ", '')}.txt", "a") as f:
        #le open cherche a append un fichier avec le nom/path fournit, si il n'existe pas il le cree
        historique = f"Date: {date.strftime("%x")};\tNom: {nom.strip().lower().title()};\tIMC: {imc}\n"

        f.write(historique) #f.write append au fichier la ligne qui contient les donnnees a sauvegarder.
    return "Sauvegarder avec success!"


def afficher_historiquqe():
    #Lit le fichier
    pass

def main():
    #test de la fonction
    sauvegarder_calcul(NOM, IMC)
    sauvegarder_calcul(NOM2, IMC2)

if __name__ == "__main__":
    main()
