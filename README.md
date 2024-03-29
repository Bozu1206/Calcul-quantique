# Calcul Quantique
Repo du cours CS-308 : Calcul quantique donné au semestre de printemps 2022 ä l’EPFL. Durant le semestre, il y avait des devoirs à rendre et ceux-ci comptaient pour 20% de la note. À la fin, il y a également eu un projet sur les machines quantiques d’IBM Q qui comptait lui aussi pour 20% de la note. 

### Homework notés 

- [HW1](homework/QC_HWG1.pdf), note : 20/20
- [HW2](homework/QC_HWG2.pdf), note : 16/20
- [HW3](homework/QC_HWG3.pdf), note : 19.75/20
- [HW4](homework/QC_HWG4.pdf), note : 11/11

### Projet 

Ce projet visait à implémenter l’algorithme de Grover afin de trouver toutes les solutions du problème $3$-SAT suivant 

$$
f(x,y,z) = (\lnot x \lor \lnot y \lor\lnot z) \land (\lnot x \lor \lnot y \lor z)\land (\lnot x \lor y \lor z)\land(x \lor \lnot y \lor z)\land(x \lor y \lor \lnot z) \land (x \lor y \lor z)
$$

Le rapport est disponible [ici](projet/Mini_Project_Grover_X_3_SAT__Copy_.pdf) et le code [ici](projet/grover_algorithm.py). 
