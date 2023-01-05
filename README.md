# Playoff Python

## Langage
Le but de tester les compétences du candidat sur python(3.11 pour ce test)

On notera au moins 3 niveaux de compétences du candidat:
- Débutant:
  - principalement du scripting
  - faible utilisation des librairies natives de python
- Intermediaire:
  - va au dela du scripting (debut de POO)
  - connait les concepts de python (ex: for comprehension)
  - connait les bases des outils de pythons (venv, black ,setuptools, ..)
- Expert:
  - programme de manière structurée
  - connait bien les libs de python
  - programme fonctionnellement en python
  
## Note pour l'examinateur
Voici les topics que le playoff va vérifier chez le candidat : 
* Conception OOP (class, héritage, self)
* Split de strings / regexp
* Lecture / écriture dans un fichier
* Conceptions de modules python (pas tout dans le même fichier...)
* La gestion d'erreur (try/except)
* Les Lambdas
* Programmation fonctionnelle

## Methodes
Chaque fonction à completer peut être réalisée de plusieurs manières. 

Un exemple de chaque manière est décrite dans la solution.

Des tests unitaires sont fournis ils devront passer au vert.


## Setup
``` bash
# créer un environnement virtuel
python -m venv .venv
# active l'environnement
.venv\Scripts\activate
# install le package pour avoir une consistence dans l'appel des modules.
pip install -e .
```