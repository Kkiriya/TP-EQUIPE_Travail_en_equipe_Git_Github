#----------------------Affiche les entrees du menu-----------------------------------------#
def afficher_entrees():
    """
    Affiche la liste des entrées disponible dans le menu.
    """
    print("Voici la liste des entrées: \n")
    entrees = [
        "1. Salade niçoise",
        "2. Soupe de tomate",
        "3. Tomate mozzarella"
    ]
    for plat in entrees:
        print(plat)


    

def afficher_plats_principaux():
    pass

def afficher_desserts():
    pass

def main():
    print("=== MENU DU RESTAURANT ===")
    # Les autres ajouteront leur code ici

if __name__ == "__main__":
    main()