# ZoneUtiles

Pour utiliser l'outil, exécuter main.py
 - Choisir un fichier .jpg à traiter
 - Choisir les paramètres de traitement d'image (des valeurs par default sont définies)'


## Pour utiliser avec des contours : 
- Aller dans le fichier MerAlgoContour.py,
- Modifier le main() avec les données du problème
- Exécuter ce fichier.

### Pour la saisie des données du problème
- Il faut crééer les contours (classe Outline)
- Modifier la taille de la plaque TOP, RIGHT, LEFT, BOTTOM _BOUNDARY, attention il ne faut pas qu'un contour soit parfaitement confondu avec un bord de la plaque
- Enfin il faut passer en parmètre un dictionnaire qui a comme clé un contour intérieur et en valeur une list des contours intérieurs associés

