# test technique d'Enlapse

Dans un but de présentation, le code pour le Neural Network a été fait sur notebook

Le fichier __results__ contient les résultats sour forme de plot du programme __mating_opencv.py__ mais les données ne sont aps facileent visibles, je conseille la visualisation par opencv directement dans le programme.

## Process de développement

### Etape 1 : observation des data:

Termes clef : Image mating / Inpainting récupéré des notes de l'entretient

7 images + 1 mask pour enlever les ouvriers d’une image, la taille de la base de donnée est très faible donc on va devoir mettre un max d’epoch, heureusement que c’est seulement pr une photo sinn ça ne marcherait pas.

On observe que en fonction des images, les variables sont :
la météo
l’ensoleillement
le positionnement des ouvriers
Particulièrement à l’endroit ou il y a un mask, il y a une photo ou il y a un ouvrier ou parfois une grue : artefacts qu'on ne veut pas forcément.

Premières solutions pensées :
Opencv couper coller simple
A creuser surement bcp de manières de faire ca avec open cv
ML : entraînement avec un auto-encodeur convolutionnel pour reconstruire l’image


### Etape 2 : Recherches

Premières recherches : medium,  youtube , tensorflow tutorial

Solution simple déjà implémentéee dans opencv : à tester

Utilisation de la structure encodeur/decodeur pour faire l’inpaint

On utilise les images avec des trous à l’endroit de masks( = on met les px du mask à 0 ) puis
Utilisation de self attention pour remplire les trous :
https://www.youtube.com/watch?v=_RItAuNR_0s à 17min Intéressant, efficace mais couteux en temps je n'aurai pas le temps d'implémenter ca. On se contentera d'un autoencodeur "basique".

Autre solution : hallucination grand classifieur :
https://medium.com/jamieai/image-inpainting-with-deep-learning-dd8555e56a32
A tester ca a l'air fun et pas compliqué à faire

~30/45 min de taf

### Etape 3 : Expérimentation  et discussion des résultats

Fonctions opencv :
ouais bof ca fait cache misère mais cest rapide à utiliser , peut-être que ca serait mieux si il n’y avait pas les grilllages, ca créé bcp de petits patterns qui se répètent c’est pas évident

1H ~ de travail

ML à tester :
https://medium.com/jamieai/image-inpainting-with-deep-learning-dd8555e56a32

Idée : couper un carré autour du mask qui sera la partie à compléter afin d’éviter d’avoir de trop grosses données

auto encodeur
Marche pas bien, plsrs raisons :
    → base de données toute petit
→ préparation des données un peu simpliste (exemple : “trous” à remplire pas disposés de manière aléatoire )
    → Architecture très (trop) simple au vu du problème posé (utilisation de self attention pour régler le pb?)
fin de temps imparti

temps utilisé 3h et qq  : ~ 4h30/45 max au total

Hallucination : manque de temps :/
