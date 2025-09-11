URL:
https://main--ds-gouv.netlify.app/example/core/favicon

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


### Snippet à inclure dans <head></head>


###
Extrait de code


<meta name="theme-color" content="#000091"><!-- Défini la couleur de thème du navigateur (Safari/Android) -->
<link rel="apple-touch-icon" href="../../../dist/favicon/apple-touch-icon.png"><!-- 180x180 -->
<link rel="icon" href="../../../dist/favicon/favicon.svg" type="image/svg+xml">
<!-- si favicon.ico peut etre placé à la racine du serveur, retirer la ligne ci-dessous -->
<link rel="shortcut icon" href="../../../dist/favicon/favicon.ico" type="image/x-icon"><!-- 32x32 -->
<link rel="manifest" href="../../../dist/favicon/manifest.webmanifest" crossorigin="use-credentials">
<!-- Modifier les chemins relatifs des favicons en fonction de la structure du projet -->
<!-- Dans le fichier manifest.webmanifest aussi, modifier les chemins vers les images -->


#### Tailles et formats


L'icône de favori (favicon) du design système est disponible sous différents formats et tailles pour correspondre aux différents supports.

##### favicon.ico (32px)


![favicon svg](../../../dist/favicon/favicon.ico)


##### favicon.svg


![favicon svg](../../../dist/favicon/favicon.svg)


##### apple-touch-icon.png (180px)


![apple-touch-icon png](../../../dist/favicon/apple-touch-icon.png)


##### Chrome / Android icons (importées depuis le nanifest.webmanifest)


###### android-chrome-192x192.png (192px)


![Chrome / Android icon 192](../../../dist/favicon/android-chrome-192x192.png)


###### android-chrome-512xx512.png (512px)


![Chrome / Android icon 512](../../../dist/favicon/android-chrome-512x512.png)


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
