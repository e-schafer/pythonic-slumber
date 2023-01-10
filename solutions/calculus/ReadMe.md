# Playoff Python -- Calculus

## Scenario 

Ton client t'a donné une série de fichiers de calculs dans un **format non standard** 
dont il souhaite avoir les résultats pour les intégrer en prod, sans avoir à 
systématiquement les calculer à la main.
Pourquoi ne pas lui faire une moulinette qui fait le travail automatiquement ? 

### Inputs

L'ensemble des fichiers de calculs que le client t'a donné en exemple sont dans 
le dossier `./resources`. 

Attention, il t'a prévenu que ces fichiers peuvent contenir des erreurs de 
syntaxes ou même fonctionnelles, ne prend rien pour acquis !

### Règles fonctionnelles

* Le client nous met à disposition plusieurs fichiers .txt
* Chaque ligne de ce fichier représente un calcule qui doit être traité (format `Operand Operator Operand`)
* Un opérande peut être soit :
	* un nombre (entier ou décimal) avec le format `Number(XX)`
	* un temps avec le format `Time(XXhYYYYYmSSSSSSs)` (60 minutes max n'est pas une certitude.)
* Les opérations attendues sont : 
	* `+` l'addition (nombre/nombre, temps/temps)
	* `-` la soustraction (nombre/nombre, temps/temps)
	* `*` la multiplication (nombre/nombre, temps/nombre)
	* `/` la division (nombre/nombre, temps/nombre)
* La sortie doit être de la forme : 
```
Nom_du_fichier_en_entree:
	* Operande Operator Operande = Resultat
	* Operande Operator Operande : Erreur (si la ligne est en erreur)
	* Operande Operator Operande = Resultat
```

