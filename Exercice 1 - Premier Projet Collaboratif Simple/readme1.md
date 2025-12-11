## Exercice 1 : Premier Projet Collaboratif Simple

### Scénario 1

Créer ensemble un "menu du restaurant" en Python

### Tâches par Rôle (4 personnes)

**Personne 1 :** Chef de projet / Git Master
**-->** Émile

- Crée le dépôt sur GitHub
- Initialise le projet
- Crée le fichier `menu.py` avec structure de base
- Gère les pull requests

**Personne 2 :** Développeur Entrées
**-->** Nadjib

- Crée une fonction `afficher_entrees()`
- Ajoute 3 entrées au menu
- Pousse ses changements

**Personne 3 :** Développeur Plats Principaux
**-->** Neil

- Crée une fonction `afficher_plats_principaux()`
- Ajoute 3 plats principaux
- Pousse ses changements

**Personne 4 :** Développeur Desserts
**-->** Bruno

- Crée une fonction `afficher_desserts()`
- Ajoute 3 desserts
- Crée le `main()` pour tout afficher

### Instructions Techniques

```python
# Structure de départ (Personne 1)
def main():
    print("=== MENU DU RESTAURANT ===")
    # Les autres ajouteront leur code ici

if __name__ == "__main__":
    main()
```

### Défis Git

1. Chacun travaille sur sa propre branche
2. Résoudre un conflit simulé (deux personnes modifient le même plat)
3. Faire un merge en équipe

---
