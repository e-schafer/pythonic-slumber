# Playoff Python -- Francais

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

---
---

# Playoff Python -- English

## Language
The goal of this test is to assess the candidate's skills in python (3.11 for this test).

At least 3 levels of candidate skills will be noted:

- Beginner:
  - primarily scripting
  - weak use of python's native libraries
- Intermediate:
  - goes beyond scripting (beginning of OOP)
  - knows python concepts (e.g. for comprehension)
  - knows the basics of python tools (venv, black, setuptools, etc.)
- Expert:
  - programs in a structured manner
  - knows python libraries well
  - programs functionally in python

## Note for the examiner
Here are the topics that the playoff will check for the candidate:

- OOP Design (class, inheritance, self)
- Splitting strings / regexp
- Reading / writing to a file
- Design of python modules (not everything in the same file...)
- Error handling (try/except)
- Lambdas
- Functional programming

## Methods
Each function to be completed can be done in multiple ways.

An example of each way is described in the solution.

Unit tests are provided and they must pass.

## Setup
``` bash
# create a virtual environment
python -m venv .venv
# activate the environment
.venv\Scripts\activate
# install the package for consistency in module calls.
pip install -e .
```