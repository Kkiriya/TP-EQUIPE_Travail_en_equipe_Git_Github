### Commandes de base: 
**Demarer:**
`git init` --> Initialiser un nouveau repo
`git status` --> voir l'etat actuel du repo
`git add fichier.py` --> ajouter un fichier au repo
`git add .` --> ajouter tous les fichiers au repo

**Sauvegarder:**
`git commit -am "message"` --> creer un commit
`git log` --> voir lhistorique de commit
`git log --oneline` --> historique condenser
`git diff` --> voir les modif apporter

### Manipuler les branches:
**Creer et Naviguer:**
`git branch` --> listes les branches
`git banch nom-branche --> creer une branche
`git checkout nom-branche` --> basculer sur la branche
`git checkout -b nom-branche` --> creer et bascule la branche

**Fusionner et Supprimer:**
`git checkout main` --> retourner sur main
`git merge nom-branche` -->  fusionne dans main
`git branch -d nom-branche` --> supprime la branche si fusionner
`git branch -D nom-branche` --> force la suppression de la branche

### Strategies de branches:

| Git flow                             | Github flow                   |
| ------------------------------------ | ----------------------------- |
| `main`: Code en production           | `main`: Toujours deployable   |
| `develop`: Integration des features  | Creer une branche par feature |
| `feature`: Nouvelles fonctionnalités | Commits regulier + push       |
| `release`: Preparation des versions  | Ouvrir une pull request       |
| `hotfix`: corrections urgentes       | review + discussion           |
|                                      | merge dans main               |

### Github et Collab

**Configuer un remote:**
`git remote add origin [URL]` --> ajoute un remore nommer *origin*
`git remote -v` --> voir les remotes configurer
`git remote remove origin` --> supprime un remote

**Clone un Repo (pour collaboration ou simplement avoir les fichier)**
`git clone [URL]` --> clone le repo et tous ses fichier
`git clone [URL] .` --> clone le repo dans le repertoire courant sans creer un nouveau repertoire

**Synchroniser:**
`git push -u origin main` --> envoyer + definir upstream (-u)
`git pull origin main` --> recuper + fusionner
`git fetch origin` --> recuperer sans fusionner
