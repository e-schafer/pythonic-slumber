# Sudoku

L'exercice consiste à faire un solver de sudoku en employant la technique du `backtracking`


Le backtracking est une technique de résolution de problèmes qui consiste à explorer récursivement toutes les possibilités jusqu'à trouver une solution valide ou à épuiser toutes les possibilités. On commence par une solution partielle et on ajoute des éléments un à un jusqu'à ce qu'on atteigne une impasse, auquel cas on revient en arrière et on essaie une autre possibilité.


## A faire
#### solver.py
Completer les méthodes :
- col_possibilities
- row_possibilities
- sector_possibilities
- solve

#### test/test_solver.py
Completer les tests:
- test_row_possibilities
- test_col_possibilities
- test_sector_possibilities_1