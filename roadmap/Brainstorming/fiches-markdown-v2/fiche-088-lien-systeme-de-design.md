URL:
https://main--ds-gouv.netlify.app/example/component/link/back-to-top

Title:
Lien - Système de design

Markdown:

Lien - Système de design


DSFR v1.14.0


[Retour](../)


# Lien (link)


Le lien permet la navigation entre une page et un autre contenu au sein de la même page, du même site ou externe. Pour les actions d'un autre type - comme la soumission d'un formulaire - il faut utiliser le composant bouton.
[Documentation](https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lien)


## Retour en haut de page


Le lien de "retour en haut de page" est une ancre vers un élément dont l'id est "top".

Afin de le faire fonctionner correctement, il est nécessaire d'ajouter l'attribut id (id="top") sur l'élement le plus haut de la page comme le body (<body id="top" ...>) ou les liens d'évitement (<div class="fr-skiplinks" id="top">), afin que le focus de navigation soit lui aussi replacé en haut de page.

Le lien haut de page est un lien classique fr-link composé de l'icone arrow-up-fill , alignée à gauche, et du libellé "Haut de page".


Le lien peut être aligné sur la gauche ou la droite du contenu.


Actuce: Pour aligner le lien à droite, l'insérer dans une div class="fr-grid-row fr-grid-row--right" .


### Lien Haut de page - id="top"


[Haut de page](#top)


###
Extrait de code


<a id="link-4316" href="#top" class="fr-link fr-icon-arrow-up-fill fr-link--icon-left">Haut de page</a>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
