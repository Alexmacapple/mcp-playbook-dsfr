URL:
https://main--ds-gouv.netlify.app/example/core/collapse

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


### Collapse


Toggle

- list item

- list item

-
Toggle nested

- list nested item

- list nested item

- list nested item


-
Close


Toggle

- list item

- list item

-
Toggle nested

- list nested item

- list nested item

- list nested item


-
Close


Toggle

- list item

- list item

-
Toggle nested

- list nested item

- list nested item

- list nested item


-
Close


###
Extrait de code


<div>
<!--
un bouton toggle (qui ouvre et qui ferme) doit avoir les attributs aria-expanded (qui définit son état) et l'attribut aria-controls (dont l'id détermine l'élément sur lequel agira le bouton.
un bouton reduce (qui ne peut que fermer) doit avoir uniquement l'attribut aria-controls.
-->
<div>
<button aria-expanded="true" aria-controls="collapsed-0" type="button" class="fr-mb-2v fr-btn">Toggle</button>
<ul class="fr-collapse" id="collapsed-0" data-fr-group="group-id">
<li>list item</li>
<li>list item</li>
<li>
<button aria-expanded="false" aria-controls="collapsed-0-nested" type="button" class="fr-mb-2v fr-btn">Toggle nested</button>
<ul class="fr-collapse" id="collapsed-0-nested">
<li>list nested item</li>
<li>list nested item</li>
<li>list nested item</li>
</ul>
</li>
<li>
<button aria-controls="collapsed-0" type="button" class="fr-mb-2v fr-btn">Close</button>
</li>
</ul>
</div>
<div>
<button aria-expanded="false" aria-controls="collapsed-1" type="button" class="fr-mb-2v fr-btn">Toggle</button>
<ul class="fr-collapse" id="collapsed-1" data-fr-group="group-id">
<li>list item</li>
<li>list item</li>
<li>
<button aria-expanded="false" aria-controls="collapsed-1-nested" type="button" class="fr-mb-2v fr-btn">Toggle nested</button>
<ul class="fr-collapse" id="collapsed-1-nested">
<li>list nested item</li>
<li>list nested item</li>
<li>list nested item</li>
</ul>
</li>
<li>
<button aria-controls="collapsed-1" type="button" class="fr-mb-2v fr-btn">Close</button>
</li>
</ul>
</div>
<div>
<button aria-expanded="false" aria-controls="collapsed-2" type="button" class="fr-mb-2v fr-btn">Toggle</button>
<ul class="fr-collapse" id="collapsed-2" data-fr-group="group-id">
<li>list item</li>
<li>list item</li>
<li>
<button aria-expanded="false" aria-controls="collapsed-2-nested" type="button" class="fr-mb-2v fr-btn">Toggle nested</button>
<ul class="fr-collapse" id="collapsed-2-nested">
<li>list nested item</li>
<li>list nested item</li>
<li>list nested item</li>
</ul>
</li>
<li>
<button aria-controls="collapsed-2" type="button" class="fr-mb-2v fr-btn">Close</button>
</li>
</ul>
</div>
</div>


Libellé bouton


Fermer


##
Paramètres d'affichage


Choisissez un thème pour personnaliser l'apparence du site.


Thème clair


Thème sombre


Système
Utilise les paramètres système
