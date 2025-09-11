URL:
https://main--ds-gouv.netlify.app/example/core/spacing

Title:
Fondamentaux - Système de design

Markdown:

Fondamentaux - Système de design


DSFR v1.14.0


[Retour](../)


# Fondamentaux (core)


Le package core est utilisé comme fondation du Design System, il contient plusieurs éléments fondamentaux.


### Typographie


Les typographies Marianne(R) et Spectral sont les typographies officielles de la charte de l'État. Leur usage crée une cohérence entre les interfaces et offre une expérience positive à l'utilisateur. Leur respect renforce également la reconnaissance de la parole de l'État.


### Icônes


Les icônes fonctionnelles sont des symboles visuels qui accompagnent l'utilisateur dans ses actions et qui aident à sa compréhension de l'interface.


### Icônes de favoris - Favicon


L'icône de favoris est un petit icône associé à un site web. Il permet à l'utilisateur de repérer qu'il se trouve sur un site de l'état.


### Medias


Les médias désignent vos contenus photos et vidéos. Lorsqu'ils sont intégré à une page de contenu, il est recommandé de suivre les règles décrites ci-dessous.


### Grille


La grille proposée par le design system vous permet de structurer vos pages et vos contenus simplement.


##### Documentation


-
[Typographie](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-de-l-identite-de-l-etat/typographie/)


-
[Icônes](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/icones)


-
[Icônes de favoris - Favicon](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/icone-de-favoris)


-
[Médias fondamentaux](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/medias)


-
[Grille](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/grille-et-points-de-rupture)


## Espacements


###### Margin/padding


Des classes utilitaires sont disponibles pour gérer les marges intérieures et extérieures d'un élément html.


Celles-ci suivent la structure suivante (entre crochets les valeurs, facultatives, possibles):


- Pour le margin : fr-m[t/r/b/l/x/y]-[n]0[v]

- pour le padding : fr-p[t/r/b/l/x/y]-0[v]


- Le prefix : 'fr-',


- la lettre 'm' pour margin ou 'p' pour padding,


- l'orientation avec 't', 'r', 'b', 'l' (top, right, bottom, left) ou 'x', 'y' (horizontal, vertical),


- un séparateur : '-',


- le token d'espacement (nb: le signe '-' des nombres négatifs est remplacé par la lettre 'n', et 0 n'a pas d'unité 'v')


------------------------------


Classes d'espacements :


Classe
Description
Exemple d'espacement
Exemple de classe


fr-m-
Margin


fr-m-2v


fr-mt-
Margin top


fr-mt-2v


fr-mr-
Margin right


fr-mr-2v


fr-mb-
Margin bottom


fr-mb-2v


fr-ml-
Margin left


fr-ml-2v


fr-mx-
Margin left & right


fr-mx-2v


fr-my-
Margin top & bottom


fr-my-2v


fr-p-
Padding


fr-p-2v


fr-pt-
Padding top


fr-pt-2v


fr-pr-
Padding right


fr-pr-2v


fr-pb-
Padding bottom


fr-pb-2v


fr-pl-
Padding left


fr-pl-2v


fr-px-
Padding left & right


fr-px-2v


fr-py-
Padding top & bottom


fr-py-2v


###### Breakpoints


Il est possible de définir le breakpoint à partir du quel on applique l'espacement.


Il suffit d'ajouter à la classe le breakpoint (md) avant la valeur du token. ex: fr-p -md -4v


Pour adapter les espacements à la taille de l'écran, on peut ainsi combiner les classes en partant du mobile puis en surchargeant en md

### exemple avec un bouton plus large en md


4v en mobile / 16v en md


###
Extrait de code


<button type="button" class="fr-px-4v fr-px-md-16v fr-btn fr-btn">4v en mobile / 16v en md</button>


Valeurs des tokens d'espacements :


Token
rem
px
Exemple d'espacement
Exemple de classe


n8v
-2
-32


1
2


fr-ml-n8v


n7v
-1.75
-28


1
2


fr-ml-n7v


n6v
-1.5
-24


1
2


fr-ml-n6v


n5v
-1.25
-20


1
2


fr-ml-n5v


n4v
-1
-16


1
2


fr-ml-n4v


n3v
-0.75
-12


1
2


fr-ml-n3v


n2v
-0.5
-8


1
2


fr-ml-n2v


n1-5v
-0.375
-6


1
2


fr-ml-n1-5v


n1v
-0.25
-4


1
2


fr-ml-n1v


n0-5v
-0.125
-2


1
2


fr-ml-n0-5v


0
0
0


1
2


fr-ml-0


0-5v
0.125
2


1
2


fr-ml-0-5v


1v
0.25
4


1
2


fr-ml-1v


1-5v
0.375
6


1
2


fr-ml-1-5v


2v
0.5
8


1
2


fr-ml-2v


3v
0.75
12


1
2


fr-ml-3v


4v
1
16


1
2


fr-ml-4v


5v
1.25
20


1
2


fr-ml-5v


6v
1.5
24


1
2


fr-ml-6v


7v
1.75
28


1
2


fr-ml-7v


8v
2
32


1
2


fr-ml-8v


9v
2.25
36


1
2


fr-ml-9v


10v
2.5
40


1
2


fr-ml-10v


11v
2.75
44


1
2


fr-ml-11v


12v
3
48


1
2


fr-ml-12v


13v
3.25
52


1
2


fr-ml-13v


14v
3.5
56


1
2


fr-ml-14v


15v
3.75
60


1
2


fr-ml-15v


16v
4
64


1
2


fr-ml-16v


17v
4.25
68


1
2


fr-ml-17v


18v
4.5
72


1
2


fr-ml-18v


19v
4.75
76


1
2


fr-ml-19v


20v
5
80


1
2


fr-ml-20v


21v
5.25
84


1
2


fr-ml-21v


22v
5.5
88


1
2


fr-ml-22v


23v
5.75
92


1
2


fr-ml-23v


24v
6
96


1
2


fr-ml-24v


25v
6.25
100


1
2


fr-ml-25v


26v
6.5
104


1
2


fr-ml-26v


27v
6.75
108


1
2


fr-ml-27v


28v
7
112


1
2


fr-ml-28v


29v
7.25
116


1
2


fr-ml-29v


30v
7.5
120


1
2


fr-ml-30v


31v
7.75
124


1
2


fr-ml-31v


32v
8
128


1
2


fr-ml-32v


auto
NaN
NaN


1
2


fr-ml-auto


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
